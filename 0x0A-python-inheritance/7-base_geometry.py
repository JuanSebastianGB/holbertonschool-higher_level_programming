#!/usr/bin/python3
""" Module of BaseGeometry"""


class BaseGeometry:
    """Defining class BaseGeometry"""

    def area(self):
        """ Raise an exceptino if area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Function that validate value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
