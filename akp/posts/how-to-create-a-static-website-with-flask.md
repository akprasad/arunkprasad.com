title: How to Create a Static Website with Flask
date: 2022-01-05
description: Static sites are fast and simple. Learn how to create one with
             Flask and Flask-Frozen.

Static sites are dead simple: simple to make, simple to deploy, and simple to
serve. And *because* they're so simple, there are naturally [hundreds][ssg] of
ways to manage them.

Even so, we have excellent and time-tested web frameworks that we can repurpose
as static site generators with minimal effort. I made this website with Flask,
and in this post I'll show you how.

(You can see this site's source code [on GitHub][gh].)

[ssg]: https://jamstack.org/generators/
[gh]: https://github.com/akprasad/arunkprasad.com


# The application skeleton

If you're familiar with Flask already, you can skip this section. If not --
behold! Flask is delightfully lightweight:

    #!python
    from flask import Flask, render_template
    from flask_assets import Environment, Bundle


    app = Flask(__name__)

    # I use Flask-Assets to build and combine CSS and JS assets,
    # but this isn't strictly necessary.
    assets = Environment(app)
    css = Bundle("css/style.css", "css/pygments.css", output="gen/style.css")
    assets.register("site_css", css)


    def parse_post(slug: str):
        ...


    def load_all_posts():
        ...


    @app.route("/")
    def index():
        posts = load_all_posts()
        return render_template("index.html", posts=posts)


    @app.route("/log/<slug>/")
    def log(slug):
        post = parse_post(slug)
        return render_template("blog-post.html", post=post)


`render_template` uses [Jinja][jinja] templates by default. Both of my
templates above inherit from `base.html`, which defines my boilerplate:

[jinja]: https://jinja.palletsprojects.com/en/3.0.x/

    #!jinja
    <!doctype html>
    <html>
      <head>
        <title>{% block title %}{% endblock %}</title>
        {% assets "site_css" %}
        <link rel="stylesheet" rel="stylesheet" href="{{ ASSET_URL }}">
        {% endassets %}

        {# Needed for sane display on mobile. #}
        <meta name="viewport" content="width=device-width, initial-scale=1">
      </head>
      <body>
        {% block body %}
        {% endblock %}
      </body>
    </html>

Since the end result is a static website, dynamic Flask features like session
management and form submissions naturally won't work. This isn't an issue as
long as you stick to the basics: routes, templates, and no stateful logic.


# Writing posts with Markdown and Pygments

I write posts in Markdown with some extra metadata:

    #!text
    title: My post title
    date: 2022-01-05

    This is my **post**.

Then I process these posts with `python-markdown`, with two extensions:

- `meta` for post metadata (the `title` and `date` fields above)
- `codehilite` for code syntax highlighting.

Both of these extensions are provided with the default `markdown` package.
Here's the basic setup:

    #!python
    import markdown
    md = markdown.Markdown(extensions=["meta", "codehilite"])

    # OK, the API here is a little wonky.
    # Hat tip to: https://stackoverflow.com/questions/66438307
    content = md.convert(text)
    title = md.Meta["title"][0]
    date = md.Meta["date"][0]

`codehilite` uses Pygments under the hood. You can generate Pygments CSS from
the command line:

    #!bash
    # https://python-markdown.github.io/extensions/code_hilite/
    # https://pygments.org/docs/cmdline/
    # https://pygments.org/styles/
    pygmentize -S solarized-light -f html -a .codehilite >> style.css

The default CSS works well enough, but I had some issues with its whitespacing
around line numbers and made some small changes to the defaults.


# Deploying with Frozen-Flask

Frozen-Flask can generally discover app URLs on its own. For most of my use
cases, it works out of the box with no extra config:

    #!python
    from flask_frozen import Freezer

    app.debug = False
    freezer = Freezer(app)

    # By default, `freezer` writes to the `build` directory
    freezer.freeze()

Then deployment is as simple as running the script above and syncing the output
to prod:

    #!bash
    ./freeze.py
    rsync -r build <server_destination>


# Scaling this setup

I've scaled this setup by caching rendered text content and re-rendering only
when the source file changes. While I haven't used this approach for a truly
massive setup with millions of static files, it has been totally sufficient for
my needs.

Overall, I love using Flask to create static websites. I can use a mature
framework that I love, lean on its rich ecosystem of plugins, and easily move
to a dynamic application if necessary.
