#!/usr/bin/python3
"""
User Registration API Endpoint
"""


from flask import Flask, request, jsonify
from controllers.user_controller import register_user


app = Flask(__name__)


@app.route('/api/user/register', methods=['POST'])
def user_registration():
    """
    User Registration API Endpoint

    Register a new user account on the SportInsight platform.

    Request Body:
    - email (str): Email address of the user. Required.
    - password (str): Password for the user account. Required.

    Returns:
    - 201 Created: JSON response with success message.
    - 400 Bad Request: Missing or invalid request body parameters.
    """
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing or invalid email or password'}), 400

    email = data['email']
    password = data['password']

    # Attempt to register the user
    success, message = register_user(email, password)
    if success:
        return jsonify({'message': message}), 201
    else:
        return jsonify({'error': message}), 400
