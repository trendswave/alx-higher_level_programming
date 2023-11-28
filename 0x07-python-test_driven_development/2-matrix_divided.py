#!/usr/bin/python3
''' Module 2 for task 1'''


def matrix_divided(matrix, div):
    ''' Divide each element of a matrix by dev '''
    errors = {
        'matrix': 'matrix must be a matrix (list of lists) of integers/floats',
        'row': 'Each row of the matrix must have the same size',
        'div': 'div must be a number',
        'zero': 'division by zero'
    }

    if type(matrix) != list:
        raise TypeError(errors['matrix'])

    row_size = None
    for row in matrix:
        # Check if the element is a list
        if type(row) is not list:
            raise TypeError(errors['matrix'])

        # Check the size of all sublist
        if row_size is None:
            row_size = len(row)
        elif row_size != len(row):
            raise TypeError(errors['row'])

        # Check that all the elements are int or flot
        status = all(type(el) in set([int, float]) for el in row)
        if status is False:
            raise TypeError(errors['matrix'])

    if type(div) not in [int, float]:
            raise TypeError(errors['div'])

    if div == 0:
            raise ZeroDivisionError(errors['zero'])

    new = map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix)
    return list(new)
