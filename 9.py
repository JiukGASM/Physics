import numpy as np
from numpy.linalg import *
from math import *
import matplotlib.pyplot as plt

m = 2.0 # 2kg, mass
k = 20.0 # spring const

omega = sqrt(k/m) # omega

c = 1.0
F0 = sqrt(omega**2 -2.0 * ((c/(2.0 *m))**2))# driving force

delta_t = 0.001
time = np.arange(0, 40, delta_t) # time from 0 to 40 sec. by 4000 sample

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


invers_A = inv(A)

def ZZ (t, y) :
    F[0] = F0 * np.cos(omega * t)
    return invers_A.dot (F - B.dot( y ))

def RK4 (t, y, delta_t):

    k1 = ZZ(t, y)
    k2 = ZZ(t + 0.5 * delta_t, y + 0.5 * delta_t * k1)
    k3 = ZZ(t + 0.5 * delta_t, y + 0.5 * delta_t * k2)
    k4 = ZZ(t + delta_t, y + 1.0 * delta_t * k3)

    return 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4
    # return k1 # RK1



# time steps
for t in time :
    # F[0] = F0*np.cos(omega*t) # driving force

    # F[0] = F0 * np.cos(omega * t)
    # k1 = invers_A.dot (F - B.dot( y ))
    #
    # F[0] = F0 * np.cos(omega * (t + 0.5 * delta_t))
    # k2 = invers_A.dot (F - B.dot(y + 0.5 * delta_t * k1))
    #
    # F[0] = F0 * np.cos(omega * (t + 0.5 * delta_t))
    # k3 = invers_A.dot(F - B.dot(y + 0.5 * delta_t * k2))
    #
    # F[0] = F0 * np.cos(omega * (t + delta_t))
    # k4 = invers_A.dot(F - B.dot(y + 1.0 * delta_t * k3))
    #
    # G = 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4

    # y = y + delta_t * G
    y = y + delta_t * RK4(t, y, delta_t)

    YY.append(y[1])
    VV.append(y[0])

plt.plot(time, VV,'r' ,time, YY,'b')
plt.grid(True)
plt.show()




