#!/usr/bin/python3
'''Module for advanced'''


class MyInt(int):
    '''Rebel class'''

    def __eq__(self, other):
        '''Override == operator'''
        return not (self is not other)

    def __ne__(self, other):
        '''Override != operator'''
        return (self is not other)
