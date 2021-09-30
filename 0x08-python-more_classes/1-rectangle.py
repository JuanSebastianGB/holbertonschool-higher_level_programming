#!/usr/bin/python3
"""Defining class Rectangle"""


class Rectangle:
    """Representing a rectangle"""

    def __init__(self, width=0, height=0):
        """Constructing the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Setter of width"""
        return self.__width

    @property
    def height(self):
        """Setter of height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Getter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Getter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
