#!/usr/bin/python3
"""Search for players in the database controller"""


from models import Player


def search_players(query):
    """
    Search for players in the database based on the provided query.

    Args:
    - query (str): The search query to filter players.

    Returns:
    - list: List of dictionaries containing player information.
    """
    # Perform database query to search for players
    players = Player.query.filter(Player.name.ilike(f'%{query}%')).all()
    # Format players into JSON-friendly format
    formatted_players = [{'id': player.id, 'name': player.name,
                          'team': player.team.name} for player in players]
    return formatted_players
