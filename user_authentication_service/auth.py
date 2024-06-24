#!/usr/bin/env python3
"""
This module defines a _hash_password method that takes in a password string
arguments and returns bytes
"""

import bcrypt


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
