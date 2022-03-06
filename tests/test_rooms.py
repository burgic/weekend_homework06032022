import unittest
from src.guests import Guests
from src.rooms import Rooms

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.rooms = Rooms("Atomic", 10, 15)

    def test_room_has_name(self):
        self.assertEqual("Atomic", self.rooms.name)
    
    def test_guest_added_to_room(self):
        guest = Guests("Doris", "Tell Me Why", 25)
        self.rooms.add_guests(guest)
        range = self.rooms.guests_in_room()
        self.assertEqual(1, range)