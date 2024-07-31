#!/usr/bin/env python3
"""A simple flask application"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index() -> str:
    """A simple route"""
    return render_template("index.html") or "Hello world"


if __name__ == "__name__":
    app.run()
