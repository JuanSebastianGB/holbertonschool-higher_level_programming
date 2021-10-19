#!/usr/bin/python3
"""[Implementing Unittest for rectangle]
    """
from logging import raiseExceptions
from typing import Type
import unittest
from models.rectangle import Rectangle
from models.base import Base
import contextlib
import io

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
        self.assertEqual(self.rectangle4.id, 30)

    def test_empty_width(self):
        """[Testing Raise type error when width is not setting]
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_empty_height(self):
        """[Testing Raise type error when height is not setting]
        """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width_wrong_type(self):
        """[Testing Cases Width is not an integer, it must return the msj too]
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.8, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([], 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1,), 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"1": "test"}, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(100), 5)

    def test_height_wrong_type(self):
        """[Testing Cases Width is not an integer, it must return the msj too]
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, "1")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 1.8)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, [])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, (1,))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {"1": "test"})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, complex(100))

    def test_x_wrong_type(self):
        """[Testing Cases x is not an integer, it must return the msj too]
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, "1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, 1.8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, [])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, (1,))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, {"1": "test"})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, complex(100))

    def test_y_wrong_type(self):
        """[Testing Cases y is not an integer, it must return the msj too]
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 15, "1")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 15, 1.8)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 15, [])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 15, (1,))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 15, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 15, {"1": "test"})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 15, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 15, complex(100))

    def test_width_wrong_value(self):
        """[Testing case width wrong value]
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2, 3, 4, 5)

    def test_height_wrong_value(self):
        """[Testing case height wrong value]
        """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0, 3, 4, 5)

    def test_x_wrong_value(self):
        """[Testing case x wrong value]
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3, 4, 5)

    def test_y_wrong_value(self):
        """[Testing case y wrong value]
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4, 5)

    def test_area_value(self):
        """[Testing the result of method area of gived rectangles]
        """
        self.assertEqual(self.rectangle1.area(), 4*15)
        self.assertEqual(self.rectangle2.area(), 4*15)
        self.assertEqual(self.rectangle3.area(), 4*15)
        self.assertEqual(self.rectangle4.area(), 4*15)

    def test_area_arguments(self):
        """[Testing when too many arguments are gived to area function]
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4).area(5, 2, 3)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4).area(5, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4).area(5)

    def test_display_output(self):
        """[Testing the displaying output of the function display, by catching
        into a variable using 'with' with io and contextlib modules]
        """
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            self.rectangle1.display()
            catched = output.getvalue()
        self.assertEqual(
            catched, "\n" * self.rectangle1.y +
            (" " * self.rectangle1.x + "#" * self.rectangle1.width + "\n")
            * self.rectangle1.height)
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            self.rectangle2.display()
            catched = output.getvalue()
        self.assertEqual(
            catched, "\n" * self.rectangle2.y +
            (" " * self.rectangle2.x + "#" * self.rectangle2.width + "\n")
            * self.rectangle2.height)
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            self.rectangle3.display()
            catched = output.getvalue()
        self.assertEqual(
            catched, "\n" * self.rectangle3.y +
            (" " * self.rectangle3.x + "#" * self.rectangle3.width + "\n")
            * self.rectangle2.height)
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            self.rectangle4.display()
            catched = output.getvalue()
        self.assertEqual(
            catched, "\n" * self.rectangle4.y +
            (" " * self.rectangle4.x + "#" * self.rectangle4.width + "\n")
            * self.rectangle4.height)

    def test_display_arguments(self):
        """[Testing when too many arguments are gived to display function]
        """
        with self.assertRaises(TypeError):
            self.rectangle1.display(5, 4, 3, 2)
        with self.assertRaises(TypeError):
            self.rectangle2.display(5, 4, 3)
        with self.assertRaises(TypeError):
            self.rectangle3.display(5, 4)
        with self.assertRaises(TypeError):
            self.rectangle4.display(5)

    def test_print_right_output(self):
        """[Testing case __str__ output of the rectangle]
        """
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            print(self.rectangle4)
            catched = output.getvalue()
        self.assertEqual(
            catched, f"[Rectangle] ({30:d}) {5:d}/{7:d} - {4:d}/{15:d}\n")

    def test_str_right_output(self):
        """[Testing str transformation of Rectangle]
        """
        self.assertEqual(str(self.rectangle4), "[Rectangle] (30) 5/7 - 4/15")

    def test_update_by_args(self):
        """[Testing update rectangle by args]
        """
        rectangle = Rectangle(10, 20)
        rectangle.update(10)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 0/0 - 10/20")
        rectangle.update(10, 20)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 0/0 - 20/20")
        rectangle.update(10, 20, 30)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 0/0 - 20/30")
        rectangle.update(10, 20, 30, 40)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 40/0 - 20/30")
        rectangle.update(10, 20, 30, 40, 50)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 40/50 - 20/30")

    def test_tm_args(self):
        """[Testing when are gived more than 5 values to the update function]
        """
        rectangle = Rectangle(1, 2)
        rectangle.update(1, 2, 3, 4, 5, 6)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 4/5 - 2/3")

    def test_tf_args(self):
        """[Testing when are not gived arguments, that does not
        modify anything]
        """
        rectangle = Rectangle(5, 8, 15, 25, 1)
        rectangle.update()
        self.assertEqual(str(rectangle), "[Rectangle] (1) 15/25 - 5/8")

    def test_wrong_types_updating(self):
        """[Testing that types when updating are right]
        """
        rectangle = Rectangle(100, 2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(100, "2", 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(100, 2.5, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(100, [], 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(100, {}, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(100, (1,), 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(100, {"1": "hellow"}, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(100, 2, "2", 2, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(100, 2, 2.5, 2, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(100, 2, [], 2, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(100, 2, {}, 2, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(100, 2, (1,), 2, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(100, 2, {"1": "hellow"}, 2, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.update(100, 2, 2, "2", 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.update(100, 2, 2, 2.5, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.update(100, 2, 2, [], 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.update(100, 2, 2, {}, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.update(100, 2, 2, (1,), 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.update(100, 2, 2, {"1": "hellow"}, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rectangle.update(100, 2, 2, 2, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rectangle.update(100, 2, 2, 2, 2.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rectangle.update(100, 2, 2, 2, [])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rectangle.update(100, 2, 2, 2, {})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rectangle.update(100, 2, 2, 2, (1,))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rectangle.update(100, 2, 2, 2, {"1": "hellow"})

    def test_wrong_values_updating(self):
        """[Testing that value numbers are right using update function]
        """
        rectangle = Rectangle(1, 1, 1, 1, 101)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.update(101, -100)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.update(101, 100, -100)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rectangle.update(101, 100, 100, -100)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rectangle.update(101, 100, 100, 100, -100)
