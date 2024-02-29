# 4.  1st order Runge-Kutta and 4th order Runge-Kutta

## 1st order Runge-Kutta
import numpy as np
import matplotlib.pyplot as plt

#non-matrix method
# variables
m = 2.0
k = 2.0

# x-axis
delta_t = 0.01 # time step
time = np.arange(0.0, 40.0, delta_t)

# initial condition
x_0, v_0 = 1.0, 0.0

# states
x,v = x_0, v_0

# result list
Y = [] # list of positions each time interval
V = []
# time-steps
for t in time :
    v = v + delta_t * (-k/m)*x
    x = x + delta_t * v
    Y.append(x)
    V.append(v)

# plot the results
plt.grid(True)
plt.plot(time,Y,'r',time,V)
plt.show()



# using matrix method
from numpy.linalg import inv # linear algebra
from math import *

# variables
m = 2.0
k = 2.0

c = 0.0 # no damping
F_0 = 0.0 # no driving force F = F0 * cos (omega * t)

delta_t = 0.001 # time step
time = np.arange(0.0, 40.0, delta_t)


# initial condition
x_0 = 1.0
v_0 = 0.0

# initial state
y = np.array([ v_0 , x_0]).T # vector [ velocity, position]

A = np.array([[m,0.0],
              [0.0, 1.0]])

B = np.array([[c,k],
              [-1.0,0.0]])

F = np.array(([0.0,0.0])).T

# result list
Y = [] # list of positions each time interval
V = [] # list of speed each time interval
# time-steps aka RK-1 method
for t in time :
    y = y + delta_t * inv(A).dot( F - B.dot(y))
    Y.append(y[1])
    V.append(y[0])

plt.grid(True)
plt.plot(time,Y,'r',time,V,'b')
plt.show()





## 4th order Runge-Kutta
m = 1 # 1kg, mass
k = 1 # spring const

omega = sqrt(k/m) # omega_0
omega_force = sqrt(omega**2 -2.0 * ((c/(2.0 *m))**2)) # omega of driving force (resonance frequency)
c = 0.00 # no damping term
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



## 1st order Runge-Kutta vs 4st order Runge-Kutta

m = 2.0 # 2kg, mass
k = 20.0 # spring const

omega = sqrt(k/m) # omega

c = 1.0
F0 = 1.0# driving force

delta_t = 0.01
time = np.arange(0, 40, delta_t) # time from 0 to 40 sec. by 4000 sample

# init condition
x0 = 0.0
v0 = 0.0

# state representation
y4 = np.array( [v0, x0]) # vector [velocity, position] --> y[0] = velocity, y[1]=position
y1 = np.array( [v0, x0])

A = np.array( [ [m, 0.0] ,[0.0, 1.0] ] ) # 2x2 matrix
B = np.array( [ [c, k ],[-1.0, 0.0] ] ) # 2x2 matrix

F = np.array( [0.0, 0.0] ) #no initial driving force

# result
YY = [] #result position of 4th
Y = [] #result position of 1th


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

def RK1 (t, y, delta_t):
    k1 = ZZ(t, y)
    return k1 # RK1

# time steps
for t in time :
    y4 = y4 + delta_t * RK4(t, y4, delta_t)
    y1 = y1 + delta_t * RK1(t, y1, delta_t)

    YY.append(y4[1])
    Y.append((y1[1]))

plt.plot(time, Y,'r' ,time, YY,'b')
plt.grid(True)
plt.show()

