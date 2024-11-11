#!/usr/bin/env python3
""" Authentication class to manage API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require paths authentication.
        checks whether a path requires authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Auth header
        check request for authentication header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current authenticated user
        """
        return None
