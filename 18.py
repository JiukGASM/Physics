from math import *
from scipy.integrate import quad # this is for numerical integral
import numpy as np
import matplotlib.pyplot as plt

# chisquare function definition
def func (nu, y) : # nu = ndf, y = chisquare
    norm = pow(2, nu/2.0) * gamma(nu/2.0) # denominator of nomalization
    powe = np.power(y, nu/2.0 - 1) # expo. part of function
    expo = np.exp(-y/2.0) # power function part

    return (1.0/norm) * powe * expo


nu = 3 # ndf
y = np.linspace(0,10,100) # 0.1steps
f_y = func(nu,y)

plt.plot(y,f_y)
plt.show()
