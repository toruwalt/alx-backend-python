#!/usr/bin/env python3
"""Parameterize a unit test"""
"""Create a TestAccessNestedMap class that inherits from unittest.TestCase."""
import unittest 
from parameterized import parameterized

access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    
    def test_access_nested_map(self, nested_map, expected):
        self.assertEqual(access_nested_map(nested_map), expected)
    
    
        