import numpy as np
import matplotlib.pyplot as plt

from math import *

## over damping case

# constants & initial conditions
k = 0.01 # spring constant, has to be very small
m = 1
c = 5 # damping constant high value means more resistance

omega = sqrt(k/m)
gamma = 0.5* c/m
q = sqrt(gamma**2 - omega**2)

x_0 = 1.0 # 1m pull from equilibrium
v_0 = 0.0 # 0m/s initial velocity

# function
t = np.linspace(0,1000,10000) # 0 to 1000sec increment of 0.1sec

# constant
A_1 = 0.5 * ( ( 1 + gamma/q ) * x_0 + v_0/q )
A_2 = 0.5 * ( ( 1 - gamma/q ) * x_0 - v_0/q )

# final result
x_t = A_1 * np.exp(-1 * (gamma - q) * t) + A_2 * np.exp(-1 * (gamma + q) * t)

# plt.plot(t, x_t)
# plt.show()

## critical damping
# condition --> c^2 = 4mk
c_crit = 2
gamma_crit = 0.5 * c_crit/m

A = gamma_crit * x_0 + v_0
B = x_0
x_t_2 = A * t * np.exp(-gamma_crit * t) + B * np.exp(-gamma_crit * t)

# plt.grid(True)
# plt.plot(t ,x_t , 'r' , t , x_t_2, 'b')
# plt.xlim(0,10)
# plt.show()

## under daming
k = 5.0
m = 1.0
c = 1.0

gamma = 0.5*c/m
omega = sqrt(k/m)

omega_d = sqrt(omega**2 - gamma**2)

# initial conditions
x_0 = 1.0
v_0 = 0.0

phi0 = pi/2
B_d = sqrt(x_0**2 + v_0**2 / omega**2)

# resulting fucntion
t = np.linspace(0,20,1000)

x_t_under = np.exp(-gamma * t) * B_d * np.sin(omega_d * t + phi0)
x_t_decay_plus = B_d * np.exp(-gamma * t)
x_t_decay_minus = -1.0* B_d * np. exp(-gamma * t)

plt.plot(t,x_t_under,'r',t,x_t_decay_plus,'b',linestyle = '-',t,x_t_decay_minus,'b')
plt.show()