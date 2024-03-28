#!/usr/bin/python3
"""Endpoint to retrieve available players and teams."""

from flask import jsonify
from database.models import Player, Team


@app.route('/api/players/available', methods=['GET'])
def get_available_players_and_teams():
    """Retrieve available players and teams from the database."""
    try:
        players = Player.query.all()
        teams = Team.query.all()
        data = {
            'players': [{'id': p.player_id,
                         'name': p.player_name} for p in players],
            'teams': [{'id': t.team_id, 'name': t.team_name} for t in teams]
        }
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
