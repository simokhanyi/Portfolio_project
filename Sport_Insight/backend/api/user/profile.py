#!/usr/bin/python3
"""
User Profile API
"""

from flask import Flask, request, jsonify
from models import User

app = Flask(__name__)


@app.route('/api/user/profile', methods=['GET'])
def get_user_profile():
    # Get the user's email from the request headers.
    user_email = request.headers.get('email')

    # Check if the user email is provided in the headers
    if not user_email:
        return jsonify({'error': 'User email not provided in headers'}), 400

    # Query the database to fetch user information
    user = User.query.filter_by(email=user_email).first()

    # Check if the user exists in the database
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Return the user's profile information
    user_data = {
        'username': user.username,
        'email': user.email,
        'profile': user.profile
    }
    return jsonify(user_data), 200


if __name__ == '__main__':
    app.run(debug=True)
