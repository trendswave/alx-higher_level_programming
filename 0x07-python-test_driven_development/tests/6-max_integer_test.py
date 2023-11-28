#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    ''' Unit cases for max_integer '''
    def test_empty(self):
        self.assertIs(max_integer(), None)

    def test_negative_list(self):
        self.assertIs(max_integer([-2, -4, -1]), -1)

    def test_max_normal(self):
        self.assertIs(max_integer([4, 5, 10, 50, 60]), 60)

    def test_max_normal2(self):
        self.assertIs(max_integer([100, 5, 10, 50, 60]), 100)

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string_argument(self):
        self.assertIs(max_integer('Holberton School'), 't')

    def test_list_string(self):
        with self.assertRaises(TypeError):
            max_integer(["Hello holberton", 12])

    def test_one_element(self):
        self.assertIs(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
