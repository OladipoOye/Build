import numpy as np
import matplotlib.pyplot as plt

# test for complex
# must be passed as an array
ar = np.array([1, 2+3j, 2-2j, 5, 5j])
x = ar.real
y = ar.imag

plt.plot(x, y, 'gx')
plt.xlabel('real')
plt.ylabel('imaginary')
plt.show()

# the theorem states that e^jnx = (cos(x) + isin(x))^n = cos(nx) + isin(nx)
# form the x list, set length and power
N, n = 100, 5
x = np.linspace(-np.pi, np.pi, N)
# exponential
y = []
for i in range(N):
    y.append(np.exp(1j * n * x[i]))
y1 = np.array(y)
# sinusodal nx solution
y2 = []
for i in range(N):
    y2.append(np.cos(n*x[i]) + (1j*np.sin(n*x[i])))
# (cos + isin)^n solution
y3 = []
for i in range(N):
    y3.append((np.cos(x[i]) + 1j*np.sin(x[i]))**n)

#plt.plot(y1.real, y1.imag, 'r*', label='using complex values only')
plt.plot(x, y, 'g*', label='idek genuinely - exponent solution')
plt.plot(x, y2, 'm-', label='sinusodal nx solution')
plt.plot(x, y3, 'bx', label='all to the power of n')
plt.xlabel('x')
plt.ylabel('y')
plt.title('$e^(5jx)$ - de moivre')
plt.legend()
plt.show()