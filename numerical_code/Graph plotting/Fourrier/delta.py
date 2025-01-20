import numpy as np
import matplotlib.pyplot as plt

def plot(n, L, k, d, a):
    an_term = np.zeros(n+1)
    bn_term = []
    f = []
    x = np.linspace(-L, L, n)
    for i in range(1, n+1):
        bn_term.append(-2 * k / (L-a) * np.sin(i*np.pi*a / L))
        f.append(d + an_term[i-1] + bn_term[i-1])
    plt.plot(x, f, 'r', label='delta function')
    plt.plot(x, np.zeros(len(x)), 'g', label='x-axis')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()


plot(200, 10, 20, 0, 2.5)