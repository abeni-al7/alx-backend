#!/usr/bin/env python3
"""A simple flask application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """A simple route"""
    return render_template("index.html") or "Hello world"


if __name__ == "__name__":
    app.run()
