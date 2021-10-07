#!/usr/bin/python3
""" Module that says a name with a last name"""


def say_my_name(first_name, last_name=""):
    """[Function that say the name with the input strings]

    Args:
        first_name ([str]): [First name, which is mandatory]
        last_name (str, optional): [Last name that can be gived or not].
        Defaults to "".

    Raises:
        TypeError: [If the name gived not is a string]
        TypeError: [If the last name gived not is a string]
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
