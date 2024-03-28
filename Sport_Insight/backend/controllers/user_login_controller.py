#!/usr/bin/python3
"""
Authenticate a user's credentials for logging in
"""

from models import User
from flask_bcrypt import Bcrypt
import jwt
from datetime import datetime, timedelta


bcrypt = Bcrypt()
SECRET_KEY = 'your_secret_key_here'


def authenticate_user(email, password):
    """
    Authenticate a user's credentials for logging in to the platform.

    Args:
    - email (str): Email address of the user.
    - password (str): Password for the user account.

    Returns:
    - str: Authentication token if credentials are valid, None otherwise.
    """
    # Retrieve the user from the database
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        # Generate JWT token
        payload = {
            'user_id': user.id,
            'email': user.email,
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')
    else:
        return None
