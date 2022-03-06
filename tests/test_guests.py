import unittest
from src.guests import Guests

class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guests = Guests("Cindy", "Lump", 25)

    def test_customer_has_name(self):
        self.assertEqual("Cindy", self.guests.name)
    
    def test_customer_has_favourite_song(self):
        self.assertEqual("Lump", self.guests.favourite_song)

    def test_song_has_age(self):
        self.assertEqual(25, self.guests.age)