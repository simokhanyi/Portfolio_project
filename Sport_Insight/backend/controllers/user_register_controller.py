#!/usr/bin/python3
"""
User Registration API controller
"""

from models import User
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()


def register_user(email, password):
    """
    Register a new user account on the SportInsight platform.

    Args:
    - email (str): Email address of the user.
    - password (str): Password for the user account.

    Returns:
    - tuple: Tuple indicating success or failure of the registration process.
    """
    # Check if the email is already registered
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return False, 'Email address is already registered'

    # Hash the password before storing it
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user object
    new_user = User(email=email, password=hashed_password)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return True, 'User registration successful'
