#!/usr/bin/python3
""" API to search players"""

from flask import Flask, request, jsonify
from models import Player


app = Flask(__name__)


@app.route('/api/players/search', methods=['GET'])
def search_players():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    # Query the database for players based on the search query
    players = Player.query.filter(Player.name.ilike(f'%{query}%')).all()

    # Convert the player objects to a list of dictionaries
    player_data = (
        [{'id': player.id, 'name': player.name,
          'team': player.team} for player in players]
    )

    return jsonify(player_data)


if __name__ == '__main__':
    app.run(debug=True)
