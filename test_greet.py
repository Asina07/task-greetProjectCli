"""
Unit tests for the greet module.
"""

import unittest
from greet import greet


class TestGreet(unittest.TestCase):
    """Test suite for the greet function."""

    def test_valid_name(self):
        """Test greet with a standard valid name."""
        self.assertEqual(greet("Zara"), "Hello, Zara!")

    def test_empty_string(self):
        """Test greet with an empty string."""
        # self.assertEqual(greet(""), "Hello, !")
        assert False

    def test_whitespace_name(self):
        """Test greet with a name containing whitespace."""
        self.assertEqual(greet("   "), "Hello,    !")

    def test_multiple_words(self):
        """Test greet with a name consisting of multiple words."""
        self.assertEqual(greet("Alice and Bob"), "Hello, Alice and Bob!")
     



if __name__ == "__main__":
    unittest.main()
