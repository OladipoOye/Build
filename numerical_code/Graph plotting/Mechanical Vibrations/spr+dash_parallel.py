import numpy as np
import matplotlib.pyplot as plt

# equation is Tydot + y = F/k
# T is lamda / k 

def ramp(N, lamda, k,  rate):
    t_list = np.linspace(0, 5, N-1)
    # applied force varying from 0 to f0 in time tau
    T  = lamda / k
    y_values = []
    
    def y_ramp(t):
        # when integrated, if y=0 at t=0, then the constant = rate* T / k
        y = rate / k * ((t + (T * np.exp(-t/T))) - T)
        return y 
    
    for i in range(N-1):
        y_values.append(y_ramp(t_list[i]))
    
    plt.plot(t_list, y_values, 'm')
    plt.xlabel('Time (s)')
    plt.ylabel('y (m)')
    plt.title('Ramp response of dashpot and spring in parallel')
    plt.show()
    

ramp(60, 1, 1.5, 10)
# The bigger the T, the longer the transient response

def step(N, lamda, k, f0):
    t_list = np.linspace(0, 5, N-1)
    T  = lamda / k
    y_values = []
    
    def y_step(t):
        y = f0/ k * (1 - np.exp(-t/T))
        return y
    
    for i in range(N-1):
        y_values.append(y_step(t_list[i]))
    plt.plot(t_list, y_values, 'g')
    plt.xlabel('Time (s)')
    plt.ylabel('y (m)')
    plt.title('Step response of dashpot and spring in parallel')
    plt.show()

step(60, 1, 1.5, 10)

def Impulse(N, lamda, k, I):
    t_list = np.linspace(0, 5, N-1)
    T  = lamda / k
    y_values = []
    
    def y_imp(t):
        y = I / (T * k) * np.exp(-t/T)
        return y
    
    for i in range(N-1):
        y_values.append(y_imp(t_list[i]))
    plt.plot(t_list, y_values, 'r')
    plt.xlabel('Time (s)')
    plt.ylabel('y (m)')
    plt.title('Impulse response of dashpot and spring in parallel')
    plt.show()

Impulse(60, 1, 1.5, 10)