#!/usr/bin/env python3
"""
SessionAuth class to make new authentication mechanism.
"""

from api.v1.auth.auth import Auth
import uuid


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
        value = SessionAuth.user_id_by_session_id.get(session_id)
        return value