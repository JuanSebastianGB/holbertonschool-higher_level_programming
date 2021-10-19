#!/usr/bin/python3
"""[Implementing Unittest for base]
"""
from unittest.case import TestCase
from models import base
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
        """[Testing, trying to get a private atrubute]
        """
        msj = "'Base' object has no attribute '_Test_base__nb_objects'"
        with self.assertRaisesRegex(AttributeError, msj) as _:
            print(Base().__nb_objects)
        msj = "'Base' object has no attribute 'nb_objects'"
        with self.assertRaisesRegex(AttributeError, msj) as _:
            print(Base().nb_objects)
