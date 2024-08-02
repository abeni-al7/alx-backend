#!/usr/bin/env python3
"""A simple babel setup"""
import datetime
from flask_babel import Babel, _, format_datetime
from flask import Flask, g, render_template, request
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError

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


def get_user() -> dict | None:
    """Returns a user dictionary or None"""
    user_id = request.args.get("login_as")
    if not user_id or user_id not in users:
        return None
    return users[user_id]


@babel.localeselector
def get_locale() -> str:
    """Gets the best locale from request"""
    locale = request.args.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale
    user = get_user()
    locale = user["locale"]
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> str:
    """Returns appropriate timezone for user"""
    time_zone = request.args.get("timezone")
    if time_zone:
        try:
            timezone(time_zone)
            return time_zone
        except UnknownTimeZoneError:
            pass
    user = get_user()
    time_zone = user["timezone"]
    if time_zone:
        try:
            timezone(time_zone)
            return time_zone
        except UnknownTimeZoneError:
            pass
    return "UTC"


@app.before_request
def before_request() -> None:
    """Gets a user and sets it to flask"""
    setattr(g, 'user', get_user())
    setattr(g, 'time', format_datetime(datetime.datetime.now()))


@app.route('/')
def get_index() -> str:
    """Returns a simple route"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
