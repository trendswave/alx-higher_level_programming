#!/usr/bin/python3


def best_score(a_dictionary):
    max_v = None
    key = None
    if a_dictionary:
        for k in a_dictionary:
            if max_v is None:
                max_v = a_dictionary[k]
                key = k
            elif a_dictionary[k] > max_v:
                max_v = a_dictionary[k]
                key = k

        return key

    return key
