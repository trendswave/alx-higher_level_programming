#!/usr/bin/python3
for k in range(0, 10):
     for p in range((k+1), 10):
        if (k != 8) or (p != 9):
            print("{}{},".format(k, p), end=" ")
        else:
            print("{}{}".format(k, p))
