import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.integrate import  quad # this is for numerical integration

# 1) Draw a plot for the data points (N infected versus Nth day) with error bars on the number of the infected.
day = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
counts = np.array([575,626,575,566,532,574,579,577,633,524,553,561,588,535,491,538,495,537,528,533,543,505,508,494,480])
error  = np.sqrt(counts)

plt.errorbar(day, counts, yerr=error, fmt= 'o')
plt.show()

#2) Perform a fitting with (a) a constant function model and (b) a linear function model separately. (b) could be a quadratic function model instead or your own model choice is okay.

# const
from scipy.optimize import curve_fit

def f(day, a):
    return np.zeros(N) + a

a = 10 # init. the const. function
N = 25

A = f(day, a)

print(A)

start = (10) # starting position

popt,pcov = curve_fit(f,day,counts,sigma = error,p0 = start, absolute_sigma=True)
print(popt)
print(pcov)

perr = np.sqrt(np.sqrt(np.diag(pcov)))
print(perr)
print(*popt)

fit_cpc = f(day,*popt)

# Compute chi square
Nexp = f(day, *popt)
r = counts - Nexp
chisqc = np.sum((r/error)**2)
dfc = N - 1
print("chisq =",chisqc, "df =",dfc)
print(chisqc/dfc)


# linear


def f1(day, a, b):
    return np.zeros(N) + a*day + b

a = 10 # init. the const. function
b = 1 # y-intersect
N = 25

A = f1(day, a, b)

start = (10,1) # starting position

popt,pcov = curve_fit(f1,day,counts,sigma = error,p0 = start, absolute_sigma=True)
print(popt)
print(pcov)

perr = np.sqrt(np.sqrt(np.diag(pcov)))
print(perr)
print(*popt)

fit_cpl = f1(day,*popt)

# Compute chi square
Nexp = f1(day, *popt)
r = counts - Nexp
chisql = np.sum((r/error)**2)
dfl = N - 2
print("chisq =",chisql, "df =",dfl)
print(chisql/dfl)

#3) Please overlay the model best fit lines with the data points.
#4) For each model, please specify parameter values with errors, chi-square values, and p-values.

plt.errorbar(day, counts, yerr=error, fmt= 'o')
plt.plot(day,fit_cpc)
plt.plot(day,fit_cpl)
plt.show()


## integral

# chisquare function definition
def func (x, nu) :
    norm = pow(2, nu/2.0) * gamma(nu/2.0)
    powe = pow(x, nu/2.0-1)
    expo = exp(-x/2.0)
    return (1.0/norm) * powe * expo

# first case
nu = dfc # ndf
minchisquare = chisqc
#numerical integral
I = quad(func, minchisquare, +inf, args = (nu))

print("Ingeral = ", I)

# second case
nu = dfl # ndf
minchisquare = chisql
#numerical integral
I = quad(func, minchisquare, +inf, args = (nu))

print("Ingeral = ", I)

