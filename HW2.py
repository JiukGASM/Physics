#2.  Simple Harmonic Oscillator

import numpy as np
import matplotlib.pyplot as plt
from math import *

# consts & initial conditions
m = 1 # mass 1kg
k = 1 # spring const. 1
omega = sqrt(k/m) # freq.
x0 = 1 # init. position
v0 = 1 # init. velocity

B = sqrt(x0*x0 + v0*v0/omega/omega) # another const
phi = atan(x0*omega/v0)

# function
t = np.linspace(0,20,100) # time
x_t = x0 * np.cos(omega * t) + v0/omega * np.sin(omega * t) # solution
x_t_dot = -x0 * omega * np.sin(omega * t) + v0 * np.cos(omega * t) # velocity

y_t = B * np.sin(omega*t + phi)


E = 0.5 * m * x_t_dot * x_t_dot + 0.5 * k * x_t * x_t #total energy

plt.subplot(311)
plt.plot(t, x_t, "r")
plt.subplot(312)
plt.plot(t, y_t, "b-")
plt.subplot(313)
plt.plot(t, E)
plt.show()