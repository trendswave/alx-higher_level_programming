#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for item in my_list:
        val =item % 2 == 0
        result.append(val)
            return result
