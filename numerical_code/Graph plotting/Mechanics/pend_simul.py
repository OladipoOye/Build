import numpy as np
import matplotlib.pyplot as plt

# eom is thetaddot = -(g/l)*sin(theta)
# theta is the angle of the pendulum
# theta0 is the initial angle
# thetadot is the angular velocity
# thetadot0 is the initial angular velocity
# thetaddot is the angular acceleratiom

def pendulum(t, theta0, thetadot0, N):
    g = 9.8
    l = 1
    dt = t/N
    
    # semi-implicit first order method
    theta = np.zeros(N)
    thetadot = np.zeros(N)
    thetaddot = np.zeros(N)
    theta[0] = theta0
    thetadot[0] = thetadot0
    thetaddot[0] = -(g/l) * np.sin(theta0)
    
    #verlet second order method
    theta_v = np.zeros(N)
    thetadot_v = np.zeros(N)
    thetaddot_v = np.zeros(N)
    theta_v[0] = theta0
    thetadot_v[0] = thetadot0
    thetaddot_v[0] = -(g/l) * np.sin(theta0)
    
    
    for n in range(1, N):
        #accelerations
        thetaddot[n] = -(g/l) * np.sin(theta[n-1])
        thetaddot_v[n] = -(g/l) * np.sin(theta_v[n-1]) 
        
        #velocities
        thetadot[n] = thetadot[n-1] + dt*thetaddot[n]
        thetadot_v[n] = thetadot_v[n-1] + 0.5*(thetaddot_v[n-1] + thetaddot_v[n])*dt
        
        #displacements
        theta[n] = theta[n-1] + dt*thetadot[n]
        theta_v[n] = theta_v[n-1] + thetadot_v[n-1]*dt + 0.5*(thetaddot_v[n-1])*(dt**2)
    
    t_list = np.linspace(0, t, N)
    plt.plot(t_list, theta, 'r')
    plt.plot(t_list, theta_v, 'g')
    plt.ylabel("amplitude")
    plt.xlabel("time")
    plt.legend(loc=1)
    plt.title('angular diplacement against time')
    plt.show()
    
pendulum(20, np.pi/4, 0, 300000)