#!/usr/bin/python3
""" module that computes area and perimeter of a rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """ Initializes width and height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve rectangle width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Set Rectangle width
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
        """Retrieve rectangle height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Set reactangle height
        """
        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("width must be an integer")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.height + self.width)
