from elevator import Elevator
from person_and_floor import Person, Floor
import random

# This is where the simulation will be run
# The Elevator sim class is split into 2
# The main function aims to provide an interactive, tracable simulation
# The gather data function is a more time-effective implementation of the simulator for gathering data

class Elevator_Simulation:
    def main(sim_time, dt, num_floors, num_ppl):
        
        # Generate the test data
        # The person mass is randomly generated, to be a value between 40 and 100
        # The destination and floor of each person is also randomly generated between the floor count (0 included)
        # The arrival list is the list of people which will queue
        arrival_list = [Person(mass=random.randint(40, 100), destination=random.randint(0,num_floors-1), floor=random.randint(0,num_floors-1), dummy_name=((i+1)*100), arrival_time=random.randint(0, 20)/10) for i in range(num_ppl)]
        
        elevator_floors = [Floor(number=i, height=(i*5)) for i in range(num_floors)]
        elevator1 = Elevator(total_mass=100, counter_balance=50, capacity=10, floors=elevator_floors, data=False)
        t = 0

        # Set a tolerance for the float times, as the 0.1 increment will cause timesteps to not be precise
        tol = 1e-6
        
        # Run simulation, by adding the person to an initial floor based on arrival time, and running the elevator function at each time step
        while t < sim_time:
            for p in arrival_list:
                if abs(p.arrival_time - t) < tol:
                    elevator_floors[p.initial_floor].q.append(p)
                    print(f"[t={t}] Person {p.dummy_name} arrives at floor {p.initial_floor} (dest={p.destination})")
            

            # Advance elevator
            elevator1.process(timer=t)
            t += dt
    
    def gather_data(num_floors, num_ppl, distance_between_floors, max_arrival_time):
        
        # Generates test data for analysis, with a simulation time of 100s, a dt of 0.1 and masses between 40 aand 100
        # The destination and floor number for each passenger will still be randomly generated between 0 and the floor count
        # The arrival time for each passenger will be generated randomly between 0s and the max arrival time/10, and will be a multiple of dt
        # The floors will be equidistance with the distance specified
        arrival_list = [Person(mass=random.randint(40, 100), destination=random.randint(0,num_floors-1), floor=random.randint(0,num_floors-1), dummy_name=((i+1)*100), arrival_time=random.randint(0, max_arrival_time)/10) for i in range(num_ppl)]
        
        # Calculate the averageg time between arrivals
        print(f'length of arrivals is: {len(arrival_list)}')
        avg_time_between_arrivals = sum(p.arrival_time for p in arrival_list) / len(arrival_list)
        
        elevator_floors = [Floor(number=i, height=(i*distance_between_floors)) for i in range(num_floors)]
        elevator2 = Elevator(total_mass=100, counter_balance=50, capacity=num_ppl, floors=elevator_floors, data=True)
        t = 0

        # Set a tolerance for the float times, as the 0.1 increment will cause timesteps to not be precise
        tol = 1e-6
        
        # Run simulation, by adding the person to an initial floor based on arrival time, and running the elevator function at each time step
        while t < 100:
            for p in arrival_list:
                if abs(p.arrival_time - t) < tol:
                    elevator_floors[p.initial_floor].q.append(p)
            

            # Advance elevator
            elevator2.process(timer=t)
            t += 0.1
        
        return avg_time_between_arrivals, elevator2.data_dict


# Simulation run
Elevator_Simulation.main(sim_time=40, dt=0.1, num_floors=4, num_ppl=10)