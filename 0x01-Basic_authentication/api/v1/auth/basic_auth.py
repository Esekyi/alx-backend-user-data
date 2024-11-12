#!/usr/bin/env python3
""" BasicAuth module
"""
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization header
        """
        if authorization_header is None or type(
                authorization_header
        ) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None or type(
                base64_authorization_header) is not str:
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
