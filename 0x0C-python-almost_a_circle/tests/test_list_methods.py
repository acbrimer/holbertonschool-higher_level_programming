#!/usr/bin/python3
"""
   A sample unit test module for list builtins
"""
import unittest


class TestListMethods(unittest.TestCase):
    """ Class for TestListMethods class """

    def test_list_equal(self):
        self.assertEqual([1, 2, 3], list({1, 2, 3}))

    def test_isinstance(self):
        self.assertTrue(isinstance([0], list))
        self.assertFalse(isinstance([0], str))
        self.assertNotIsInstance([0], int)

    def test_get_missing_index(self):
        l = [1, 2, 3]
        with self.assertRaises(IndexError):
            print(l[3])

    def test_item_in_list(self):
        l = [1, 2, 3]
        self.assertIn(1, l)
        self.assertNotIn(4, l)

if __name__ == '__main__':
    unittest.main()
