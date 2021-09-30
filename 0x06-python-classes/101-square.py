#!/usr/bin/python3
"""Defining class square"""


class Square:
    """Representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter of position"""
        if type(value) is not tuple or len(value) != 2 \
                or not all(type(el) == int for el in value) or min(value) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes the area of a square"""
        return self.size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print()
            return
        [print() for el in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")

    def __str__(self):
        """Print of the class"""
        if self.size == 0:
            print()
            return

        return "\n" * self.__position[1] + (self.__size *
                                            (" " * self.__position[0] +
                                             "#" * self.__size + "\n"))[:-1]
