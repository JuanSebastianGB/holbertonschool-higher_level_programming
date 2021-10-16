#!/usr/bin/python3
"""Module with class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Creating square"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """overloading __str__ method by returning
        [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.width)
