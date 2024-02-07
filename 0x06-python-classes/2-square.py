#!/usr/bin/python3
""" This module demonstrates use of private instance attributes
    together with instantiation
"""


class Square:
    """ square with specified size, size must be integer and greater than zero
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
