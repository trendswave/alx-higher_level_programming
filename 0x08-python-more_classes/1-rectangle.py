#!/usr/bin/python3
'''class rectangle'''


class Rectangle:
    '''Form'''

    def __init__(self, width=0, height=0):
        '''Constructor'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Get the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        '''Get the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the height'''
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
