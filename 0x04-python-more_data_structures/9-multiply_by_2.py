#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = {}
    for k in a_dictionary:
        new_dict[k] = 2 * a_dictionary[k]

    return new_dict
