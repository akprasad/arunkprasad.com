arunkprasad.com
===============

Personal website.


Helper commands
---------------

Generate Pygments styles:

    # https://python-markdown.github.io/extensions/code_hilite/
    # https://pygments.org/docs/cmdline/
    # https://pygments.org/styles/
    pygmentize -S monokai -f html -a .codehilite >> akp/static/style.css

Linting:

    black .

Devserver:

    python runserver.py

Deploy:

    ./production/deploy.py
