class Rooms:
    def __init__(self, name, capacity, costs):
        self.name = name
        self.capacity = capacity
        self.costs = costs
        self.guests_in_room = []

    def add_guests(self, guest):
        self.guests_in_room.append(guest)

    def remove_guests(self,guest):
        self.guests_in_room.pop(guest)
        
    def guests_in_room(self):
        return len(self.guests_in_room)

