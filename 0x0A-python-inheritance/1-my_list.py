#!/usr/bin/python3
'''Module for task 1'''


class MyList(list):
    '''Subclass of list'''

    def print_sorted(self):
        '''Print a list in sorted ascending'''
        print(sorted(self))
