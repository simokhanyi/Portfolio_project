#!/usr/bin/python3
"""
Retrieve detailed information about a specific team
"""

from flask import Flask, request, jsonify
from controllers.team_details_controller import get_team_details


app = Flask(__name__)


@app.route('/api/team/details', methods=['GET'])
def team_details():
    """
    Team Details API Endpoint

    Retrieve detailed information about a specific team,
    including player roster and recent match results.

    Query Parameters:
    - team_id (int): The unique identifier of the team. Required.

    Returns:
    - 200 OK: JSON response with team details.
    - 400 Bad Request: Missing team_id parameter.
    - 404 Not Found: Team with the specified ID not found.
    """
    team_id = request.args.get('team_id')
    if not team_id:
        return jsonify({'error': 'Missing team_id parameter'}), 400

    team_details = get_team_details(team_id)
    if team_details:
        return jsonify(team_details), 200
    else:
        return jsonify({'error': 'Team not found'}), 404
