from elevator import Elevator
from person_and_floor import Person, Floor
import numpy as np

# This is where the simulation will be run
# The main function takes in a dictionary of people, and arrival times
# These people will have randomized times and floors, and will all have a mass less than 100kg


def main(sim_time, dt, num_floors, num_ppl):
    
    # Generate the test data
    # The mass is randomly generated, to be a value between 40 and 100
    # The destination and floor is also randomly generated between the floor count (0 included)
    arrival_dict = {Person(mass=(40 + np.random.rand()*60), destination=int(np.random.rand()*(num_floors)), floor=int(np.random.rand()*num_floors), dummy_name=((i+1)*100)): float(int(np.random.rand()*10))/5 for i in range(num_ppl)}
    # print(arrival_dict)
    
    elevator_floors = [Floor(number=i, height=(i*5)) for i in range(num_floors)]
    elevator1 = Elevator(total_mass=100, counter_balance=50, capacity=10, floors=elevator_floors)
    t = 0
    
    # Run simulation, by adding the person to an initial floor based on arrival time, and running the elevator function at each time step
    while t < sim_time:
        for p, time in arrival_dict.items():
            if time == t:
                elevator_floors[p.initial_floor].q.append(p)
                print(f"[t={t}] Person {p.dummy_name} arrives at floor {p.initial_floor} (dest={p.destination})")

        # Advance elevator
        elevator1.process(timer=t)
        t += dt

main(sim_time=30, dt=0.1, num_floors=4, num_ppl=10)