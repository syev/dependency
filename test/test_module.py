"""Unit tests"""
import unittest
import dependency.depmodule

class TestModule(unittest.TestCase):
    def test_something(self):
        self.assertEqual(dependency.depmodule.function(), 0)

