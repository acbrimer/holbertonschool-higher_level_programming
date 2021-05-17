#!/usr/bin/python3
"""
   A sample unit test module for string builtins
   Borrowed from:
   https://docs.python.org/3.4/library/unittest.html
"""
import unittest


class TestStringMethods(unittest.TestCase):
    """ Class for TestStringMethods class """

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
