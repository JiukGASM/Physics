import numpy as np
import matplotlib.pyplot as plt

def f(mass,a):
    return np.zeros(4) + a

counts = np.array([7,9,12,10]) #data
errors = np.sqrt(counts)
mass   = np.array([0.5,1.5,2.5,3.5])

print("Data =", counts)
print("Error on the data =", errors)
print("X axis =",mass)

a = 0
Mu = np.zeros(4) + a #model

from scipy.optimize import curve_fit

popt, pcov = curve_fit(f, mass, counts, sigma = errors, p0 = 1, absolute_sigma=True)
print("results = ", popt)
print("results = ", pcov) #분산 covariance

perr = np.sqrt(np.diag(pcov))
print("uncertantiy = ",perr)

## linear
# def f(mass, a, b):
#     return np.zeros(4) + a * mass + b
#
# a = 0
# b = 0
#
# start = [1,1]
# popt, pcov = curve_fit(f, mass, counts, sigma = errors, p0 = start, absolute_sigma=True)
# print("results = ", popt)
# print("results = ", pcov) #분산 covariance
#
# perr = np.sqrt(np.diag(pcov))
# print("uncertantiy = ",perr)
# 1.23 ( +- 1.31)x + 6.9(+-2.8)

## minimum chi-squar value

Nexp = f(mass, *popt) #* 의미: popt가 숫자 1개면 1개, 숫자 2개면 2개 넣음 # 9.147 9.147 9.147 9.147
r = counts - Nexp # result function, mu = a line, mu = 9.147 # numerator of chi-squre
chisq = np.sum((r/errors)**2)
print("Minium chi-square = ",chisq)

plt.errorbar(mass,counts, yerr = errors,fmt='o') #data point drawing
plt.plot(mass,Nexp) # line of model drawing
plt.show()


## chi^2/NDF 가 1 근처면 좋아 1차함수로 할지 2차함수로 할지 이걸로 결정 ok 만약 1보다 너무 작으면 문제가 있는거야 에러를 잘못 넣었거나..
#에러바를 68개만 지나가는게 정상인데 거의다 지나감 17P