#!/usr/bin/python3
""" Module of Rectangle"""
BaseGemotry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGemotry):
    """ Defining Class Rectangle"""

    def __init__(self, width, height):
        """ Construct of the function"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
