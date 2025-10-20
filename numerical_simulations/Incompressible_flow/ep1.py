# This is my plots for example flows taken from examples paper 1 in the incompressible flow course
import numpy as np
import matplotlib.pyplot as plt

class Grid:
    def __init__(self):
        pass
    
    def cartesian_mode(self, x_start, x_end, y_start, y_end):
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        # Create a grid for cartesian coordinates, from start to end in both directions
        self.x = np.linspace(x_start, x_end, 50)
        self.y = np.linspace(y_start, y_end, 50)
        self.X, self.Y = np.meshgrid(self.x, self.y)

    def polar_mode(self, r_start, r_end, theta_start, theta_end):
        self.r_start = r_start
        self.r_end = r_end
        self.theta_start = theta_start
        self.theta_end = theta_end
        # Create a grid for polar coordinates, from start to end in both directions
        self.r = np.linspace(r_start, r_end, 50)
        self.theta = np.linspace(theta_start, theta_end, 50)
        self.R, self.Theta = np.meshgrid(self.r, self.theta)
        # Convert polar grid to cartesian for plotting
        self.X = self.R * np.cos(self.Theta)
        self.Y = self.R * np.sin(self.Theta)

    def plot_contour(self, Z, title, xlabel, ylabel):
        plt.figure()
        cp = plt.contourf(self.X, self.Y, Z, cmap='viridis')
        plt.colorbar(cp)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

class FlowField:
    def __init__(self, fluid):
        if fluid == 'air':
            self.rho = 1.225  # kg/m^3
        elif fluid == 'water':
            self.rho = 1000  # kg/m^3
        else:  
            raise ValueError("Unsupported fluid type")
        pass

    def v_magnitude(self, u, v):
        return np.sqrt(u**2 + v**2)
    
    def dynamic_pressure(self, v, u):
        return 0.5 * self.rho * self.v_magnitude(u, v)**2
    
    def pressure_coefficient(self, p, p_inf, v, u):
        return (p - p_inf) / self.dynamic_pressure(v, u)


# question 2
# question2_grid = Grid()
# question2_grid.cartesian_mode(-5, 5, -5, 5)
# question2_flow = FlowField(fluid='air')
A = 1
# v_potential_equation2 = 0.5*A*question2_grid.X**2 - 0.5*A*question2_grid.Y**2
# stream_function_equation2 = A*question2_grid.X*question2_grid.Y
k = 10
# pressure_equation2 = k -0.5*question2_flow.rho*A*(question2_grid.X**2 + question2_grid.Y**2)

# question2_grid.plot_contour(stream_function_equation2, 'Question 2 Stream Function', 'X-axis', 'Y-axis')
# question2_grid.plot_contour(v_potential_equation2, 'Question 2 velocity potential', 'X-axis', 'Y-axis')
# question2_grid.plot_contour(pressure_equation2, 'Question 2 Pressure Field', 'X-axis', 'Y-axis')

# question 3
question3_grid = Grid()
question3_grid.polar_mode(0, 10, 0, 5*np.pi/3)
question3_flow = FlowField(fluid='air')
stream_function_equation3 = A*(question3_grid.R**1.2)*np.sin(6*question3_grid.Theta/5)


question3_grid.plot_contour(stream_function_equation3, 'Question 3 Stream Function', 'X-axis', 'Y-axis')
pressure_equation3 = k - 0.5*question3_flow.rho*(1.2*A*question3_grid.R**0.2)**2
question3_grid.plot_contour(pressure_equation3, 'Question 3 Pressure Field', 'X-axis', 'Y-axis')