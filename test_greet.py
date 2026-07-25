import unittest
from greet import greet

class TestGreet(unittest.TestCase):
    def test_valid_name(self):
        self.assertEqual(greet("Asina"), "Hello, Asina!")

    def test_empty_string(self):
        self.assertEqual(greet(""), "Hello, !")

if __name__ == "__main__":
    unittest.main()
