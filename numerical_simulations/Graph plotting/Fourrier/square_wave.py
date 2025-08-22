import numpy as np 
import matplotlib.pyplot as plt

def plot(N, d):
    #  purely odd
    #  a_n = 0
    b_n = []
    f = []
    t = np.linspace(-np.pi, np.pi, N)
    for n in range(1, N+1):
        b_n.append((2 * (1 - ((-1)**n)) / n / np.pi) * np.sin(n*t[n-1]))
        f.append(d + b_n[n-1])
        print("n is", n, ", d is", d, ", d + b_n is", f[n-1], ", t is", t[n-1], ", sine nt =", np.sin(n*t[n-1]))
    plt.plot(t, f, 'r')
    plt.plot(t, np.zeros(len(t)), 'g')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.show()


plot(15, 0)
    