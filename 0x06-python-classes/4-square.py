#!/usr/bin/python3
'''
Square class definition
'''


class Square():
    '''
    Square class with private attribute size
    '''
    def __init__(self, size=0):
        '''
        Args:
            size: size of the square
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        '''
        Returns the size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Sets the size of the square
        Args:
            value: value to be evaluated
        '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
