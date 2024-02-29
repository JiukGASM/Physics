import numpy as np
import matplotlib.pyplot as plt
from math import sqrt , atan

# x = np.arange(-10,10,0.02)
# z = 1 + x + 0.5*x*x + 1/6*x*x*x + 1/24 * x ** 4 # taylor expansion approx.
# y2 = np.exp(x) # actual expo function
# plt.axis([-2.5,2.5,-5,5])
# plt.plot(x, z, "r",x,y2,"b--")
# plt.show()

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


E = 0.5 * m * x_t_dot * x_t_dot + 0.5 * k * x_t * x_t

# plt.plot(t, x_t, "r")
# plt.plot(t, y_t, "b-")
plt.plot(t, E)
plt.show()