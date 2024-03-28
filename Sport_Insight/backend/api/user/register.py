#!/usr/bin/python3
"""
User Registration to Database API Endpoint
"""


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql://root:@Masasa12@localhost/SportInsight'
)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not (username and email and password):
        return jsonify({'error': 'Missing required fields'}), 400

    # Check if username or email already exists in the database
    if (User.query.filter_by(username=username).first() or
            User.query.filter_by(email=email).first()):
        return jsonify({'error': 'Username or email already exists'}), 409

    # Create a new user object and add it to the database
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


if __name__ == '__main__':
    app.run(debug=True)
