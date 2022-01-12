#!/usr/bin/env python3

import datetime
import re
import sys


def new_post(title):
    slug = re.sub("\s+", "-", title.lower())
    date = datetime.datetime.today().strftime("%Y-%m-%d")
    content = "\n".join(
        [
            f"title: {title}",
            f"description: A new blog post",
            f"date: {date}",
        ]
    )
    path = f"akp/posts/{slug}.md"
    with open(path, "w") as f:
        f.write(content)
    print(f"Created new post at {path}.")


def main(command, *args):
    if command == "new_post":
        new_post(*args)
    else:
        raise Exception(f"Unknown argument {command}")


if __name__ == "__main__":
    main(*sys.argv[1:])
