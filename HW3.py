#3.  Three cases for the damping harmonic oscillator.

import numpy as np
import matplotlib.pyplot as plt
from math import *

## over damping case (q > 0 and real)

# constants & initial conditions
k = 0.1 # spring constant, has to be very small
m = 10
c = 5 # damping constant high value means more resistance

omega = sqrt(k/m)
gamma = 0.5* c/m
q = sqrt(gamma**2 - omega**2)

x_0 = 10.0 # 10m pull from equilibrium
v_0 = 0.0 # 0m/s initial velocity

# function
t = np.linspace(0,100,10000) # 0 to 100sec increment of 0.01sec

# constant
A_1 = 0.5 * ( ( 1 + gamma/q ) * x_0 + v_0/q )
A_2 = 0.5 * ( ( 1 - gamma/q ) * x_0 - v_0/q )

# final result
x_t = A_1 * np.exp(-1 * (gamma - q) * t) + A_2 * np.exp(-1 * (gamma + q) * t)







## critical damping (q = 0 and real)
# condition --> c^2 = 4mk
c_crit = sqrt(4 * m * k)
gamma_crit = 0.5 * c_crit/m

A = gamma_crit * x_0 + v_0
B = x_0
x_t_2 = A * t * np.exp(-gamma_crit * t) + B * np.exp(-gamma_crit * t)








## under daming (q is imaginary)
k_under = 0.1
m = 10
c_under = 1

gamma = 0.5*c_under/m
omega = sqrt(k_under/m)

omega_d = sqrt(omega**2 - gamma**2)

# initial conditions
x_0 = 10.0
v_0 = 0.0

phi0 = pi/2
B_d = sqrt(x_0**2 + v_0**2 / omega**2)


x_t_under = np.exp(-gamma * t) * B_d * np.sin(omega_d * t + phi0)
x_t_decay_plus = B_d * np.exp(-gamma * t)
x_t_decay_minus = -1.0* B_d * np. exp(-gamma * t)



# plot all cases
plt.grid(True)
plt.plot(t ,x_t , 'r' , t , x_t_2, 'b')
plt.plot(t,x_t_under,'g')
plt.plot(t,x_t_decay_plus,color='darkgreen',linestyle='dashed')
plt.plot(t,x_t_decay_minus,color='darkgreen',linestyle='dashed')

plt.show()
