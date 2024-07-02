#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """
    Home page  with "Hello world" as header
    """
    return render_template('0-index.html')
