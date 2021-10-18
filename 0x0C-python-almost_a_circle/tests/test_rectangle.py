#!/usr/bin/python3
"""[Implementing Unittest for rectangle]
    """
import unittest
from models.rectangle import Rectangle
from models.base import Base

# Running test by python3 -m unittest discover tests -v


class Test_rectangle(unittest.TestCase):
    """Class for test all the functions of rectangle class"""
    @classmethod
    def setUpClass(cls):
        """ Setting instances of Rectangles once"""
        Base.__nb_objects = 0
        cls.rectangle1 = Rectangle(4, 15)
        cls.rectangle2 = Rectangle(4, 15, 5)
        cls.rectangle3 = Rectangle(4, 15, 5, 7)
        cls.rectangle4 = Rectangle(4, 15, 5, 7, 30)

    def test_width(self):
        """[Testing that the width assignation is rigth]
        """
        self.assertEqual(self.rectangle1.width, 4)
        self.assertEqual(self.rectangle2.width, 4)
        self.assertEqual(self.rectangle3.width, 4)
        self.assertEqual(self.rectangle4.width, 4)

    def test_height(self):
        """[Testing that the height assignation is rigth]
        """
        self.assertEqual(self.rectangle1.height, 15)
        self.assertEqual(self.rectangle2.height, 15)
        self.assertEqual(self.rectangle3.height, 15)
        self.assertEqual(self.rectangle4.height, 15)

    def test_x(self):
        """[Testing that the x assignation is rigth]
        """
        self.assertEqual(self.rectangle1.x, 0)
        self.assertEqual(self.rectangle2.x, 5)
        self.assertEqual(self.rectangle3.x, 5)
        self.assertEqual(self.rectangle4.x, 5)

    def test_y(self):
        """[Testing that the y assignation is rigth]
        """
        self.assertEqual(self.rectangle1.y, 0)
        self.assertEqual(self.rectangle2.y, 0)
        self.assertEqual(self.rectangle3.y, 7)
        self.assertEqual(self.rectangle4.y, 7)

    def test_id(self):
        """[Testing that the id assignation is right, considering Base]
        """
        self.assertEqual(self.rectangle1.id, 1)
        self.assertEqual(self.rectangle2.id, 2)
        self.assertEqual(self.rectangle3.id, 3)
        self.assertEqual(self.rectangle4.id, 30)

    def test_empty_width(self):
        """[Testing Raise type error when width is not setting]
        """
        with self.assertRaises(TypeError) as _:
            Rectangle()

    def test_empty_height(self):
        """[Testing Raise type error when height is not setting]
        """
        with self.assertRaises(TypeError) as _:
            Rectangle(1)
