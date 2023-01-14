#!/usr/bin/python3
"""function that returns the JSON
representation of an object (string)
"""

def to_json_string(my_obj):
    """function that accept an argument"""

    return json.dump(my_obj)
