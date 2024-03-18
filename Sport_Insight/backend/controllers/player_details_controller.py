#!/usr/bin/python3
"""
Retrieve detailed information about a specific player
"""


from models import Player


def get_player_details(player_id):
    """
    Retrieve detailed information about a specific player from the database.

    Args:
    - player_id (int): The unique identifier of the player.

    Returns:
    - dict: Dictionary containing player details.
    """
    player = Player.query.get(player_id)
    if player:
        # Format player details into JSON-friendly format
        player_details = {
            'id': player.id,
            'name': player.name,
            'team': player.team.name,
            # Add additional player details as needed
        }
        return player_details
    else:
        return None
