#!/usr/bin/python3

""" This Defines the print_square function"""


def print_square(size):
    """[Print a matrix of #, depending on the input size]

    Args:
        size ([int]): [size of the square]

    Raises:
        TypeError: [if size is not a valid number]
        ValueError: [if size is less than 0]
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise ValueError("size must be an integer")
    if size == 0:
        return

    string = "#" * size + "\n"
    string *= size
    print(string[:-1])
