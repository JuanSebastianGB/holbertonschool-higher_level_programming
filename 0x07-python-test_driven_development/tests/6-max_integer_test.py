#!/usr/bin/python3

""" Implementing Unittests for max integer in a list max_integer([......])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_unsorted_list(self):
        """ Testing an unsorted list of integers """
        self.assertEqual(max_integer([4, 7, 8, 1]), 8)


if __name__ == '__main__':
    unittest.main()
