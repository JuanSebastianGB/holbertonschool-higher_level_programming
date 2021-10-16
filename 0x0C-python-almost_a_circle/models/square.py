#!/usr/bin/python3
"""Module with class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Creating square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
