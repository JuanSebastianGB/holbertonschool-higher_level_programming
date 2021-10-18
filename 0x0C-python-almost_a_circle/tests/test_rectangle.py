#!/usr/bin/python3
"""[Implementing Unittest for rectangle]
    - Test setting form line ...
    - Test Types from line ...
    """
from typing import Type
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

    def test_width_wrong_type(self):
        """[Testing Cases Width is not an integer, it must return the msj too]
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer") as _:
            Rectangle("1", 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer") as _:
            Rectangle(1.8, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer") as _:
            Rectangle([], 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer") as _:
            Rectangle((1,), 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer") as _:
            Rectangle(True, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer") as _:
            Rectangle({"1": "test"}, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer") as _:
            Rectangle({1, 2, 3}, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer") as _:
            Rectangle(complex(100), 5)

    def test_height_wrong_type(self):
        """[Testing Cases Width is not an integer, it must return the msj too]
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer") as _:
            Rectangle(5, "1")
        with self.assertRaisesRegex(TypeError, "height must be an integer") as _:
            Rectangle(5, 1.8)
        with self.assertRaisesRegex(TypeError, "height must be an integer") as _:
            Rectangle(5, [])
        with self.assertRaisesRegex(TypeError, "height must be an integer") as _:
            Rectangle(5, (1,))
        with self.assertRaisesRegex(TypeError, "height must be an integer") as _:
            Rectangle(5, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer") as _:
            Rectangle(5, {"1": "test"})
        with self.assertRaisesRegex(TypeError, "height must be an integer") as _:
            Rectangle(5, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "height must be an integer") as _:
            Rectangle(5, complex(100))

    def test_x_wrong_type(self):
        """[Testing Cases x is not an integer, it must return the msj too]
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer") as _:
            Rectangle(5, 10, "1")
        with self.assertRaisesRegex(TypeError, "x must be an integer") as _:
            Rectangle(5, 10, 1.8)
        with self.assertRaisesRegex(TypeError, "x must be an integer") as _:
            Rectangle(5, 10, [])
        with self.assertRaisesRegex(TypeError, "x must be an integer") as _:
            Rectangle(5, 10, (1,))
        with self.assertRaisesRegex(TypeError, "x must be an integer") as _:
            Rectangle(5, 10, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer") as _:
            Rectangle(5, 10, {"1": "test"})
        with self.assertRaisesRegex(TypeError, "x must be an integer") as _:
            Rectangle(5, 10, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "x must be an integer") as _:
            Rectangle(5, 10, complex(100))

    def test_y_wrong_type(self):
        """[Testing Cases y is not an integer, it must return the msj too]
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer") as _:
            Rectangle(5, 10, 15, "1")
        with self.assertRaisesRegex(TypeError, "y must be an integer") as _:
            Rectangle(5, 10, 15, 1.8)
        with self.assertRaisesRegex(TypeError, "y must be an integer") as _:
            Rectangle(5, 10, 15, [])
        with self.assertRaisesRegex(TypeError, "y must be an integer") as _:
            Rectangle(5, 10, 15, (1,))
        with self.assertRaisesRegex(TypeError, "y must be an integer") as _:
            Rectangle(5, 10, 15, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer") as _:
            Rectangle(5, 10, 15, {"1": "test"})
        with self.assertRaisesRegex(TypeError, "y must be an integer") as _:
            Rectangle(5, 10, 15, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "y must be an integer") as _:
            Rectangle(5, 10, 15, complex(100))

    def test_width_wrong_value(self):
        """[Testing case width wrong value]
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0") as _:
            Rectangle(-10, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0") as _:
            Rectangle(0, 2, 3, 4, 5)

    def test_height_wrong_value(self):
        """[Testing case height wrong value]
        """
        with self.assertRaisesRegex(ValueError, "height must be > 0") as _:
            Rectangle(1, -2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0") as _:
            Rectangle(1, 0, 3, 4, 5)

    def test_x_wrong_value(self):
        """[Testing case x wrong value]
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0") as _:
            Rectangle(1, 2, -3, 4, 5)

    def test_y_wrong_value(self):
        """[Testing case y wrong value]
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0") as _:
            Rectangle(1, 2, 3, -4, 5)

    def test_area_value(self):
        """[Testing the result of method area of gived rectangles]
        """
        self.assertEqual(self.rectangle1.area(), 4*15)
        self.assertEqual(self.rectangle2.area(), 4*15)
        self.assertEqual(self.rectangle3.area(), 4*15)
        self.assertEqual(self.rectangle4.area(), 4*15)
