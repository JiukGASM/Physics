import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import *
from math import *

# Slope(G) function
def G (t, y) :
    F[0] = -g*sin(y[1]) # -g sin(theta)
    # approximation : F[0] = - g * y[1]
    F[1] = y[0] # angular speed
    return inv_L.dot(F)

# RK4 method
def RK4 (t, y, delta_t):

    k1 = G(t, y)
    k2 = G(t + 0.5 * delta_t, y + 0.5 * delta_t * k1)
    k3 = G(t + 0.5 * delta_t, y + 0.5 * delta_t * k2)
    k4 = G(t + delta_t, y + 1.0 * delta_t * k3)

    return 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4

g = 9.8 #gravity const
l = 1.0 # lenth

omega = sqrt(g/l)

delta_t = 0.01
time = np.arange(0, 5, delta_t) # zero to 5 sec by 0.01 imcrement

theta0 = 10.0 * pi / 180 # this is radian
thetadot0 = 0 # of course this is too

y = np.array( [ thetadot0, theta0] ) # vector [angular velocity, angle]

L = np.array( [ [ l, 0.0 ], [ 0.0, 1.0 ]])
F = np.array( [ 0.0, 0.0] ) # not a force

# result
Angle = [] # angle
AS = [] # anlgular speed

inv_L = inv(L)

for t in time :
    y = y + delta_t * RK4 (t, y, delta_t)
    AS.append(y[0])
    Angle.append(y[1])

plt.plot(time, Angle)
plt.grid(True)
plt.show()

# 10도에서 실제 식과 approximation 식 비교, 60도에서 실제 식과 approximation 비교해보기