#!/usr/bin/env python3
"""
Basic Flask app, All your functions and coroutines must be type-annotated
"""
from flask import Flask, render_template
from typing import Any

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world() -> Any:
    """
    Home page  with "Hello world" as header
    """
    return render_template('0-index.html')
