#!/usr/bin/python3
""" Addition of 2 integers """


def add_integer(a, b=98):
    """[Addition of 2 numbers]

    Args:
        a ([int]): [Mandatory integer]
        b (int, optional): [Optional integer to sum]. Defaults to 98.

    Raises:
        TypeError: [Show error if a or b are not integer and not float]

    Returns:
        [int]: [Addition of the inputs]
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
