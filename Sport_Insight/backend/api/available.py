#!/usr/bin/python3
"""Endpoint to retrieve available players and teams."""

from flask import jsonify
from database.models import Player, Team


@app.route('/api/players/available', methods=['GET'])
def get_available_players_and_teams():
    """
    Retrieve available players and teams from the database.

    Returns:
        dict: A dictionary containing available players and teams.
    """
    try:
        # Query the database for available players and teams
        available_players = Player.query.all()
        available_teams = Team.query.all()

        # Convert player objects to dictionaries
        available_players_data = [
            {'id': player.player_id, 'name': player.player_name}
            for player in available_players
        ]

        # Convert team objects to dictionaries
        available_teams_data = [
            {'id': team.team_id, 'name': team.team_name}
            for team in available_teams
        ]

        # Combine player and team data into a dictionary
        available_data = {'players': available_players_data,
                          'teams': available_teams_data}

        return jsonify(available_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
