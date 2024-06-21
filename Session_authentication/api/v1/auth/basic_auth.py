#!/usr/bin/env python3
"""
BasicAuth class to manage API authentication.
"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class to manage API authentication """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for
        Basic Authentication.

        Args:
            authorization_header (str): The Authorization header string.

        Returns:
            str: The Base64 part of the Authorization header if present and
            valid, None otherwise.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Decodes the Base64 part of the Authorization header.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        Extracts user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Search for the user by email
        users = User.search({'email': user_email})
        if not users or len(users) == 0:
            return None

        user = users[0]

        # Check if the password is valid
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieve the User instance for a request using Basic Authentication.
        """
        if request is None:
            return None

        # Extract Authorization header from request
        authorization_header = request.headers.get('Authorization')

        # Extract Base64 part from Authorization header
        base64_part = self.extract_base64_authorization_header(
            authorization_header)

        # Decode Base64 string to get user credentials
        decoded_credentials = self.decode_base64_authorization_header(
            base64_part)

        # Extract user credentials (email and password)
        user_email, user_pwd = self.extract_user_credentials(
            decoded_credentials)

        # Retrieve User instance based on credentials
        user = self.user_object_from_credentials(user_email, user_pwd)

        return user
