# This project aims to determine the design efficiency of an aircraft using numerical methods.
# The code is structured to allow for easy modification and testing of different design parameters.
# This is made in conjunction with the Aircraft Design Elective at the University of Cambridge.
# There will be one aircraft class, with input parameters for the design.
# M = 0.85, Cl = 0.5 (cruise) and Cl = 1.6(Take-off) All constants assumed based on large aircraft curves, and will have to be adapted for smaller/different types of aircrafts

import numpy as np
#import matplotlib.pyplot as plt

class Aircraft:
    def __init__(self, empty_weight, passengers, max_fuel_weight, range_f, cruise_alt, M, L_D, AFR, eta_th, fuel_weight = 300):
        self.range = range_f
        self.cruise_alt = cruise_alt
        self.M = M  # Cruise Mach number
        self.lift_drag_ratio = L_D
        self.max_fuel_weight = max_fuel_weight
        self.passengers = passengers
        self.empty_weight = empty_weight
        self.fuel_mass = min(fuel_weight, self.max_fuel_weight)
        self.AFR = AFR  # Air to fuel ratio
        self.eta_th = eta_th  # Thermal efficiency of the engine
        
    def calculate_weight(self):
        g = 9.81
        # Avg passenger weight is 90kg including luggage 
        payload_mass = self.passengers * 90
        # Check for too many passengers
        if (payload_mass > (self.fuel_mass / 3)):
            print("Too many passengers, reduce")
        total = (self.fuel_mass + payload_mass + self.empty_weight) * g
        return total
        
    def reduce_passengers(self, passengers):
        self.passengers -= passengers
        self.calculate_weight()
        return self.passengers
    
    
    # Cruise conditions: temperature, density, thrust and speed, M=0.85, Cl= 0.5
    def calculate_temperature(self):
        # Calculate the temperature at cruise altitude using the International Standard Atmosphere (ISA) model
        # T = T0 - (0.0065 * self.cruise_alt)
        T0 = 288.15
        T = T0 - (0.0065 * self.cruise_alt)
        return T
    
    def calculate_density(self, inital=False):
        # Calculate the density based on the temperature and pressure at cruise altitude
        P0 = 101325
        T0 = 288.15
        R = 287.05
        if (inital):
            rho = P0 / (R*T0)
            return rho
        T = self.calculate_temperature()
        # P = P0 * (1 - (T0 - T) / T0) ** (9.81 / (0.0065 * R))
        P = P0 * (1 - (0.0065 * self.cruise_alt) / T0) ** (9.81 / (0.0065 * R))
        # Calculate density based on pressure
        rho = P / (R*T)
        return rho
    
    def calculate_cruise_thrust(self):
        # Calculating the cruise net thrust, based on L/D Ratio
        # At cruise, drag is equal to net thrust, and lift is equal to weight
        # As a result, Fn/W = 1/ (L/D)
        Fn = self.calculate_weight * (1 / self.lift_drag_ratio)
        return Fn
    
    def calculate_cruise_speed(self):
        M = self.M
        gamma = 1.4
        R = 287
        T = self.calculate_temperature()
        # The Mach no is the ratio of the flight speed and the local speed of sound
        # M = V / sqrt(gamma*R*T)
        V = M * np.sqrt(gamma*R*T)
        return V
    
    def calculate_mdotf(self):
        # Fuel consumption rate calculated based on total change and total time
        initial_weight = self.calculate_weight() / 9.81
        final_weight = (self.passengers * 90) + self.empty_weight
        mdotf = (initial_weight - final_weight) / (self.range / self.calculate_cruise_speed()) 
        return mdotf
    
    
    def calculate_distance(self, W_start, W_end):
        # The Breguet Range equation gives us the distance travelled at a given weight/time
        # It can be derived by subbing in the sfc, into the dw = mdotf*g, then separating the variables and integrating
        # s = (V* L/D) / (g*sfc) * ln(Wstart/Wend)
        # From this, we can see that the range is dependent on the cruise height, velocity, l/d, sfc and fuel consumption
        V = self.calculate_cruise_speed()
        L_D = self.lift_drag_ratio
        int_m = self.calculate_weight()
        range = self.range
        
        sfc = self.calculate_sfc()
        
        s = np.log(W_start/W_end) * (V * (L_D)) / (9.81 * sfc)
        return s
        
    
    # Top-of-flight conditions
    def calculate_TOF_thrust(self, theta):
        # Theta is the inclination of the plane to the horizontal at top-of-flight (max thrust)
        # Theta must be in radians
        Fn = self.calculate_weight * ( (1 / self.lift_drag_ratio) * np.sin(theta) )
        return Fn
    
    
    # Take-off conditions
    def calculate_wing_area(self):
        # The Wing Area is set by the lift coefficient and takoff speed
        # Cl = L / 0.5*rho_sl*V^2*A
        rho_sl = self.calculate_density(inital=True)
        # L = W at takeoff
        L = self.calculate_weight()
        # Takeoff conditions
        Cl = 1.6
        V = 90
        # Calculate Area
        A = L / (0.5 * rho_sl * V**2 * Cl)
        return A
        
    def calculate_jet_velocity(self):
        # The thermal efficiency comes from the change in kinetic energy of the flow, due to the heat release
        # The thermal efficiency is also related to the thermodynamic efficiency of the cycle
        # The jet velocity is therefore a function of the thermal efficiency, LCV and the plane speed
        # We will however calculate the jet velocity based on the thrust and the mass flow rate of air
        # Fn = mdota * (Vj - V)
        AFR = self.AFR
        V = self.calculate_cruise_speed()
        Fn = self.calculate_cruise_thrust()
        
        mdota = self.calculate_mdotf() * AFR
        
        Vj = (Fn / mdota) + V
        return Vj
    
        
    # Performance metrics
    def calculate_sfc(self):
        # The specific fuel consumption is the mass flow rate of fuel, per engine net thrust
        # Assuming cruise conditions dominate for fuel consumption, and that the fuel consumption stays steady
        # The time of flight is equal to the range over the speed
        Fn = self.calculate_cruise_thrust()
        mdotf = self.calculate_mdotf()
        # Calculate sfc
        sfc = mdotf / Fn
        return sfc
    
    def calculate_Wf_sWp(self, s):
        # The fuel burn per km payload is a key environmental metric
        # It's useful for evaluating fuell usage
        # H is the exponent of the breguet range equation
        V = self.calculate_cruise_speed()
        L_D = self.lift_drag_ratio
        g = 9.81
        sfc = self.calculate_sfc()
        H = (V*L_D) / (g*sfc)
        
        #We/Wp
        w_ratio = self.empty_weight/(self.passengers * 90)
        
        Wf_sWp = (1/s) * (w_ratio) * (np.exp(H*s) - 1)
        return Wf_sWp
        # Either minimise the weight ratio, or H in order to minimise the fuel burn per km payload
        
    def calculate_EI(self, s):
        # The emissions index is the mass of pollutant(CO2) over the mass of fuel burnt
        # Assume average chemical formula of C8H18 for jet fuel
        EI_CO2 = 3.1
        
        # CO2 per passenger_km is CO2 per fuel (EI_CO2) * (fuel burn per km payload) * (passenger mass )
        EI_CO2_sNp = self.calculate_Wf_sWp(s) * EI_CO2 * 90
        return EI_CO2_sNp
    
    
    # Efficiencies
    # Simplifications are:
    # mdota >> mdotf - So neglect mdotf in calculations apart from heat release
    # Regardless of bypass Vcj = Vbj = Vj (The core and bypass jet air has the same velocity)
    # From SFME of engine => Fn = mdota(Vj - V)
    # SFEE of engine => Q = mdota*cp*(Tj - Ta) + 0.5*mdota*(Vj^2 - V^2)
    # From SFEE of engine => mdotf*LCV = mdota*cp*(Tj - Ta) + 0.5*mdota*(Vj - V)^2 + mdota*V*(Vj - V) 
    
    def calculate_gross_thrust(self, mdota, Vj):
        # The gross thrust is the thrust with no inlet momentum (V=0)
        # Hence, Fn = Fg - mdota*V
        Vj = self.calculate_jet_velocity(LCV = 43e6)
        Fg = mdota * Vj
        return Fg
        
    def calculate_eta_p(self):
        # The propulsive efficiency comes from the power to the aircraft(V*Fn), due to the change in kinetic energy of the flow
        # V*Fn is equal to the last term of the expanded SFEE equation (mdota*V*(Vj - V))
        # The change in kinetic energy is 0.5*mdota*((Vj**2) - V**2)
        # Due to the difference of 2 squares, this ratio simplifies down to 2V/(Vj + V)
        V = self.calculate_cruise_speed()
        Vj = self.calculate_jet_velocity(LCV=43e6)
        
        #Froude equation
        eta_p = 2*V / (Vj + V)
        
        # Hence if Vj->V, there will be a higher eta_p, but no thrust.
        # The ideal case is to make the jet velocity similar to the aircraft velocity, but have a large mass flow rate of air, so that the thrust is sufficient to drive the plane
        return eta_p
    
    def calculate_eta_o(self):
        eta_p = self.calculate_eta_p()
        eta_o = eta_p * self.eta_th
        return eta_o
