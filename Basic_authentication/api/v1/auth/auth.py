#!/usr/bin/env python3
"""
Auth class to manage API authentication.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    This class provides methods to handle authentication and authorization for
    API endpoints.
    """
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
        """ Returns None - request will be the Flask request object """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None - request will be the Flask request object """
        return None
