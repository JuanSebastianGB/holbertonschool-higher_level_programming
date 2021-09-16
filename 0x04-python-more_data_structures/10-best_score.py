#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict):
        return None
    for key, value in a_dictionary.items():
        if max(a_dictionary.values()) == value:
            return key
    return None
