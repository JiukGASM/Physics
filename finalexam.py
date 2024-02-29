import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.integrate import  quad # this is for numerical integration
from scipy.optimize import curve_fit

#1) Draw a plot for the measurement points (mass versus experiments) with error bars on the mass.
experiments = np.array(["A","B","C","D","E","F","G","H","I"])
experiments2 = np.array([1,2,3,4,5,6,7,8,9])
mass = np.array([80478,80432,80336,80270,80415,80440,80376,80370,80433])
error  = np.array([83,79,67,55,52,51,23,19,9])

plt.errorbar(experiments, mass, yerr=error, fmt= 'o')
plt.show()

#2) Please calculate the raw counts of each measurements.

N = (mass/error) * (mass/error)
print(np.round(N))

#3) Perform a fitting with a constant function model and overlay the model best fit line with the data points.
def f(experiments, a):
    return np.zeros(N) + a

a = 10 # init. the const. function
N = 9

start = (80000) # starting position

popt,pcov = curve_fit(f,experiments2,mass,sigma = error,p0 = start, absolute_sigma=True)


perr = np.sqrt(np.sqrt(np.diag(pcov)))


fit_cpc = f(experiments,*popt)
plt.errorbar(experiments, mass, yerr=error, fmt= 'o')
plt.plot(experiments,fit_cpc)
plt.show()

#4) Please specify the parameter value with error, the chi-square value, and the p-value.

# Compute chi square
Nexp = f(experiments, *popt)
r = mass - Nexp
chisqc = np.sum((r/error)**2)
dfc = N - 1
print("chisq =",chisqc, "df =",dfc)
print("parameter value =", popt, "error =", perr)


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

print("p-value = ", I)

#5) Please validate this model using the goodness-of-fitting method and interpret the result.
print("chisquare / ndf =",chisqc/dfc)
#chisquare / ndf = 2.708269858509456 이 값이 1에서 많이 벗어나있음. 그래서 좋은 피팅이라고 보기는 어려움. p-value는 0.00557로 다시 실험을 하고 다시 피팅을 했을 때 0.5퍼센트의 확률로 chisquare의 값이 이 값보다 클 수 있음. 5sigma 수준에선 기각이 불가능하고 자연에서 충분히 일어날 수 있는 수준이지만 피팅을 다른 방법으로 다시 해볼 필요가 있다고 판단됨.

#6) Please provide the python codes for all above.

#7) Please compare the previous result with a new fitting excluding the measurement “I (blue box)” using the goodness of the fit method.



experiments = np.array(["A","B","C","D","E","F","G","H"])
experiments2 = np.array([1,2,3,4,5,6,7,8])
mass = np.array([80478,80432,80336,80270,80415,80440,80376,80370])
error  = np.array([83,79,67,55,52,51,23,19])

a = 10 # init. the const. function
N = 8

start = (80000) # starting position

popt,pcov = curve_fit(f,experiments2,mass,sigma = error,p0 = start, absolute_sigma=True)


perr = np.sqrt(np.sqrt(np.diag(pcov)))


fit_cpc = f(experiments,*popt)
plt.errorbar(experiments, mass, yerr=error, fmt= 'o')
plt.plot(experiments,fit_cpc)
plt.show()

# Compute chi square
Nexp = f(experiments, *popt)
r = mass - Nexp
chisqc = np.sum((r/error)**2)
dfc = N - 1
print("second chisq =",chisqc, "second df =",dfc)
print("second parameter value =", popt, "second error =", perr)


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

print("second p-value = ", I)

print("second chisquare / ndf =",chisqc/dfc)

#8 Interpret the answer 7)
# 1에 가까운 값임 ok 더 나아가서 p value도 0.305정도로 이 실험을 다시 진행하고 피팅했을 때 이보다 안좋을 확률이 약 30퍼센트로 충분히 일어날 수 있는 일. 괜찮은 피팅임.
