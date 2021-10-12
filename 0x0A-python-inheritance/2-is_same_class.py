#!/usr/bin/python3

""" Module of the same class function"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an instance
    of the specified class ; otherwise False."""
    return type(obj) == a_class
