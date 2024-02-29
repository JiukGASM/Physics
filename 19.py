from math import *
from scipy.integrate import  quad # this is for numerical integration
import numpy as np
import matplotlib.pyplot as plt


# 1. const.model ndf = n= 3 x_min = 1.41
# 2. linear model ndf = n = 2 x_min = 0.532


## integral

# chisquare function definition
def func (x, nu) :
    norm = pow(2, nu/2.0) * gamma(nu/2.0)
    powe = pow(x, nu/2.0-1)
    expo = exp(-x/2.0)
    return (1.0/norm) * powe * expo

# first case
nu = 3 # ndf
minchisquare = 1.41
#numerical integral
I = quad(func, minchisquare, +inf, args = (nu))

print("Ingeral = ", I)

# second case
nu = 2 # ndf
minchisquare = 0.532
#numerical integral 1
I = quad(func, minchisquare, +inf, args = (nu))

print("Ingeral = ", I)


## Fitting

# linear

from scipy.optimize import curve_fit

def f(mass, a, b):
    return np.zeros(N) + a*mass + b

a = 10 # init. the const. function
b = 1 # y-intersect
N = 4

counts = np.array([7,9,12,10]) # data points
mass   = np.array([0.5,1.5,2.5,3.5]) # mass of pumpkins
error  = np.sqrt(counts) # errors poisson error = sqrt of mean

print("Mass (x)", mass)
print("Counts (y)", counts)
print("Error on counts =",error)

A = f(mass, a, b)

print(A)

start = (10,1) # starting position

popt,pcov = curve_fit(f,mass,counts,sigma = error,p0 = start, absolute_sigma=True)
print(popt)
print(pcov)

perr = np.sqrt(np.sqrt(np.diag(pcov)))
print(perr)
print(*popt)

# Compute chi square
Nexp = f(mass, *popt)
r = counts - Nexp
chisq = np.sum((r/error)**2)
df = N - 2
print("chisq =",chisq, "df =",df)

plt.errorbar(mass, counts, yerr=error, fmt= 'o')
plt.show()

# second order

def f(mass, a, b, c):
    return np.zeros(N) + a*mass**2 + b*mass + c

a = -2 # init. the const. function
b = 4 # y-intersect
c = 12
N = 4

counts = np.array([7,9,12,10]) # data points
mass   = np.array([0.5,1.5,2.5,3.5]) # mass of pumpkins
error  = np.sqrt(counts) # errors poisson error = sqrt of mean

print("Mass (x)", mass)
print("Counts (y)", counts)
print("Error on counts =",error)

A = f(mass, a, b, c)

print(A)

start = (10,2,1) # starting position

popt,pcov = curve_fit(f,mass,counts,sigma = error,p0 = start, absolute_sigma=True)
print(popt)
print(pcov)

perr = np.sqrt(np.sqrt(np.diag(pcov)))
print(perr)
print(*popt)

# Compute chi square
Nexp = f(mass, *popt)
r = counts - Nexp
chisq = np.sum((r/error)**2)
df = N - 3
print("chisq =",chisq, "df =",df)

plt.errorbar(mass, counts, yerr=error, fmt= 'o')
plt.show()