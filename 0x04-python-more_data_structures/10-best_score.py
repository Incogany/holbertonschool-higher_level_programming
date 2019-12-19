#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    m = sorted(a_dictionary.values())
    value_max = m[-1]
    for i in a_dictionary:
        if value_max == a_dictionary[i]:
            return i
