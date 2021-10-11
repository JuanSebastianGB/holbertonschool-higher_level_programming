#!/usr/bin/python3
""" Module of the class MyList  """


class MyList(list):
    """ Defining a subclasss of list"""

    def __init__(self):
        """ Starting object """
        super().__init__()

    def print_sorted(self):
        """ Using function inherited from parent"""
        print(sorted(self))
