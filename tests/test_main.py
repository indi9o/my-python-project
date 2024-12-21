import unittest
from src.main import get_greeting, get_day_greeting

class TestMain(unittest.TestCase):
    def test_get_greeting(self):
        """
        Test the get_greeting function to ensure it returns a valid greeting message.
        """
        # Test for English language
        greeting = get_greeting("en")
        self.assertIn(greeting, ["Good morning", "Good afternoon", "Good evening"])
        
        # Test for Spanish language
        greeting = get_greeting("es")
        self.assertIn(greeting, ["Buenos días", "Buenas tardes", "Buenas noches"])
        
        # Test for Indonesian language
        greeting = get_greeting("id")
        self.assertIn(greeting, ["Selamat pagi", "Selamat sore", "Selamat malam"])

    def test_get_day_greeting(self):
        """
        Test the get_day_greeting function to ensure it returns a valid day greeting message.
        """
        day_greeting = get_day_greeting()
        self.assertTrue(day_greeting.startswith("Happy"))

if __name__ == "__main__":
    unittest.main()