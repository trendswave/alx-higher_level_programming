#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for item in my_list:
        val = True if item % 2 == 0 else False
        result.append(val)
            return result
