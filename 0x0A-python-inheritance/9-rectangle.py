#!/usr/bin/python3
'''Module subclass Rectangle'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Subclass of BaseGeometry'''

    def __init__(self, width, height):
        '''Constructor'''
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height

    def area(self):
        '''Calculates the area of a rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''Return the string representation of a rectangle'''
        msg = '[Rectangle] {}/{}'.format(self.__width, self.__height)
        return msg
