class Person:
    def __init__(self, mass, destination, floor):
        self.mass = mass
        self.destination = destination
        self.base_floor = floor

        # Arrival time, pickup time and destination time will be added in to measure avg trip times soon
        #self.arrival_time = arrival_time
        #self.pickup_time = pickup_time
        #self.destination_time = destination_time

class Floor:
    def __init__(self, number, height):
        self.number = number
        self.height = height
        self.q = []
    
    def add_person(self, person):
        self.q.append(person)

    def waiting_tally(self):
        print(f'In floor {self.number} there are {len(self.q)} people waiting')