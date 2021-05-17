#!/usr/bin/python3
"""
    Unit test module for Rectangle class 
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """ Class for Rectangle class """

    def test_5_x_5(self):
        r1 = Rectangle(5, 5)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_5_x_5_id(self):
        r1 = Rectangle(5, 5, 0, 0, 5)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

if __name__ == '__main__':
    unittest.main()
