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
