#!/usr/bin/python3
""" This module that can be used to check attributes and methods of an object
"""


def lookup(obj):
    """ This function returns a list of attributes and methods of 'obj'
    """
    return dir(obj)
