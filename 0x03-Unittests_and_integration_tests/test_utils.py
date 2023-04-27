#!/usr/bin/env python3
"""Test Access Nested Map Fn"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest import mock


class TestAccessNestedMap(unittest.TestCase):
    """Defines TestAccessNestedMap Class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

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
    def test_get_json(self, test_url, test_payload):
        with mock.patch("requests.get") as get_data:
            res = mock.Mock()
            res.json.return_value = test_payload
            get_data.return_value = res
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Defines TestMemoize class"""

    def test_memoize(self):
        """test memoize function"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, "a_method",
                               return_value=lambda: 42) as func:
            test_obj = TestClass()
            self.assertEqual(test_obj.a_property(), 42)
            self.assertEqual(test_obj.a_property(), 42)
            func.assert_called_once()
