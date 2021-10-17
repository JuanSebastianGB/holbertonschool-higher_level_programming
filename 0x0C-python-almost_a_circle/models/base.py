#!/usr/bin/python3

"""[Module of the class Base]

    Returns:
        [Class]: [Parent class to almost a circle project]
    """
import json


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            dicts = []
        dicts = [el.to_dictionary() for el in list_objs]
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dicts))

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file with json string representation"""
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, mode="r", encoding="utf-8") as f:
                f = cls.from_json_string(f.read())
            return [cls.create(**el) for el in f]
        except IOError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        else:
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy
