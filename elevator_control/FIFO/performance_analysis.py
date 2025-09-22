# This aims to analyse the effect of various variables 
# (e.g number of floors, average distance between floors, average time between arrivals etc)
# On the average waiting time for the elevator

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
# import matplotlib.pyplot as plt
# import seaborn as sn
from main import Elevator_Simulation
import numpy as np

number_of_simulations = 500
# Initialise the list for the x variables
linspace_floors = np.ceil(np.linspace(2, 8, number_of_simulations))
num_floors_list = [int(i) for i in linspace_floors]

linspace_distances = np.ceil(np.linspace(1, 10, number_of_simulations))
distance_between_floors = [int(i) for i in linspace_distances]

linspace_arrivals = np.ceil(np.linspace(1, 50, number_of_simulations))
max_arrrival_times = [int(i) for i in linspace_arrivals]

avg_time_between_arrivals = []

linspace_passengers = np.ceil(np.linspace(1, 25, number_of_simulations))
num_passengers = [int(i) for i in linspace_passengers]

# Initialise the list for the output
avg_total_waiting_time = []

# Run simulation 50 times, with varying inputs
for j in range(number_of_simulations):

    # Gather the input variables for the simulation
    floor_count = num_floors_list[j]
    ppl_count = num_passengers[j]
    floor_distance = distance_between_floors[j]
    max_time = max_arrrival_times[j]

    # Run the simulation and collect the data
    arrival_time_separation, results = Elevator_Simulation.gather_data(num_floors=floor_count, num_ppl=ppl_count, distance_between_floors=floor_distance, max_arrival_time=max_time)
    avg_time_between_arrivals.append(arrival_time_separation)

    # Sort the average total waiting time from the dictionary of arrival and journey completion times
    waiting_times = [r[1]-r[0] for r in results.values()]
    avg_total_waiting_time.append(sum(waiting_times)/len(waiting_times))

# Create the results data, and scale it
X = [[num_floors_list[i], distance_between_floors[i], avg_time_between_arrivals[i], num_passengers[i]] for i in range(number_of_simulations)]
X_scaled =  StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, avg_total_waiting_time, test_size=0.3, random_state=42)

# Fit the model using the train data
model = LinearRegression()
model.fit(X=X_train, y=y_train)
coefficients = model.coef_
intercept = model.intercept_

# Print the model coefficients and intercept
print(f"Coefficients are: {coefficients}, with an intercept of {intercept}")

# Build predictive y values using the model, in order to evaluate the model
y_pred = model.predict(X_test)
# Calculate R-squared and RMSE
print("R² Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))