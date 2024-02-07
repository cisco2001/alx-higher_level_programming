#!/usr/bin/python3
""" This module demonstrate how to use private instance attribute
"""


class Square:
    """ a square with size '__size'
    """
    def __init__(self, size):
        self.__size = size
