#!/usr/bin/python3
""" Module of square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defining class square"""

    def __init__(self, size) -> None:
        """ Consturctor of the class Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns the area of square """
        return self.__size ** 2
