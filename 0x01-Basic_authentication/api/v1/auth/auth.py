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
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Auth header
        check request for authentication header
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return str(request.headers['Authorization'])

    def current_user(self, request=None) -> TypeVar('User'):
        """ current authenticated user
        """
        return None
