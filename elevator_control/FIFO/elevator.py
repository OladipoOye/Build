# from person_and_floor import Person, Floor

class Elevator:
    def __init__(self, total_mass, counter_balance, capacity=10, floors=[], number=0, day_time="morning"):
        self.number = number
        self.total_mass = total_mass
        self.counter_balance_mass = counter_balance
        self.passengers = []
        self.capacity = capacity
        
        self.current_floor = 0
        # self.last_floor = 0
        self.direction = 1 # 1 for up, and -1 for down
        self.daytime = day_time
        self.at_floor = True # At each timestep, check if a floor is reached. If so, wait a few seconds
        
        self.height = 0
        self.floors = floors
        self.floor_heights = {floor.height : floor.number for floor in floors}

    def add_floor(self, floor):
        self.floors.append(floor)
        print(f'added floor {floor.number} at height {floor.height} to elevator {self.number}')

    def path_sort(self):
        # Sorts the destinations of the passengers, in this case, a first in first out structure is used
        self.direction = 1 if self.passengers[0].destination > self.current_floor else -1


    def floor_reached(self, t):
            # self.last_floor = self.current_floor
            self.current_floor = self.floor_heights[self.height]
            cf = self.current_floor

            # drop the people in the corresponding floor
            drop_off = [person for person in self.passengers if person.destination == cf]
            # If there are people in the elevator, drop them off
            if drop_off:
                for x in drop_off:
                    self.passengers.remove(x)
                    self.total_mass -= x.mass
                    print(f'Someone has successfuly reached floor {cf} from floor {x.base_floor} at time {t} seconds')
            
            # pick up people in the corresponding floor, by iterating over the people currently waiting
            for p in self.floors[cf].q:
                # Check if the floor capacity has been reached
                if len(self.passengers) >= self.capacity:
                    print(f'Elevator capacity {self.capacity} reached on floor {cf}. Apologies for any inconvenience')
                    continue
                else:
                    self.passengers.append(p)
                    self.total_mass += p.mass
            
            # generate the direction and path for next journey
            self.path_sort()

    def process(self, t, dt):
        # Check if elevator has passengers, if not, wait
        if self.passengers:
            # Check if elevator is at the floor height, otherwise, move the elevator
            fh = self.floor_heights
            if self.height in fh.keys():
                self.floor_reached(t)
                self.at_floor = True
            else:
                self.at_floor = False
                self.height += dt*self.velocity*self.direction
        
        # If no passengers, go to the closest floor with passengers
        else:
            nextfloor_proximities = {fl.number:abs(fl.number-self.current_floor)  for fl in self.floors if fl.q}
            prox_list =[]
            nextfloor_list=[]
            if nextfloor_proximities.keys():
                for fl, prox in nextfloor_proximities.items():
                    # Separate the dictionary into proximities and floors, to evaluate and select the closest floor
                    prox_list.append(prox)
                    nextfloor_list.append(fl)

                # If it's earlier in the day, pick the lowest floor with the closest passenger
                if self.daytime == "morning":
                    nextfl = nextfloor_list[prox_list.index(min(prox_list))]

                # If it's later in the day, pick the higher floors
                elif self.daytime == "afternoon":
                    prox_list = prox_list.reverse()
                    nextfloor_list = nextfloor_list.reverse()
                    nextfl = nextfloor_list[prox_list.index(min(prox_list))]
                
                # Update the direction
                self.direction = 1 if nextfl>self.current_floor else -1

            # If no passengers on any floors, wait
            else:
                return