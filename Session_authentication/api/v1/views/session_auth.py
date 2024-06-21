#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views
import os
from models.user import User
from flask import request, jsonify, abort


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """
    Handles user logout by destroying the session.

    Returns:
        - JSON empty dictionary with status code 200 if successful
        - 404 error if logout fails
    """
    from api.v1.app import auth

    if not auth.destroy_session(request):
        abort(404)

    return jsonify({}), 200


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def handles_all_routes() -> str:
    """
    Handles the login route for session authentication.

    This view retrieves email and password from the POST request,
    validates them, and creates a session ID if the credentials are correct.

    Returns:
        - JSON response with user details and sets a session cookie if
        successful.
        - JSON error message and appropriate HTTP status code if there are
        errors.
    """
    email = request.form.get('email')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    users = User.search({'email': email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth

        session_id = auth.create_session(user.id)
        response = jsonify(user.to_json())
        session_name = os.getenv('SESSION_NAME')
        response.set_cookie(session_name, session_id)
        return response

