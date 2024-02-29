#1. Find a resonance solution using the 4th-order Runge-Kutta method
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from math import *

## 4th order Runge-Kutta
m = 1 # 1kg, mass
k = 1 # spring const
c = 0.0 # damping term

omega = sqrt(k/m) # omega_0
omega_force = sqrt(omega**2 -2.0 * ((c/(2.0 *m))**2)) # omega of driving force (resonance frequency)
F0 = 0.1# driving force

delta_t = 0.001
time = np.arange(0, 100, delta_t) # time from 0 to 100 sec.

# init condition
x0 = 0.0
v0 = 0.0

# state representation
y = np.array( [v0, x0]) # vector [velocity, position] --> y[0] = velocity, y[1]=position

A = np.array( [ [m, 0.0] ,[0.0, 1.0] ] ) # 2x2 matrix
B = np.array( [ [c, k ],[-1.0, 0.0] ] ) # 2x2 matrix

F = np.array( [0.0, 0.0] ) #no initial driving force

# result
YY = [] #result position
VV = [] # result velocity
FF = [] # result force

invers_A = inv(A)

def ZZ (t, y) :
    F[0] = F0 * np.cos(omega_force * t)
    return invers_A.dot (F - B.dot( y ))

def RK4 (t, y, delta_t):

    k1 = ZZ(t, y)
    k2 = ZZ(t + 0.5 * delta_t, y + 0.5 * delta_t * k1)
    k3 = ZZ(t + 0.5 * delta_t, y + 0.5 * delta_t * k2)
    k4 = ZZ(t + delta_t, y + 1.0 * delta_t * k3)

    return 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4



# time steps
for t in time :
    y = y + delta_t * RK4(t, y, delta_t)

    YY.append(y[1])
    VV.append(y[0])
    FF.append(F[0])

plt.plot(time, FF,'r' ,time, YY,'b')
plt.grid(True)
plt.show()
