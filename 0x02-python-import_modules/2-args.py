#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))
    idx = 1
    for element in argv[1:]:
        print("{}: {}".format(idx, element))
        idx += 1
