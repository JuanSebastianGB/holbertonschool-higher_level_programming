#!/usr/bin/python3
"""Defining class square"""


class Square:
    """Representing a square"""

    def __init__(self, size=0):
        """Initializing square"""
        self.size = size

    @property
    def size(self):
        """Getter of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of __size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes the area of the square"""
        return self.size ** 2

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
