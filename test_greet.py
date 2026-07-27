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
        self.assertEqual(greet(""), "Hello, !")

    def test_whitespace_name(self):
        """Test greet with a name containing whitespace."""
        self.assertEqual(greet("   "), "Hello,    !")

    


if __name__ == "__main__":
    unittest.main()
