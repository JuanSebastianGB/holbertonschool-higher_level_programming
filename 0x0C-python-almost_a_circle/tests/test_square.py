#!/usr/bin/python3
"""[Implementing Unittest for square]
    - Test setting form line ...
    - Test Types from line ...
    """
from logging import raiseExceptions
from typing import Type
import unittest
from models.square import Square
from models.base import Base
import contextlib
import io

# Running test by python3 -m unittest discover tests -v


class Test_square(unittest.TestCase):
    """Class for test all the functions of square class"""
    @classmethod
    def setUpClass(cls):
        """ Setting instances of Rectangles once"""
        Base.__nb_objects = 0
        cls.square1 = Square(4)
        cls.square2 = Square(4, 15)
        cls.square3 = Square(4, 15, 5)
        cls.square4 = Square(4, 15, 5, 7)

    def test_size(self):
        """[Testing that the size assignation is rigth]
        """
        self.assertEqual(self.square1.size, 4)
        self.assertEqual(self.square2.size, 4)
        self.assertEqual(self.square3.size, 4)
        self.assertEqual(self.square4.size, 4)

    def test_x(self):
        """[Testing that the x assignation is rigth]
        """
        self.assertEqual(self.square1.x, 0)
        self.assertEqual(self.square2.x, 15)
        self.assertEqual(self.square3.x, 15)
        self.assertEqual(self.square4.x, 15)

    def test_y(self):
        """[Testing that the y assignation is rigth]
        """
        self.assertEqual(self.square1.y, 0)
        self.assertEqual(self.square2.y, 0)
        self.assertEqual(self.square3.y, 5)
        self.assertEqual(self.square4.y, 5)

    def test_id(self):
        """[Testing that the id assignation is right, considering Base]
        """
        self.assertEqual(self.square4.id, 7)

    def test_empty_size(self):
        """[Testing Raise type error when width is not setting]
        """
        with self.assertRaises(TypeError):
            Square()

    def test_size_wrong_type(self):
        """[Testing Cases Width is not an integer, it must return the msj too]
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1,))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"1": "test"})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(100))

    def test_x_wrong_type(self):
        """[Testing Cases x is not an integer, it must return the msj too]
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, 1.8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, [])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, (1,))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {"1": "test"})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, complex(100))

    def test_y_wrong_type(self):
        """[Testing Cases y is not an integer, it must return the msj too]
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 10, "1")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 10, 1.8)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 10, [])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 10, (1,))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 10, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 10, {"1": "test"})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 10, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 10, complex(100))

    def test_size_wrong_value(self):
        """[Testing case width wrong value]
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2, 3, 4)

    def test_x_wrong_value(self):
        """[Testing case x wrong value]
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -3, 4, 5)

    def test_y_wrong_value(self):
        """[Testing case y wrong value]
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 3, -4, 5)

    def test_area_value(self):
        """[Testing the result of method area of gived sqaureas]
        """
        self.assertEqual(self.square1.area(), 4**2)
        self.assertEqual(self.square2.area(), 4**2)
        self.assertEqual(self.square3.area(), 4**2)
        self.assertEqual(self.square4.area(), 4**2)

    def test_area_arguments(self):
        """[Testing when too many arguments are gived to area function]
        """
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4).area(5, 2, 3)
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4).area(5, 2)
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4).area(5)

    def test_display_output(self):
        """[Testing the displaying output of the function display, by catching
        into a variable using 'with' with io and contextlib modules]
        """
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            self.square1.display()
            catched = output.getvalue()
        self.assertEqual(
            catched, "\n" * self.square1.y +
            (" " * self.square1.x + "#" * self.square1.size + "\n")
            * self.square1.size)
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            self.square2.display()
            catched = output.getvalue()
        self.assertEqual(
            catched, "\n" * self.square2.y +
            (" " * self.square2.x + "#" * self.square2.size + "\n")
            * self.square2.size)
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            self.square3.display()
            catched = output.getvalue()
        self.assertEqual(
            catched, "\n" * self.square3.y +
            (" " * self.square3.x + "#" * self.square3.size + "\n")
            * self.square2.size)
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            self.square4.display()
            catched = output.getvalue()
        self.assertEqual(
            catched, "\n" * self.square4.y +
            (" " * self.square4.x + "#" * self.square4.size + "\n")
            * self.square4.size)

    def test_display_arguments(self):
        """[Testing when too many arguments are gived to display function]
        """
        with self.assertRaises(TypeError):
            self.square1.display(5, 4, 3, 2)
        with self.assertRaises(TypeError):
            self.square2.display(5, 4, 3)
        with self.assertRaises(TypeError):
            self.square3.display(5, 4)
        with self.assertRaises(TypeError):
            self.square4.display(5)

    def test_print_right_output(self):
        """[Testing case __str__ output of the square]
        """
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            print(self.square4)
            catched = output.getvalue()
        self.assertEqual(
            catched, "[Square] (7) 15/5 - 4\n")

    def test_str_right_output(self):
        """[Testing str transformation of Square]
        """
        self.assertEqual(str(self.square4), "[Square] (7) 15/5 - 4")

    def test_update_by_args(self):
        """[Testing update square by args]
        """
        square = Square(10)
        square.update(10)
        self.assertEqual(str(square), "[Square] (10) 0/0 - 10")
        square.update(10, 20)
        self.assertEqual(str(square), "[Square] (10) 0/0 - 20")
        square.update(10, 20, 30)
        self.assertEqual(str(square), "[Square] (10) 30/0 - 20")
        square.update(10, 20, 30, 40)
        self.assertEqual(str(square), "[Square] (10) 30/40 - 20")

    def test_tm_args(self):
        """[Testing when are gived more than 4 values to the update function]
        """
        square = Square(1)
        square.update(1, 2, 3, 4, 5, 6)
        self.assertEqual(str(square), "[Square] (1) 3/4 - 2")

    def test_tf_args(self):
        """[Testing when are not gived arguments, that does not
        modify anything]
        """
        square = Square(5, 8, 15, 250)
        square.update()
        self.assertEqual(str(square), "[Square] (250) 8/15 - 5")

    def test_wrong_types_updating(self):
        """[Testing that types when updating are right]
        """
        square = Square(100, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(100, "2", 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(100, 2.5, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(100, [], 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(100, {}, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(100, (1,), 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(100, {"1": "hellow"}, 2, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(100, 2, "2", 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(100, 2, 2.5, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(100, 2, [], 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(100, 2, {}, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(100, 2, (1,), 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(100, 2, {"1": "hellow"}, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(100, 2, 2, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(100, 2, 2, 2.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(100, 2, 2, [])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(100, 2, 2, {})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(100, 2, 2, (1,))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(100, 2, 2, {"1": "hellow"})

    def test_wrong_values_updating(self):
        """[Testing that value numbers are right using update function]
        """
        square = Square(1, 1, 1, 101)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(101, -100)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(101, 100, -100)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(101, 100, 100, -100)
