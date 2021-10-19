#!/usr/bin/python3
"""[Implementing Unittest for base]
"""
from unittest.case import TestCase
from models import base
import json
Base = base.Base


class Test_base(TestCase):
    """[Class for test all the functions of base class]
    """

    def test_empty_base(self):
        """[Testing empty base(), that must return by id]
        """
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_1_argument_base(self):
        """[Testing 1 argument base(), that must set the corresponding id]
        """
        obj = Base(15)
        self.assertEqual(obj.id, 15)

    def test_tm_arguments(self):
        """[Testing too many arguments in Base]
        """
        with self.assertRaises(TypeError) as _:
            Base(1, 2, 3)

    def test_private(self):
        """[Testing, trying to get a private atribute]
        """
        msj = "'Base' object has no attribute '_Test_base__nb_objects'"
        with self.assertRaisesRegex(AttributeError, msj) as _:
            print(Base().__nb_objects)
        msj = "'Base' object has no attribute 'nb_objects'"
        with self.assertRaisesRegex(AttributeError, msj) as _:
            print(Base().nb_objects)

    def test_to_json_string(self):
        """[Testing to_json_string]
        """
        r1 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        r2 = {"id": 10, "width": 20, "height": 30, "x": 40, "y": 50}
        output = Base.to_json_string([r1, r2])
        self.assertEqual(json.loads(output), [r1, r2])
        self.assertEqual(type(output), str)

    def test_tf_none_arguments_to_json_string(self):
        """[Testing cases None and [] like inputs]
        """
        self.assertEqual(type(Base.to_json_string([])), str)
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(type(Base.to_json_string(None)), str)
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        """[Testing Output of from_json_string]
        """
        json_string = '[{"height": 4, "width": 10, "id": 89},\
        {"height": 7, "width": 1, "id": 20}]'
        objects_json = Base.from_json_string(json_string)
        self.assertEqual(len(objects_json), 2)
        self.assertEqual(type(objects_json), list)
        self.assertEqual(all([type(el) is dict for el in objects_json]), True)
        self.assertEqual(objects_json[0], {"height": 4, "width": 10, "id": 89})
        self.assertEqual(objects_json[1], {"height": 7, "width": 1, "id": 20})

    def test_tf_none_arguments_from_json_string(self):
        """[Testing empty or none inputs for the function from_json_string]
        """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
