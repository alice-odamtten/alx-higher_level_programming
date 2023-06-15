#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    maxnum = None
    best = None
    for key, value in a_dictionary.items():
        if maxnum is None or value > maxnum:
            maxnum = value
            best = key
    return best
