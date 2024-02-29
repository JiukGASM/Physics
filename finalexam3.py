import numpy as np
import matplotlib.pyplot as plt
from math import *
import random

chisquares = []
for j in range(1000):
    probability = []
    for i in range(0, 24):
        p = (10 ** i * exp(-10)) / factorial(i)
        probability.append(p)
    probability[23] = probability[23] + (1 - sum(probability))

    counts = []
    for i in range(0, 6):
        count = np.random.choice(np.arange(0, 24), p=probability)
        counts.append(count)

    experiments = np.array(range(0, 6))
    error = np.sqrt(counts)

    from scipy.optimize import curve_fit


    def f(experiments, a):
        return np.zeros(N) + a


    a = 10  # init. the const. function
    N = 6

    start = (10)  # starting position

    popt, pcov = curve_fit(f, experiments, counts, sigma=error, p0=start, absolute_sigma=True)

    # Compute chi square
    Nexp = f(experiments, *popt)
    r = counts - Nexp
    chisqc = np.sum((r / error) ** 2)
    chisquares.append(chisqc)





#draw

# chisquare function definition
def func (x, nu) :
    norm = np.power(2, nu/2.0) * gamma(nu/2.0)
    powe = np.power(x, nu/2.0-1)
    expo = np.exp(-x/2.0)
    return (1.0/norm) * powe * expo

nu = 5
delta_x = 0.0001 # time step
x = np.arange(0.0, 40.0, delta_x)

plt.grid(True)
plt.plot(x,func(x,nu),'r')
plt.hist(chisquares, bins=100, density=True, histtype='step')
plt.show()

