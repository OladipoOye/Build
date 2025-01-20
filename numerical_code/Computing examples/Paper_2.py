import numpy as np
import math
import matplotlib.pyplot as plt
# question 3 

# one sided taylor series differential approximation


def f(x):
    f = x*3 + 5
    return f


#def taylor_approx(n, h):
    x = np.linspace(-10, 10, n)
    one = []
    two = []
    for i in range(len(x)):
        taylor1 = (f(x[i]+h) - f(x[i])) / h
        taylor2 = (f(x[i]+h) - f(x[i]-h)) / 2*h
        actual =  3*(x[i]**2)
        one.append( (taylor1 - actual) / h)
        two.append( (taylor2 - actual) / h**2)
    plt.plot(x, one, 'rx', label='onesided')
    plt.plot(x, two, 'gx', label='twosided')
    plt.legend()
    plt.show()
    
    
#taylor_approx(100, 0.01)

def taylor_approx_proper(ind, h, x):
        taylor1 = (f(x+h) - f(x)) / h
        taylor2 = (f(x+h) - f(x-h)) / 2*h
        actual =  3*(x**2)
        if ind==0:
            return print(taylor1 - actual)
        if ind !=0:
            return print(taylor2 - actual)


#taylor_approx_proper(1, 0.01, 3)
        
    

# question 4
# function is x squared * sine(x squared)

def comparison(x, h):
    def f_1(x):
        f = (x**2) * np.sin(x**2)
        return f
         
    actual = (2*x*np.sin(x**2)) + (2*(x**3)*np.cos(x**2))
    z = f_1(x + 1j*h)
    diff_1 = z.imag / h
    diff_2 = (f_1(x+h) - f_1(x-h)) / 2*h
        
    error_complex = diff_1 - actual
    error_twosided = diff_2 - actual
    return print("comparison is", error_complex, error_twosided)


comparison(10, 10**(-9))
comparison(10, 10**(-12))
comparison(10, 10**(-15))
comparison(100, 10**(-9))
comparison(100, 10**(-12))
comparison(100, 10**(-15))
comparison(1000, 10**(-9))
comparison(1000, 10**(-12))
comparison(1000, 10**(-15))
comparison(10000, 10**(-9))
comparison(10000, 10**(-12))
comparison(10000, 10**(-15))

# question 5 3 point average
def point_3_avg(x):
    avg = []
    for n in range(len(x) -2):
        avg.append(x[n] + x[n+1] + x[n+2] / 3)
    return avg


def fx(x):
    return (np.sin(x) + np.cos(10*x)) / 5

z = np.linspace(0, 2*np.pi, 51)
z1 = np.linspace(0, 2*np.pi, 49)
fx_list = []
for i in range(len(z)):
    fx_list.append(fx(z[i]))
fx_array = np.array(fx_list)

for j in range(len(fx_array) - 2):
    point_3 = point_3_avg(fx_array)
point_3.append(fx_array[49] + fx_array[50] / 2)
point_3.append(fx_array[50])
plt.plot(z, fx_list, 'r', label='original')
plt.plot(z, point_3, 'g', label='3 point moving avg')
plt.legend()
plt.show()


# question 5b baker building


#question 1 binary search

def binary(x, n):
    len_x = len(x)
    low, hi = 0, len_x -1
    if n<x[low] or n>x[hi]:
        return None
    while True:
        mid = low + hi / 2
        if n > x[mid]:
            low = mid + 1
        elif n < x[mid]:
            hi = mid - 1
        elif n == mid:
            return mid            