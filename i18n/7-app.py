#!/usr/bin/env python3
"""
Basic Flask app, All your functions and coroutines must be type-annotated
"""
from flask import Flask, render_template, request, g
from typing import Any
from flask_babel import Babel, gettext
import pytz
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)


class Config():
    """
    Class that has a LANGUAGES class attribute equal to ["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_locale() -> str:
    """
    Determine the best match with our supported languages
    """
    forced_locale = request.args.get('locale')
    if forced_locale and forced_locale in app.config['LANGUAGES']:
        return forced_locale
    user = get_user()
    if user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request() -> None:
    """
    use get_user to find a user if any, and set it as a global on flask.g.user
    """
    user_dict = get_user()
    if user_dict:
        g.user = user_dict


def get_user() -> dict:
    """
    Function that returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed
    """
    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }
    login_as = request.args.get('login_as')
    if login_as:
        login_as = int(login_as)
        for key, value in users.items():
            if key == login_as:
                return value
    return None


def get_timezone() -> str:
    """
    Find timezone parameter in URL parameters
    Find time zone from user settings
    Default to UTC
    """
    tz_name = request.args.get('timezone')
    if tz_name:
        try:
            pytz.timezone(tz_name)
            return tz_name
        except UnknownTimeZoneError:
            pass
    user = get_user()
    if user and user['timezone']:
        try:
            pytz.timezone(user['timezone'])
            return user['timezone']
        except UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/", strict_slashes=False)
def hello_world() -> Any:
    """
    Home page  with "Hello world" as header
    """
    user = getattr(g, 'user', None)
    message = gettext("not_logged_in")
    if user:
        username = user['name']
        message = gettext("logged_in_as") % {'username': username}
        title = gettext("home_title")
        header = gettext("home_header")
        return render_template('6-index.html', username=username, title=title,
                               header=header, message=message)
    title = gettext("home_title")
    header = gettext("home_header")
    return render_template('6-index.html', title=title,
                           header=header, message=message)


if __name__ == "__main__":
    app.run(debug=True)
