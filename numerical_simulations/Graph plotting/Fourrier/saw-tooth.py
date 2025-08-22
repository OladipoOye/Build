import numpy as np
import matplotlib.pyplot as plt

# saw tooth wave
# Period is 2pi
# avg value of wave is d, which is a free input variable

def st(N, d):
    x = np.linspace(-np.pi, np.pi, N)
    f = np.zeros(len(x))
    fn = []
    for n in range(1, N):
        for t in range(len(x)):
            fn.append((-1**(n+1)) * np.sin(x[t]*n) / n)
            f[t] += fn[t]
        #print(fn)
    for j in range(len(f)):
        f[j] = (f[j] * 2/np.pi) + d
    plt.plot(f, x, 'r')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.title('saw tooth wave')
    plt.show()


st(100, 0)
