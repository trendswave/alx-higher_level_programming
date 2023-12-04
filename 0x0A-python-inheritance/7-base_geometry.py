#!/usr/bin/python3
'''Module class BaseGeometry'''


class BaseGeometry:
    '''Class BaseGeometry'''

    def area(self):
        '''Method not implemented'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validate value by type and value'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
