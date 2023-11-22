#!/usr/bin/python3
'''
square class definition
'''


class Square():
    '''
    Square class with private attribute size
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Initialize method for the Square class
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
            self.position = position

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

    @property
    def position(self):
        '''
        Returns the position of the square
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        Sets the position of the square
        '''
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''
        Returns area of the square
        '''
        return self.__size ** 2

    def my_print(self):
        '''
        Prints out the square
        '''
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            row = ' ' * self.position[0]
            row += ''.join('#' for c in range(self.size))
            print('\n'.join(row for r in range(self.size)))
