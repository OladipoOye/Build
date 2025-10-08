# from person_and_floor import Person, Floor

class Elevator:
    def __init__(self, total_mass, counter_balance, capacity=10, floors=[], number=0, day_time="morning", data=False):
        self.number = number
        self.total_mass = total_mass
        self.counter_balance_mass = counter_balance
        self.passengers = []
        self.capacity = capacity
        
        self.current_floor = 0
        self.direction = 1 # 1 for up, and -1 for down
        self.daytime = day_time
        self.wait_count = 1 # Counter to implement stoppage when a floor is reached
        
        self.height = 0
        self.floors = floors
        self.floor_heights = {floor.height : floor.number for floor in floors}

        self.collect_data = data # Boolean to represent if data should be tracked
        self.data_dict = {} # Tracking data, with the key as the person's dummy name, and the value as a list containing the arrival time, and time of journey completion
        # In addition, to speed up simulation times, the print statements will be reduced if data is being collected

    def check_other_floors(self):
        # Gather the number of people on each floor
        waiting_list = [len(fl.q) for fl in self.floors]
        # If there's at least one person on any floor, return true, else return false
        if max(waiting_list) > 0:
            return True
        
        return False

    def set_no_passengers_path(self):
        # Gather a dictionary with the floor number, and proximity to current/last floor
        nextfloor_proximities = {fl.number:abs(fl.number-self.current_floor) for fl in self.floors if fl.q}

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


    def set_FIFO_path(self):
        # Sorts the destinations of the passengers, in this case, a first in first out structure is used
        self.direction = 1 if self.passengers[0].destination > self.current_floor else -1
    
    def move(self):
        # Shift the elevator at a speed of 0.25m per time count
        self.height += self.direction*0.25


    def drop_off(self, time):
        drop_off_list = [person for person in self.passengers if person.destination == self.current_floor]
        # If there are people in the elevator with a destination of the current floor, drop them off
        if drop_off_list:
            for leaver in drop_off_list:
                self.passengers.remove(leaver)
                self.total_mass -= leaver.mass
                if self.collect_data:
                    self.data_dict[leaver.dummy_name] = [leaver.arrival_time, time]
                else:
                    print(f'Person {leaver.dummy_name} has successfuly reached floor {self.current_floor} from floor {leaver.initial_floor} at time {time} seconds')
    
    def pick_up(self, time):
        # Check if the current floor is empty, and if not, pick up people
        # Pick people up by iterating over the people waiting on the floor, and adding them into the lift passengers
        if self.floors[self.current_floor].q:
            floor_info = {per.dummy_name: per.destination for per in self.floors[self.current_floor].q}
            if not self.collect_data:
                print(f'passengers with destinations on floor {self.current_floor} are: {floor_info}')
            # Create a copy of the floor queue to prevent modifications whilst picking up passengers
            for p in self.floors[self.current_floor].q[:]:
                # Check if the floor capacity has been reached
                if len(self.passengers) >= self.capacity:
                    print(f'Elevator capacity {self.capacity} reached on floor {self.current_floor}. Apologies for any inconvenience')
                    continue
                # Check if the person isn't going anywhere
                elif p.destination == p.initial_floor:
                    if self.collect_data:
                        self.data_dict[p.dummy_name] = [p.arrival_time, p.arrival_time]
                    else:
                        print(f'Destination already reached with current floor for passenger {p.dummy_name}, lift will not proceed with them.')
                    self.floors[self.current_floor].q.remove(p)
                else:
                    self.passengers.append(p)
                    # print(f'passenger {p.dummy_name} has been picked up from floor {floor}, at time {time}, with destination {p.destination}')
                    self.total_mass += p.mass
                    self.floors[self.current_floor].q.remove(p)
            
            if not self.collect_data:
                # Display the lift passengers after pickup
                p_names = [str(passenger.dummy_name) for passenger in self.passengers]
                formatted_p_names = " and ".join(p_names)
                print(f'passengers in elevator now are: {formatted_p_names}')

    def floor_reached(self, t):
            # run the drop off, then pick up operation
            self.drop_off(time=t)
            self.pick_up(time=t)
            
            # After a floor is reached, if there are still passengers in the lift, generate the direction from first passenger
            # If not, check if there are passengers on other floors
            # If there are, generate the path from the closes passenger holding floor, and move
            # However if there are no passengers in sight, wait 
            if self.passengers:
                self.set_FIFO_path()
                self.move()
            elif self.check_other_floors():
                self.set_no_passengers_path()
                if not self.collect_data:
                    print(f'No passengers in lift at time {t}s, going to find new passengers at other floors')
                self.move()
            else:
                # print('No passengers in lift or on any floors, elevator is now idle')
                return

            
    def process(self, timer):
        fh = self.floor_heights
        at_floor = False
        tol = 1e-6
        for h in fh.keys():
            if abs(self.height - h) < tol:
                at_floor = True
                self.current_floor = fh[h]
        #print(f'height is {self.height}m, time is {timer}s')
        
        # Check if the elevator is currently at a floor
        if at_floor:
            # If so, wait at the floor for a few counts, then process the drop/pickup operations
            self.wait_count += 1
            # print(f'waiting at floor {fh[self.height]}, count {self.wait_count}')
            if (self.wait_count%5 == 0):
                # Once the count reaches 5 time steps, call the operation for a floor reached
                # print(f'now commencing operations at floor {fh[self.height]}')
                self.floor_reached(timer)
        
        # Procedure if not at a floor
        else:
            # Check if there are passengers in the lift, and adjust the path accordingly
            if self.passengers:
                self.set_FIFO_path()
                self.move()
            else:
                # If no passengers in lift, go to the nearest floor with passengers, unless there's no one in sight
                if self.check_other_floors():
                    self.set_no_passengers_path()
                    self.move()
                else:
                    raise RuntimeError('elevator is mid-floors despite no passengers in sight')