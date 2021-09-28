#!/usr/bin/python3
"""Defining class Square"""


class Square:
    """Class that represent a square"""

    def __init__(self, size=0):
        """Initializing square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
