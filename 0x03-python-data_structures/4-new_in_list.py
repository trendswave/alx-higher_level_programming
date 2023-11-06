#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # handle the case where the index (idx) is negative or out of range
    while idx < 0 or idx >= len(my_list):
        return my_list[:]
    #modifies the first list , n== new
    n_list = my_list[:]
    # replace the element at that index
    n_list[idx] = element
    return n_list

