#!/usr/bin/python3
""" This module checks if an object is exactly an
    instance of the specified class
"""


def is_same_class(obj, a_class):
    """ Return True if an object is an
        instance of the specified class otherwise False

        Arguments:
        obj: target object
        a_class: specified class
    """
    if type(obj) is a_class:
        return isinstance(obj, a_class)
