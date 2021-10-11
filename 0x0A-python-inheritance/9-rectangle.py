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

    def area(self):
        """ Return the area of the rectangle """
        return self.__width * self.__height

    def __str__(self) -> str:
        """ Print the rectangle description """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
