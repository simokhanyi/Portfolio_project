#/usr/bin/python3
"""
Retrieve detailed information about a specific player
"""

from flask import Flask, request, jsonify
from controllers.player_details_controller import get_player_details


app = Flask(__name__)


@app.route('/api/player/details', methods=['GET'])
def player_details():
    """
    Player Details API Endpoint

    Retrieve detailed information about a specific player, including
    performance statistics.

    Query Parameters:
    - player_id (int): The unique identifier of the player. Required.

    Returns:
    - 200 OK: JSON response with player details.
    - 400 Bad Request: Missing player_id parameter.
    - 404 Not Found: Player with the specified ID not found.
    """
    player_id = request.args.get('player_id')
    if not player_id:
        return jsonify({'error': 'Missing player_id parameter'}), 400

    player_details = get_player_details(player_id)
    if player_details:
        return jsonify(player_details), 200
    else:
        return jsonify({'error': 'Player not found'}), 404
