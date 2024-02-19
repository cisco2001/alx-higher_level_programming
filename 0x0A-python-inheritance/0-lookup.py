#!/usr/bin/python3
""" This is a module consisting of a function that can be used to check attributes and methods of an object
"""


def lookup(obj):
	return obj.__dir__()
