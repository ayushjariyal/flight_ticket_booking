class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def add_passangers(self, name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passangers)
    
flight = Flight(3)

people = ["Harry", "Hermione", "Ron", "Draco"]

for person in people:
    succes = flight.add_passangers(people)
    if succes:
        print(f"{person} added successfully")

    else:
        print(f"No available seats for {person}")