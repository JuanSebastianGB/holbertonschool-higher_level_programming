#!/usr/bin/python3

""" Module of add_attribute if doesn's exists """


def add_attribute(obj, attr_to_add, value_to_add):
    """ adds a new attribute to an object if it’s possible """

    if not hasattr(obj, "__dict__"):
        """ identify if has not an atrtribute """
        raise TypeError("can't add new attribute")
    setattr(obj, attr_to_add, value_to_add)
