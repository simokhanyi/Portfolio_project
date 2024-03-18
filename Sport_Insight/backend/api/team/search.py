#!/usr/bin/python3
"""
Search for teams based on specified criteria
"""

from flask import Flask, request, jsonify
from controllers.team_search_controller import search_teams


app = Flask(__name__)


@app.route('/api/team/search', methods=['GET'])
def team_search():
    """
    Team Search API Endpoint

    Search for teams based on specified criteria such as team name or
    recent match results.

    Query Parameters:
    - query (str): The search query to filter teams. Required.

    Returns:
    - 200 OK: JSON response with search results.
    - 400 Bad Request: Missing query parameter.
    """
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    teams = search_teams(query)
    return jsonify(teams), 200
