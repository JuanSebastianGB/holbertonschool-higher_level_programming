#!/usr/bin/python3
""" Module of square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defining class square"""

    def __init__(self, size) -> None:
        """ Consturctor of the class Square"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns the area of square """
        return self.__size ** 2

    def __str__(self) -> str:
        """ Print the description of the Square """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
