#!/usr/bin/env python3
"""A simple babel setup"""
from flask_babel import Babel, _
from flask import Flask, g, render_template, request

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    locale = request.args.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """Returns a simple route"""
    return render_template('3-index.html')


def get_user() -> dict | None:
    """Returns a user dictionary or None"""
    user_id = request.args.get("login_as")
    if not user_id or user_id not in users:
        return None
    return users[user_id]


@app.before_request
def before_request() -> None:
    """Gets a user and sets it to flask"""
    user = get_user()
    g.user = user


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
