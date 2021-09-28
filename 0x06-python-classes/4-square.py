#!/usr/bin/python3
"""Defining the class square"""


class Square:
    """Representing a square"""

    def __init__(self, size=0):
        """Constructing a square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

    @property  # getter
    def size(self):
        """Getter of the size of the square"""
        return self.__size

    @size.setter  # setter
    def size(self, value):
        """Setter of the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Cumputes area of the square"""
        return self.size ** 2
