import unittest
from src.main import get_greeting, get_day_greeting

class TestMain(unittest.TestCase):
    def test_get_greeting(self):
        """
        Test the get_greeting function to ensure it returns a valid greeting message.
        """
        greeting = get_greeting()
        self.assertIn(greeting, ["Good morning", "Good afternoon", "Good evening"])
    def test_get_day_greeting(self):
        """
        Test the get_day_greeting function to ensure it returns a valid day greeting message.
        """
        day_greeting = get_day_greeting()
        self.assertTrue(day_greeting.startswith("Happy"))

if __name__ == "__main__":
    unittest.main()