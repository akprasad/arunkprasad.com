#!/usr/bin/env python3

"""Build the site."""

import glob
import os

from flask_frozen import Freezer

from akp import app


PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(PROJECT_DIR, "build")


app.debug = False
app.config["FREEZER_DESTINATION"] = OUTPUT_DIR
freezer = Freezer(app)


if __name__ == "__main__":
    freezer.freeze()
    print("Written to: " + OUTPUT_DIR)
