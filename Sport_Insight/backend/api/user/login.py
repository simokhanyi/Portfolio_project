#!/usr/bin/python3
"""
User Authentication API Endpoint
"""

from flask import Flask, request, jsonify
from controllers.user_controller import authenticate_user


app = Flask(__name__)


@app.route('/api/user/login', methods=['POST'])
def user_authentication():
    """
    User Authentication API Endpoint

    Authenticate a user's credentials for logging in to the platform.
    Request Body:
    - email (str): Email address of the user. Required.
    - password (str): Password for the user account. Required.

    Returns:
    - 200 OK: JSON response with authentication token.
    - 401 Unauthorized: Invalid credentials.
    """
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing or invalid parameters'}), 400

    email = data['email']
    password = data['password']

    # Attempt to authenticate the user
    token = authenticate_user(email, password)
    if token:
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401


if __name__ == '__main__':
    app.run(debug=True)
