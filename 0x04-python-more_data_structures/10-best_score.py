#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
    max_score = max(a_dictionary.values())
    for keys,values in a_dictionary.items():
        if values == max_score:
            return keys
