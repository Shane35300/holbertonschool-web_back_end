#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template, request
from typing import Any
from flask_babel import Babel, gettext

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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def hello_world() -> Any:
    """
    Home page  with "Hello world" as header
    """
    title = gettext("home_title")
    header = gettext("home_header")
    return render_template('3-index.html', title=title, header=header)


if __name__ == "__main__":
    app.run(debug=True)
