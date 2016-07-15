"""Unit tests"""
import unittest
import other_dependency.depmodule

class TestModule(unittest.TestCase):
    def test_something(self):
        self.assertEqual(other_dependency.depmodule.function(), 1)

