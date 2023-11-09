#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list == []:
        return 0

    prod = 0
    res_sum = 0
    for t in my_list:
        t_list = list(t)
        prod += t_list[0] * t_list[1]
        res_sum += t_list[1]

    return prod / res_sum
