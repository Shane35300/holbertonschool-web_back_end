#!/usr/bin/env python3
"""
SessionAuth class to make new authentication mechanism.
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    new authentication mechanism:
    validate if everything inherits correctly without any overloading
    validate the “switch” by using environment variables
    """
    pass
