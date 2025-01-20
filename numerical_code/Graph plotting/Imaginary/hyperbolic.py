import numpy as np
import matplotlib.pyplot as plt
# hyperbolic functions don't work for some reason
N = 500
times = np.linspace(-8*np.pi, 8*np.pi, N-1)
shy = []
cosh = []
tanh = []
for i in range(N-1):
    shy.append(np.sinh(times[i]))
    cosh.append(np.cosh(times[i]))
    tanh.append(np.tanh(times[i]))
plt.plot(times, shy, 'r*', label='sinh(x)')
plt.plot(times, cosh, 'b', label='cosh(x)')
plt.plot(times, tanh, 'g', label='tanh(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('hyperbolic graphs using numpy')
plt.show()
 # doesn't work this way either
shy2 = []
cosh2 = []
tanh2 = []
for n in range(N-1):
    shy2.append((np.exp(times[n])-np.exp(times[n])) / 2)
    cosh2.append((np.exp(times[n])+np.exp(times[n])) / 2)
    tanh2.append((np.exp(times[n])-np.exp(times[n]))/ (np.exp(times[n])+np.exp(times[n])))
plt.plot(times, shy2, 'r*', label='sinh(x)')
plt.plot(times, cosh2, 'b', label='cosh(x)')
plt.plot(times, tanh2, 'g', label='tanh(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('hyperbolic graphs via exponential')
plt.show()