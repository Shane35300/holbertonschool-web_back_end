#!/usr/bin/env python3
"""
Basic Flask app, All your functions and coroutines must be type-annotated
"""
from flask import Flask, render_template
from typing import Any
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Class that has a LANGUAGES class attribute equal to ["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app, default_locale=app.config['BABEL_DEFAULT_LOCALE'],
              default_timezone=app.config['BABEL_DEFAULT_TIMEZONE'])


@app.route("/", strict_slashes=False)
def hello_world() -> Any:
    """
    Home page with "Hello world" as header
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=False)
