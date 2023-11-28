#!/usr/bin/python3
''' Module 4 for task 3 '''


def print_square(size):
    ''' Print a square with size '''
    errors = {
        'int': 'size must be an integer',
        'zero': 'size must be >= 0'
    }

    if type(size) is not int:
        raise TypeError(errors['int'])

    if size < 0:
        raise ValueError(errors['zero'])

    for i in range(size):
        print('#' * size)
