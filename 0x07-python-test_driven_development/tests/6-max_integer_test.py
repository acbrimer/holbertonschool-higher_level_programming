#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Test class for max_integer """
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
    
    def test_max_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([1,3,5,4,3]), 5)

    def test_max_list_empty(self):
        self.assertIsNone(max_integer([]))

    def test_max_list_single(self):
        self.assertEqual(max_integer([1]), 1)

    def test_max_not_list(self):
        with self.assertRaises(TypeError):
           max_integer(2)

if __name__ == '__main__':
    unittest.main()
