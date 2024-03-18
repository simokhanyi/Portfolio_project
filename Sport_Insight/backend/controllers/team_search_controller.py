#!/usr/bin/python3
"""
Search for teams in the database
"""


from models import Team


def search_teams(query):
    """
    Search for teams in the database based on the provided query.

    Args:
    - query (str): The search query to filter teams.

    Returns:
    - list: List of dictionaries containing team information.
    """
    # Perform database query to search for teams
    teams = Team.query.filter(Team.name.ilike(f'%{query}%')).all()
    # Format teams into JSON-friendly format
    formatted_teams = [{'id': team.id, 'name': team.name} for team in teams]
    return formatted_teams
