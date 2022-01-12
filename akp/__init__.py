import os
from dataclasses import dataclass
from datetime import datetime
from typing import List

import markdown
import pytz
from flask import Flask, Response, render_template
from flask_assets import Environment, Bundle


PROJECT_DIR = os.path.dirname(__file__)
app = Flask(__name__)

assets = Environment(app)
css = Bundle("css/style.css", "css/pygments.css", output="gen/style.css")
assets.register("site_css", css)


@dataclass
class Post:
    title: str
    slug: str
    date: str
    description: str
    draft: bool
    content: str
    ordering: int

    @property
    def iso_datetime(self):
        dt = datetime.fromisoformat(self.date)
        dt = dt.replace(tzinfo=pytz.timezone("America/Los_Angeles"))
        return dt.isoformat()


def parse_document(directory: str, slug: str):
    md = markdown.Markdown(extensions=["meta", "codehilite", "admonition"])

    document_path = os.path.join(directory, f"{slug}.md")
    with open(document_path) as f:
        text = f.read()
    content = md.convert(text)
    content = content.replace("--", "&mdash;")
    ordering = int(md.Meta.get("ordering", 0))

    return Post(
        title=md.Meta["title"][0],
        slug=slug,
        date=md.Meta["date"][0],
        description=" ".join(md.Meta["description"]),
        content=content,
        # Draft if this is set at all, for simplicity.
        draft=bool(md.Meta.get("draft")),
        ordering=ordering,
    )


def sort_documents(documents: List[Post]) -> List[Post]:
    return reversed(sorted(documents, key=lambda p: (p.date, p.ordering)))


def load_all_documents(directory: str) -> List[Post]:
    documents = []
    with os.scandir(directory) as it:
        for entry in it:
            if entry.is_file():
                slug, _, _ = entry.name.partition(".")
                documents.append(parse_document(directory, slug))
    return sort_documents(documents)


def parse_log_post(slug: str):
    directory = f"{PROJECT_DIR}/posts"
    return parse_document(directory=directory, slug=slug)


def parse_page(slug: str):
    directory = f"{PROJECT_DIR}/pages"
    return parse_document(directory=directory, slug=slug)


def load_all_posts() -> List[Post]:
    return load_all_documents(f"{PROJECT_DIR}/posts")


def load_all_pages() -> List[Post]:
    return load_all_documents(f"{PROJECT_DIR}/pages")


@app.route("/")
def index():
    posts = [p for p in load_all_posts() if not p.draft]
    return render_template("index.html", posts=posts)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/log/<slug>/")
def log(slug):
    post = parse_log_post(slug)
    return render_template("blog-post.html", post=post)


@app.route("/drafts/")
def drafts():
    posts = [p for p in load_all_posts() if p.draft]
    return render_template("index.html", posts=posts)


@app.route("/drafts/<slug>/")
def draft(slug):
    post = parse_log_post(slug)
    return render_template("blog-post.html", post=post)


@app.route("/pages/")
def pages():
    page_map = {p.slug: p for p in load_all_pages()}
    return render_template("pages.html", pages=page_map)


@app.route("/pages/<slug>/")
def page(slug):
    page = parse_page(slug)
    return render_template("blog-post.html", post=page)


@app.route("/atom.xml")
def atom_feed():
    posts = [p for p in load_all_posts() if not p.draft]
    text = render_template("atom.xml", posts=posts)
    return Response(text, mimetype="application/xml")
