#!/usr/bin/env python3
"""
This module create a simple Flask App
"""
from flask import Flask, jsonify, request, abort, make_response, Response
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    """
    Simple method for testing
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def user() -> Response:
    """
    Method end-point should expect two form data fields:
    "email" and "password". If the user does not exist, the end-point should
    register it and respond with the following JSON payload
    """
    email = request.form.get('email')
    pwd = request.form.get('password')
    if email and pwd:
        try:
            AUTH.register_user(email, pwd)
            return jsonify({"email": email, "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> Response:
    """
    This method is made for the login step
    """
    email = request.form.get('email')
    pwd = request.form.get('password')
    if email and pwd:
        if AUTH.valid_login(email, pwd):
            session_id = AUTH.create_session(email)
            response = make_response('creating a cookie')
            response.set_cookie('session_id', session_id)
            return jsonify({"email": email, "message": "logged in"})
        else:
            abort(401)
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
