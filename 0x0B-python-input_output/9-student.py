#!/usr/bin/python3
"""" Module that contain class Student """


class Student:
    """[ Defining student]
    """

    def __init__(self, first_name, last_name, age) -> None:
        """ Creating a student  """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return the json representation of the class """
        return self.__dict__
