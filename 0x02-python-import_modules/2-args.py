#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(length - 1))
        i = 1
        for n in range(1, length):
            print("{}: {}".format(i, argv[n]))
            i += 1
