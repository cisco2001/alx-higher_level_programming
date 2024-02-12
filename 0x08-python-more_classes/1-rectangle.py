#!/usr/bin/python3
""" Module for a class that defines a rectangle with specific width and height
"""


class Rectangle:
    """ A rectangle with specified width and height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieve rectangle width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """set rectangle width
        """
        if isinstance(width, int):
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ retrieve rectangle height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ set rectangle height
        """
        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
