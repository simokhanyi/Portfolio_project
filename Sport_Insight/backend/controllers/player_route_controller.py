#!/usr/bin/python3
"""Endpoint to retrieve routes of a player."""

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


# MySQL database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '@Masasa12',
    'database': 'SportInsight'
}


# Route to fetch player details by player name
@app.route('/players/<string:player_name>', methods=['GET'])
def get_player_details(player_name):
    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # Query to fetch player details by player name
        query = "SELECT * FROM Players WHERE player_name = %s"
        cursor.execute(query, (player_name,))

        # Fetch the results
        player_details = cursor.fetchone()

        if player_details:
            return jsonify(player_details), 200
        else:
            return jsonify({'error': 'Player not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # Close the database connection
        cursor.close()
        connection.close()


if __name__ == '__main__':
    app.run(debug=True)
