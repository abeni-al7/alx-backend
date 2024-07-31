#!/usr/bin/env python3
"""A simple flask application"""
from flask import Flask, render_template
from flask_babel import Babel, Locale
from pytz import timezone


class Config:
    """A configuration class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object = Config
babel = Babel(app)


@app.route("/")
def index() -> str:
    """A simple route"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
