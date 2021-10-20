#!/usr/bin/python3

"""[Module of the class Base]

    Returns:
        [Class]: [Parent class to almost a circle project]
    """
import json
import csv


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
        dicts = []
        if list_objs is not None:
            dicts = [el.to_dictionary() for el in list_objs]
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            f.write(cls.to_json_string(dicts))

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file with
        json string representation"""
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in csv"""
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, mode="w", encoding="utf-8", newline="") as csv_f:
            csv_obj = csv.writer(csv_f)
            if cls.__name__ == "Rectangle":
                [csv_obj.writerow([obj.id, obj.width, obj.height,
                                  obj.x, obj.y]) for obj in list_objs]
            elif cls.__name__ == "Square":
                [csv_obj.writerow([obj.id, obj.size,
                                  obj.x, obj.y]) for obj in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in csv"""
        file_name = "{}.csv".format(cls.__name__)
        try:
            with open(file_name, mode="r", encoding="utf-8", newline="")\
                    as csv_f:
                csv_obj = csv.reader(csv_f)
                if cls.__name__ == "Rectangle":
                    destiny = ['id', 'width', 'height', 'x', 'y']
                    return [(cls.create(**{destiny[index]: int(el) for index,
                                        el in enumerate(row)}))
                            for row in csv_obj]
                elif cls.__name__ == "Square":
                    destiny = ['id', 'size', 'x', 'y']
                    return [(cls.create(**{destiny[index]: int(el) for index,
                                        el in enumerate(row)}))
                            for row in csv_obj]
        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        pass
