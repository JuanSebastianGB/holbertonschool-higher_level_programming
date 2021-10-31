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
import json
import pycodestyle

# Running test by python3 -m unittest discover tests -v


class Test_style(unittest.TestCase):
    """[ Class for testing some stuff related with style and syntax]
    """

    def test_pycode(self):
        foo = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/square.py'])
        self.assertEqual(foo.total_errors, 0,
                         "Found code style error (and warnings).")


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
        self.assertEqual(Square(id=400, size=3).area(), 3**2)

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
        square = Square(5, 5, 5, 169)
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            square.display()
            catched = output.getvalue()
        self.assertEqual(catched, "\n" * 5 + (" " * 5 + "#" * 5 + "\n") * 5)
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
            * self.square3.size)
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
        self.assertEqual(str(Square(5, 10, 15, 200)),
                         "[Square] (200) 10/15 - 5")
        self.assertEqual(str(Square(20, 20)),
                         "[Square] (28) 20/0 - 20")
        self.assertEqual(str(Square(20, 20, 20)),
                         "[Square] (29) 20/20 - 20")

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

    def test_update_kwargs(self):
        """[Testing update by sending kwargs]
        """
        square = Square(5, 5, 5, 1)
        square.update(id=5)
        self.assertEqual(str(square), "[Square] (5) 5/5 - 5")
        square.update(y=50)
        self.assertEqual(str(square), "[Square] (5) 5/50 - 5")
        square.update(x=150)
        self.assertEqual(str(square), "[Square] (5) 150/50 - 5")
        square.update(size=200)
        self.assertEqual(str(square), "[Square] (5) 150/50 - 200")
        square.update(size=300, x=78, id=32)
        self.assertEqual(str(square), "[Square] (32) 78/50 - 300")
        square = Square(1, 1, 1, 1)
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            square.update(size=20, id=400)
            print(square)
            catched = output.getvalue()
        self.assertEqual(catched, "[Square] (400) 1/1 - 20\n")

    def test_wrong_types_updating_kwargs(self):
        """[Testing wrong types updating kwargs]
        """
        square = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(size="98")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(size=10.5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(size=[])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(size={})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(size=(1,))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(x="98")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(x=10.5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(x=[])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(x={})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(x=(1,))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(y="98")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(y=10.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(y=[])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(y={})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(y=(1,))

    def test_wrong_values_updating_kwargs(self):
        """[Testing wrong values updating kwargs]
        """
        square = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(size=-5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(x=-5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(y=-5)

    def test_new_atribute_kwargs(self):
        """[Testing if is inserted a non exitent key when updating with kwargs]
        """
        square = Square(1, 1, 1, 1)
        square.update(new_one=27)
        self.assertEqual(str(square), "[Square] (1) 1/1 - 1")

    def test_mix_update(self):
        """[Testing mixing args and kwargs in update]
        """
        square = Square(1, 1, 1, 1)
        square.update(10, 20, 30, 40, new_one=50, id=1000)
        self.assertEqual(str(square), "[Square] (10) 30/40 - 20")

    def test_to_dictionary(self):
        """[Testing the output of to_dictionary function]
        """
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.to_dictionary(),
                         {'id': 4, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(type(square.to_dictionary()), dict)
        self.assertTrue(type(square.to_dictionary()) is dict)
        square2 = Square(1, 1, 1, 1)
        square2.update(**square.to_dictionary())
        self.assertEqual(str(square), str(square2))
        self.assertNotEqual(square, square2)

    def test_tm_args_to_dictionary(self):
        """[Testing if are passed functions to to_dictionary]
        """
        square = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError) as _:
            square.to_dictionary(1, 2, 3)

    def test_save_to_file(self):
        """[Testing function save_to_file]
        """
        squares = [Square(i, i, i, i) for i in range(1, 10)]
        Square.save_to_file(squares)
        with open("Square.json", "r") as f:
            ls = [el.to_dictionary() for el in squares]
            self.assertEqual(json.dumps(ls), f.read())

    def test_save_to_file_empty(self):
        """[Testing the json string output in '[]' when are gived
        a '[]']
        """
        Square.save_to_file([])
        with open("Square.json", mode="r", encoding="utf-8") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_none(self):
        """[Testing the json string output in '[]' when are gived
        a None]
        """
        Square.save_to_file(None)
        with open("Square.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

    def test_no_args_save_to_file(self):
        """[Testing when save_to_file has not arguments]
        """
        with self.assertRaises(TypeError) as _:
            Square.save_to_file()

    def test_for_create(self):
        """[Testing output for create function]
        """
        first = {"id": 1, "size": 3, "x": 4, "y": 5}
        second = {"id": 10, "size": 30, "x": 40, "y": 50}
        square = Square.create(**first)
        square1 = Square.create(**second)
        self.assertEqual(str(square), "[Square] (1) 4/5 - 3")
        self.assertEqual(str(square1), "[Square] (10) 40/50 - 30")
        self.assertIsNot(first, square)
        self.assertIsNot(second, square1)
        self.assertNotEqual(first, square)
        self.assertNotEqual(second, square1)

    def test_create_empty(self):
        """[Testing case create without arguments]
        """
        with self.assertRaises(TypeError) as _:
            Square().create()

    def test_load_from_file(self):
        """[Testing load_to_file(), by checkink different outputs]
        """
        squares = [Square(i, i, i, i) for i in range(1, 15)]
        Square.save_to_file(squares)
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 14)
        self.assertEqual(type(loaded), list)
        self.assertTrue(all([type(el) is Square for el in loaded]))
        [self.assertEqual(str(squares[index]), str(loaded[index]))
         for index, el in enumerate(squares)]
        [self.assertIsNot(squares[index], loaded[index])
         for index, el in enumerate(squares)]
        [self.assertNotEqual(squares[index], loaded[index])
         for index, el in enumerate(squares)]

    def test_tf_arguments_lff(self):
        """[Testing case when nor argument is gived to load_from_file function]
        """
        from os import remove

        file_name = "Square.json"
        try:
            remove(file_name)
        except Exception as e:
            pass
        with open(file_name, mode="a", encoding="utf-8") as f:
            self.assertEqual(Square.load_from_file(), [])

    def test_tf_arguments_lff_nf(self):
        """[Testing case when nor argument is gived to load_from_file function]
        """
        from os import remove

        file_name = "Square.json"
        try:
            remove(file_name)
        except Exception as e:
            pass
        self.assertEqual(Square.load_from_file(), [])
