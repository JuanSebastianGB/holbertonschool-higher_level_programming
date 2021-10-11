#!/usr/bin/python3
""" Module of BaseGeometry"""


class BaseGeometry:
    """Defining class BaseGeometry"""
    pass

    def area(self):
        """ Raise an exceptino if area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Function that validate value"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
