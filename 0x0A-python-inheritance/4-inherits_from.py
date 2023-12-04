#!/usr/bin/python3
'''Module for task 4'''


def inherits_from(obj, a_class):
    '''Returns True if obj inherits from a_class, False'''
    return issubclass(type(obj), a_class) and type(obj) != a_class
