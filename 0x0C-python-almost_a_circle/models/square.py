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
        """Getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """overloading __str__ method by returning
        [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update by assigning an argument to each attribute"""
        if len(args) > 0:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                if index == 1:
                    self.size = value
                if index == 2:
                    self.x = value
                if index == 3:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
