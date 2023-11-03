#!/usr/bin/python3
from hidden_4 import *
if __name__ == '__main__':
    for el in dir():
        if el[0] == el[1] == '_':
            continue
        print(el)
