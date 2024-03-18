#!/usr/bin/python3
"""
controller for compare api
"""


from models import Player, Team


def compare_entities(entity_type, entity_id_1, entity_id_2):
    """
    Compare the performance of two players or teams.

    Args:
    - entity_type (str): Type of entities to compare ('player' or 'team').
    - entity_id_1 (int): ID of the first entity to compare.
    - entity_id_2 (int): ID of the second entity to compare.

    Returns:
    - dict: Dictionary containing comparison results.
    """
    if entity_type == 'player':
        entity_1 = Player.query.get(entity_id_1)
        entity_2 = Player.query.get(entity_id_2)
    elif entity_type == 'team':
        entity_1 = Team.query.get(entity_id_1)
        entity_2 = Team.query.get(entity_id_2)
    else:
        return None

    if entity_1 and entity_2:
        # Perform comparison logic and generate results
        comparison_results = {
            'entity_1': {
                'id': entity_1.id,
                'name': entity_1.name,
                # Include relevant performance metrics or statistics for 1
            },
            'entity_2': {
                'id': entity_2.id,
                'name': entity_2.name,
                # Include relevant performance metrics or statistics for 2
            },
            # Include comparison metrics or statistics
        }
        return comparison_results
    else:
        return None
