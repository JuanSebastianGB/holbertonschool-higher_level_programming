#!/usr/bin/python3
"""Defining class Square"""


class Square:
    """Representing a square"""

    def __init__(self, size=0):
        """Initializing square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Compute Area of a square"""
        return self.__size ** 2
