#!/usr/bin/python3

""" Implementing Unittests for max integer in a list max_integer([...])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Define unittest for max_integer() function"""

    def test_unsorted_list(self):
        """ Testing an unsorted list of integers """
        self.assertEqual(max_integer([4, 7, 8, 1]), 8)

    def test_sorted_list(self):
        """ Testing a sorted list of integers """
        self.assertEqual(max_integer([4, 7, 8, 10]), 10)

    def test_at_the_start(self):
        """ Testing max integer at the start """
        self.assertEqual(max_integer([40, 7, 8, 10]), 40)

    def test_at_the_middle(self):
        """ Testing max integer at the middle """
        self.assertEqual(max_integer([40, 7, 80, 10, 30]), 80)

    def test_with_negatives(self):
        """ Testing max integer from negatives """
        self.assertEqual(max_integer([-40, -7, -80, -10, 30]), 30)

    def test_empty_list(self):
        """ Testing an empty list """
        self.assertEqual(max_integer([]), None)

    def test_None(self):
        """ Testing None input """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_empty_string(self):
        """ Testing an empty string """
        self.assertEqual(max_integer(""), None)

    def test_asci_list(self):
        """ Testing an Ascci input (string) """
        self.assertEqual(max_integer("ABCZ"), 'Z')

    def test_strings_list(self):
        """ Testing list of strings input """
        self.assertEqual(max_integer(["one", "two", "three"]), 'two')

    def test_floats_list(self):
        """ Testing list of floats inputs """
        self.assertEqual(max_integer([10.50, 100.45, -85.5]), 100.45)

    def test_combine_numbers_list(self):
        """ Testing list of floats and integers inputs """
        self.assertEqual(max_integer([10.50, 100.45, -85.5, 500]), 500)

    def test_unique_integer(self):
        """ Testing one single element in the list """
        self.assertEqual(max_integer([1000]), 1000)

    def test_not_input(self):
        """ Testing if not input is gived """
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
