#!/usr/bin/python3

"""[Module of the class Base]

    Returns:
        [Class]: [Parent class to almost a circle project]
    """


class Base:
    """[Defining Base class for project almost a circle]
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """[Contructor]

        Args:
            id (attributs of Base, id): [Incremental id]. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
