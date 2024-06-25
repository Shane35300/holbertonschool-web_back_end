#!/usr/bin/env python3
"""
This module create a simple Flask App
"""
from flask import Flask, jsonify, request, abort, make_response, Response
from flask import redirect, url_for
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
    This method is made for the login step. It returns a response
    """
    email = request.form.get('email')
    pwd = request.form.get('password')
    if email and pwd:
        if AUTH.valid_login(email, pwd):
            print("pwd is valid")
            session_id = AUTH.create_session(email)
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie('session_id', session_id)
            return response, 200
        else:
            print("pwd is not valid")
            abort(401)
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> Response:
    """
    This method is made for the logout step. It returns a response
    """
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            return jsonify({"Location": "/"}), 200
        else:
            abort(403)
    else:
        abort(403)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> Response:
    """
    This method contains a session_id cookie. Use it to find the user.
    If the user exist, respond with a 200 HTTP status and the following
    JSON payload
    """
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": user.email}), 200
        else:
            abort(403)
    else:
        abort(403)


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> Response:
    """
    The request is expected to contain form data with the "email" field. If
    the email is not registered, respond with a 403 status code. Otherwise,
    generate a token and respond with a 200 HTTP status and the following
    JSON payload
    """
    email = request.form.get('email')
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email,
                        "reset_token": token}), 200
    except ValueError:
        abort(403)


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password() -> Response:
    """
    Update the password. If the token is invalid, catch the exception and
    respond with a 403 HTTP code. If the token is valid,
    respond with a 200 HTTP code
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
