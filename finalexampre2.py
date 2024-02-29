#(1) Provide means and sigmas of two distributions.
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

## Gaussian Fit Example
def gaus(x, *p):
    A, mu, sigma = p
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))

scores = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50])
nums = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,10,13,11,17,14,15,5,2,2,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
nums2 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,2,2,9,8,12,14,11,17,6,6,2,4,2,1,1,0,0,0,0,0,0])
start = (15,19,2)

popt,pcov = curve_fit(gaus,scores,nums,p0 = start,absolute_sigma=True)
start = (15,35,2)
popt2,pcov2 = curve_fit(gaus,scores,nums2,p0 = start,absolute_sigma=True)

print(popt)
print(popt2)

fit_cp1 = gaus(scores,*popt)
fit_cp2 = gaus(scores,*popt2)
plt.plot(scores,nums,'o')
plt.plot(scores,fit_cp1)
plt.show()

plt.plot(scores,nums2,'o')
plt.plot(scores,fit_cp2)
plt.show()