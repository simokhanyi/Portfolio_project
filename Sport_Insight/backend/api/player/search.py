#!/usr/bin/python3
""" API to search players"""
from flask import Flask, request, jsonify
from controllers.player_search_controller import search_players


app = Flask(__name__)


@app.route('/api/player/search', methods=['GET'])
def player_search():
    """
    Player Search API Endpoint

    Search for players based on specified criteria such as player name or
    team affiliation.

    Query Parameters:
    - query (str): The search query to filter players. Required.

    Returns:
    - 200 OK: JSON response with search results.
    - 400 Bad Request: Missing query parameter.
    """
    query = request.args.get('query')
    if query:
        players = search_players(query)
        return jsonify(players), 200
    else:
        return jsonify({'error': 'Missing query parameter'}), 400
