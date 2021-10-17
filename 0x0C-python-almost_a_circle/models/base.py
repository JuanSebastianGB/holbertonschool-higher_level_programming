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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            dicts = []
        dicts = [el.to_dictionary() for el in list_objs]
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dicts))
