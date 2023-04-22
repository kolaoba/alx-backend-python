#!/usr/bin/env python3
"""Test Access Nested Map Fn"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Defines TestAccessNestedMap Class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        assert access_nested_map(nested_map, path) == expected

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Defines TestGetJson Class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @unittest.mock.patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_get.return_value = unittest.mock.Mock()
        mock_get.return_value.json.return_value = test_payload
        response = get_json(test_url)
        assert response == test_payload
