# This project aims to determine the design efficiency of an aircraft using numerical methods.
# The code is structured to allow for easy modification and testing of different design parameters.
# This is made in conjunction with the Aircraft Design Elective at the University of Cambridge.
# There will be one engine class, as an extension of the aircraft class in the design_efficiency file.
# The engine class will have input parameters for the design.

#Currently under development, and will be used to calculate the bypass ratio, and thermodynamic efficiency of the engine.

import numpy as np

class Engine:
    def __init__(self, thrust, fuel_flow_rate, specific_fuel_consumption, rpc, rpt, eta_fan):
        self.thrust = thrust  # Thrust in Newtons
        self.fuel_flow_rate = fuel_flow_rate  # Fuel flow rate in kg/s
        self.specific_fuel_consumption = specific_fuel_consumption  # SFC in kg/(N*s)
        self.rpc = rpc  # Pressure ratio across the compressor
        self.rpt = rpt # Pressure ratio across the turbine
        self.fan_efficiency = eta_fan  # Fan efficiency