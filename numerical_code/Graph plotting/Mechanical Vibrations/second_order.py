import numpy as np
import matplotlib.pyplot as plt


#dashpot and spring in parallel
# equation is yddot / (w_n)^2  + 2*zeta*ydot/ (w_n) + y = x 
# x0 will be the step
# zeta = lamda/2*sqrt(km)
# w_n = sqrt(k/m)
def step_underd(N, w_n, zeta, x0):
    w_d = w_n * np.sqrt(1 - (zeta**2))
    phi = np.arctan(zeta * w_d / w_n)
    t_list = np.linspace(0, 5, N-1)
    y_list = []
    approx_list = []
    non_dim_amp = []
    
    def y_actual(t):
        y = x0 * (1 - (np.exp(-zeta*w_n*t)*np.cos(w_d*t - phi) / np.cos(phi)))
        return y
    
    def y_approx(t):
        y = x0 *(1 - (np.exp(-zeta*w_n*t)*np.cos(w_d*t - phi)))
        return y
    
    for i in range(N-1):
        y_list.append(y_actual(t_list[i]))
        approx_list.append(y_approx(t_list[i]))
        non_dim_amp.append(y_list[i] / x0)
        
    
    plt.plot(t_list, y_list, 'g', label='step response for second order')
    #plt.plot(w_d*t_list, non_dim_amp, 'rx', label='non dimensional amplitude against time')
    plt.plot(t_list, approx_list, 'm*', label='small angle approx')
    plt.xlabel('time')
    plt.ylabel('displacement')
    plt.title('Second order step response')
    plt.legend()
    plt.show()
    
step_underd(1200, 3, 0.3, 20)
# Only zeta affects the small angle approximation
# increasing the natural time frequency squishes the graph
# increasing w_n makes the initial gradient steeper
# all graphs start as sinusodal, then level off
# changing x0 only changes the magnitude of the displacement, not shape

def imp_underd(N, w_n, zeta, I):
    w_d = w_n * np.sqrt(1 - (zeta**2))
    phi = np.arctan(zeta * w_n/w_d)
    t_list = np.linspace(0, 10, N-1)
    y_list = []
    def y_imp(t):
        y = I / np.cos(phi) * ((-zeta*w_n*np.exp(-zeta*w_n*t)*np.cos(w_d*t - phi)) + (w_d*np.exp(-zeta*w_n*t)*np.sin(w_d*t - phi)))
        return y 
    for i in range(N-1):
        y_list.append(y_imp(t_list[i]))
    plt.plot(t_list, y_list, 'rx')
    plt.xlabel('time')
    plt.ylabel('displacement')
    plt.title('Second Order Impulse response')
    plt.show()

#imp_underd(100, 3, 0.3, 20)
# oscillates between negative and positive
# increasing the natural time frequency squishes the graph
# decreasing zeta reduces the damping
# changing the impulse only affects the magnitude of the displacement, not the shape