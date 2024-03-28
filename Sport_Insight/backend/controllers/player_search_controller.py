#!/usr/bin/python3
"""Search for players in the database controller"""


from flask import jsonify
from database.models import Player


def search_players(query):
    """
    Search for players based on the given query.

    Args:
        query (str): The search query to filter players.

    Returns:
        list: A list of dictionaries representing the search results.
    """
    # Perform the search query in your database
    # Example: Search players whose name contains the query
    players = Player.query.filter(Player.player_name.ilike(f'%{query}%')).all()

    # Convert the search results to a list of dictionaries
    player_data = [{'player_id': player.player_id,
                    'player_name': player.player_name} for player in players]

    return player_data
