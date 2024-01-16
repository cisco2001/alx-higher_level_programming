#!/usr/bin/python3
for ascii_code in range(ord('a'), ord('z') + 1):
    if ascii_code != ord('q') and ascii_code != ord('e'):
        print("{}".format(chr(ascii_code)), end="")
