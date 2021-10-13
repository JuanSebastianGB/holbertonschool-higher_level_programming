#!/usr/bin/python3
""" Module that contain class Student """


class Student:
    """ Definition of student """

    def __init__(self, first_name, last_name, age) -> None:
        """ Creation of student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return the json representation of the class """
        if isinstance(attrs, list) and all([type(el) is str for el in attrs]):
            return {el: getattr(self, el) for el in attrs if hasattr(self, el)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for key, value in json.items():
            setattr(self, key, value)
