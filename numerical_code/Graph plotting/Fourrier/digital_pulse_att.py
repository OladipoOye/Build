import numpy as np
import matplotlib.pyplot as plt


def plot(n, T, d):
    an_term = []
    bn_term = []
    f = []
    t = np.linspace(0, 2*np.pi, n)
    for i in range(1, n+1):
        an_term.append(np.sin(i*T) / i / np.pi * np.cos(i*t[i-1]))
        bn_term.append((1 - np.cos(i*T)) / i / np.pi * np.sin(i*t[i-1]))
        f.append(an_term[i-1] + bn_term[i-1])
    final = [j + d for j in f]
    plt.plot(t, final, 'r', label='fourrier q1')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.axis([t[0], t[-1], -0.25, 1.25])
    #  plt.legend()
    plt.show()


plot(n=17, T=np.pi, d=0.5)