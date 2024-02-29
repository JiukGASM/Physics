import numpy as np
import matplotlib.pyplot as plt

''''# variables
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
plt.show()'''

from numpy.linalg import inv # linear algebra
from math import *

# variables
m = 2.0
k = 2.0

c = 0.0 # no damping
F_0 = 0.0 # no driving force F = F0 * cos (omega * t)

delta_t = 0.0001 # time step
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