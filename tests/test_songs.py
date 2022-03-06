import unittest
from src.songs import Songs

class TestSongs(unittest.TestCase):
    def setUp(self):
        self.songs = Songs("Lump", 3)