class Guests:
    def __init__(self, name, favourite_song, age):
        self.name = name
        self.favourite_song = favourite_song
        self.age = age
        self.total_guests = []

    def measure_total_guests(self):
        return len(self.total_guests)
