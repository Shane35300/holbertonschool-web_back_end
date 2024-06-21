#!/usr/bin/env python3
"""
SessionAuth class to make new authentication mechanism.
"""

from api.v1.auth.auth import Auth
from models.user import User
import uuid
import os
from api.v1.views import app_views
from flask import request, jsonify


class SessionAuth(Auth):
    """
    new authentication mechanism:
    validate if everything inherits correctly without any overloading
    validate the “switch” by using environment variables
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        instance method def create_session(self, user_id: str = None) -> str:
        that creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        instance method def user_id_for_session_id() that
        returns a User ID based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        value = self.user_id_by_session_id.get(session_id)
        return value

    def current_user(self, request=None):
        """
        Return a User instance based on a cookie value _my_session_id in the
        request.

        Args:
            request: Flask request object

        Returns:
            User instance if session ID is valid and corresponds to a user,
            None otherwise
        """
        if request is None:
            return None
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def handles_all_routes():
    """ view that handles all routes for the Session authentication
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
