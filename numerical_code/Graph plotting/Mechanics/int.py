import matplotlib.pyplot as plt
import numpy as np

# for the integration of eyler and semi-implicit re-run for a car acceleration
# a = -u*g
# v(n) = v(n-1) + a*dt
# euler: x(n) = x(n-1)  + v(n-1)*dt
# semi-implicit x(n) = x(n-1) + v(n)*dt
# analytic: x(t) = x0 + v0*t + (u*g*t^2)/2


def plot( x0, v0, u, N, g=10):
    t = np.linspace(0, 15, N)
    dt = 15/N
    xe = np.zeros(N)
    xs = np.zeros(N)
    xdot = np.zeros(N)
    an = np.zeros(N)
    xdot[0] = v0
    xe[0], xs[0], an[0] = x0, x0, x0
    xddot = -u*g

# the analytic solution
    def z(t1):
        return x0 + v0*t1 + xddot*((t1**2)/2)
# the numerical integration
    for n in range(1, N):
        xdot[n] = xdot[n-1] + xddot*dt
        xe[n] = xe[n-1] + xdot[n-1]*dt
        xs[n] = xs[n-1] + xdot[n]*dt

    for i in range(1, N):
        an[i] = z(t[i-1])
        print(an[i-1])

    
    plt.plot(t, xe, 'r+', label='euler')
    plt.plot(t, xs, 'b+', label='semi-implicit')
    plt.plot(t, an, 'g+', label='analytic')
    plt.xlabel('Time')
    plt.ylabel('Distance')
    plt.legend()
    plt.show()

plot(50, 20, 0.4, 80)


x = 1j