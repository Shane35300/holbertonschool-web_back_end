#!/usr/bin/env python3
"""
Auth class to manage API authentication.
"""

from flask import request
from typing import List, TypeVar
import os


class Auth:
    """
    This class provides methods to handle authentication and authorization for
    API endpoints.
    """
    def session_cookie(self, request=None):
        """Return the value of the session cookie from the request."""
        if request is None:
            return None
        cookie_name = os.getenv('SESSION_NAME')
        if cookie_name is None:
            return None
        return request.cookies.get(cookie_name)

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a given path requires authentication.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not require
            authentication.

        Returns:
            bool: True if the path is not in the excluded_paths list, False
            otherwise.
        """
        if path is None:
            return True
        if not excluded_paths or excluded_paths is None:
            return True

        # Add slash if not present
        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header value from the request.

        Args:
            request: Flask request object.

        Returns:
            str: Value of the Authorization header, or None if not found.
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None - request will be the Flask request object """
        return None
