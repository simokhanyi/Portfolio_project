#!/usr/bin/python3
"""
controller for retrieving etailed information about a specific team
"""


from models import Team


def get_team_details(team_id):
    """
    Retrieve detailed information about a specific team from the database.

    Args:
    - team_id (int): The unique identifier of the team.

    Returns:
    - dict: Dictionary containing team details.
    """
    team = Team.query.get(team_id)
    if team:
        # Format team details into JSON-friendly format
        team_details = {
            'id': team.id,
            'name': team.name,
        }
        return team_details
    else:
        return None
