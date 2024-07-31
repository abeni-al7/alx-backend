#!/usr/bin/env python3
"""A simple babel setup"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """A class for configuring flask babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Gets the best locale from request"""
    return request.accept_languages.best


@app.route('/')
def get_index() -> str:
    """Returns a simple route"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
