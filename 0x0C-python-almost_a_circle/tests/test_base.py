#!/usr/bin/python3
"""
    Unit test module for Base class 
"""
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """ Class for Base class """

    def test_defined_id(self):
        b1 = Base(100)
        self.assertEqual(b1.id, 100)

    def test_autoincriment_id(self):
        b2 = Base()
        self.assertEqual(b2.id, 1)

if __name__ == '__main__':
    unittest.main()
