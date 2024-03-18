#!/usr/bin/python3
"""
Compare the performance of two players or teams.
"""

from flask import Flask, request, jsonify
from controllers.compare_controller import compare_entities


app = Flask(__name__)


@app.route('/api/compare', methods=['GET'])
def compare():
    """
    Compare API Endpoint

    Compare the performance of two players or teams.

    Query Parameters:
    - entity_type (str): Type of entities to compare ('player' or 'team').
    - entity_id_1 (int): ID of the first entity to compare. Required.
    - entity_id_2 (int): ID of the second entity to compare. Required.

    Returns:
    - 200 OK: JSON response with comparison results.
    - 400 Bad Request: Missing or invalid query parameters.
    - 404 Not Found: Entity with the specified ID not found.
    """
    entity_type = request.args.get('entity_type')
    entity_id_1 = request.args.get('entity_id_1')
    entity_id_2 = request.args.get('entity_id_2')
    # Validate query parameters
    if not entity_type or entity_type not in ['player', 'team']:
        return jsonify({'error': 'Invalid entity_type parameter'}), 400
    if not entity_id_1 or not entity_id_2:
        return jsonify({'error': 'Missing entity_id parameters'}), 400

    comparison_results = compare_entities(entity_type,
                                          entity_id_1, entity_id_2)
    if comparison_results:
        return jsonify(comparison_results), 200
    else:
        return jsonify({'error': 'Entity not found'}), 404
