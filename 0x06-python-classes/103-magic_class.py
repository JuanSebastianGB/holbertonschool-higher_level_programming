#!/usr/bin/python3
"""Python class MagicClass"""

import math


class MagicClass:
    def __init__(self, radius=0):
        """Construct/initializes magic class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Computing area of the circle in magic class"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Computing circumference of the circle in magic class"""
        return 2 * math.pi * self.__radius
