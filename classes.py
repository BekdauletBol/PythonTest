class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_pass(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(2)
people = ["Bekdaulet", "Yernazar","Dimash", "Marat"]
for person in people:
    if     flight.add_pass(person):
        print(f"Successfuly added {person}!")
    else:
        print(f"No available seats for {person} =(")
