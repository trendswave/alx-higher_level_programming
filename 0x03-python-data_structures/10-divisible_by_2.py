#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []

    for item in my_list:
        val = True
        if item % 2 == 0:
            val = False
            if item % 2 != 0:
                result.append(val)
        return result
