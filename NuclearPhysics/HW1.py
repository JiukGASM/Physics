import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

# constants
V_0 = 10**(-18) # electron energy in hydrogen atom(J)
m = 9.1 * 10**(-31) # electron mass(kg)
a = 5 * 10**(-11) # bohr radius(m)
E = np.linspace(10**(-30),V_0-10**(-30),100000)
k = np.sqrt(2 * m * (V_0 - E)/constants.hbar**2)

# function
T = ((1 + (V_0**2 * (np.sinh(k*a))**2) / (4 * E * (V_0 - E))))**(-1)
plt.plot(E,T)
plt.xlabel("Energy(J)")
plt.ylabel("Transmission coefficient")
plt.show()