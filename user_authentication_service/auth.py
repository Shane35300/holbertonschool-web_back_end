#!/usr/bin/env python3
"""
This module defines a _hash_password method that takes in a password string
arguments and returns bytes
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def update_password(self, reset_token: str, password: str):
        """ Use the reset_token to find the corresponding user. If it does not
        exist, raise a ValueError exception.
        Otherwise, hash the password and update the user’s hashed_password
        field with
        the new hashed password and the reset_token field to None.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError("User not found")
        hashed_password = _hash_password(password)
        self._db.update_user(user.id, hashed_password=hashed_password,
                             reset_token=None)

    def get_reset_password_token(self, email: str) -> str:
        """
        take an email string argument and returns a string.
        """
        try:
            user = self._db.find_user_by(email=email)
            new_uuid = _generate_uuid()
            self._db.update_user(user.id, reset_token=new_uuid)
            return new_uuid
        except NoResultFound:
            raise ValueError
        except InvalidRequestError:
            raise ValueError

    def destroy_session(self, user_id: int) -> None:
        """
        The method takes a single user_id integer argument and returns None
        """
        self._db.update_user(user_id, session_id=None)
        return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        It takes a single session_id string argument and returns the
        corresponding User or None
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
            if user:
                return user
            else:
                return None
        except NoResultFound:
            return None
        except InvalidRequestError:
            return None

    def valid_login(self, email: str, password: str) -> bool:
        """
        Try locating the user by email. If it exists, check the password with
        bcrypt.checkpw. If it matches return True. In any other case,
        return False
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                if bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password):
                    return True
                return False
        except NoResultFound:
            return False

    def register_user(self, email: str, password: str) -> User:
        """
        This method takes mandatory email and password string arguments and
        return a User object
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User " + email + " already exists")
        except NoResultFound:
            pass
        user = self._db.add_user(email, _hash_password(password))
        return user

    def create_session(self, email: str) -> str:
        """
        This method should find the user corresponding to the email, generate
        a new UUID and store it in the database as the user’s session_id,
        then return the session ID.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                new_uuid = _generate_uuid()
                self._db.update_user(user.id, session_id=new_uuid)
                return new_uuid
        except NoResultFound:
            return None
        except InvalidRequestError:
            return None


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password.
    """
    salt = bcrypt.gensalt()
    encrypted_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return encrypted_pwd


def _generate_uuid() -> str:
    """
    This method generates a uuid4, converts it into a string and returns it
    """
    new_uuid = uuid.uuid4()
    return str(new_uuid)
