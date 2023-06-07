#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([9, 5, 1, 8]), 9)
    
    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
    
    def test_negative_numbers(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)
        self.assertEqual(max_integer([-9, -5, -1, -8]), -1)
    
    def test_duplicate_numbers(self):
        """Test with a list containing duplicate numbers"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
    
    def test_single_element_list(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([100]), 100)
        self.assertEqual(max_integer([-50]), -50)

if __name__ == '__main__':
    unittest.main()