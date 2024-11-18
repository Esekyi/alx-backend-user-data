#!/usr/bin/env python3
"""Session authentication module"""
import requests
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """SessionAuth class inherited from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session ID for user_id"""
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return user based on id from a Session"""
        if session_id is None or type(session_id) is not str:
            return None
        return str(self.user_id_by_session_id.get(session_id))

    def current_user(self, request=None):
        """overload function that returns a User based on session ID"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user
