#!/usr/bin/env python3
"""Parameterize a unit test"""
import requests
import unittest
from parameterized import parameterized
from unittest.mock  import patch

access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


class TestAccessNestedMap(unittest.TestCase):
    """UnitTest Class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test method that check assertEqual"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test method that check assertRaises"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Mocks HTTP Calls"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    
    # @patch('utils.get_json')
    # def test_get_json(self, url, mock_get, mock_expected):
        # """Test method for getting JSON"""
        
        # mock_get.return_value = mock_expected

        # test_payload = get_json(url)
        # self.assertEqual(test_payload, mock_expected)
    

    @patch('utils.get_json')
    def test_get_json(self, url, mock_expected, mock_get):
        """Test method for getting JSON"""
        mock_get.return_value = mock_expected

        test_payload = get_json(url)

        self.assertEqual(test_payload, mock_expected)

