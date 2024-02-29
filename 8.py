import numpy as np
from numpy.linalg import inv
from math import *
import matplotlib.pyplot as plt

m = 2.0 # 2kg, mass
k = 2.0 # spring const

omega = sqrt(k/m) # omega

c = 0.0
F_0 = 0.0 # driving force

delta_t = 0.01
time = np.arange(0, 40, delta_t) # time from 0 to 40sec. by 4000sample

# init condition
x_0 = 1.0
v_0 = 0.0

#state representation
y = np.array( [v_0, x_0] ).T

A = np.array()

