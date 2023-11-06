#!/usr/bin/python3


def return_value(tuple_v, idx):
    if idx >= len(tuple_v):
        return 0

    return tuple_v[idx]


def add_tuple(tuple_a=(), tuple_b=()):
    a = return_value(tuple_a, 0) + return_value(tuple_b, 0)
    b = return_value(tuple_a, 1) + return_value(tuple_b, 1)

    return (a, b,)
