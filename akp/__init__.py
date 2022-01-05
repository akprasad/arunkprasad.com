import os
from dataclasses import dataclass

import markdown
from flask import Flask, render_template
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
    content: str


def parse_post(slug: str):
    with open(f"{PROJECT_DIR}/posts/{slug}.md") as f:
        text = f.read()

    md = markdown.Markdown(extensions=["meta", "codehilite"])
    content = md.convert(text)
    content = content.replace("--", "&mdash;")

    return Post(
        title=md.Meta["title"][0],
        slug=slug,
        date=md.Meta["date"][0],
        content=content,
    )


def load_all_posts():
    with os.scandir(f"{PROJECT_DIR}/posts") as it:
        for entry in it:
            if entry.is_file():
                slug, _, _ = entry.name.partition(".")
                yield parse_post(slug)


@app.route("/")
def index():
    posts = load_all_posts()
    return render_template("index.html", posts=posts)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/log/<slug>/")
def log(slug):
    post = parse_post(slug)
    return render_template("blog-post.html", post=post)
