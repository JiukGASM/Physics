import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from numpy import linalg as LA

## HW1-1

# physical constant
a = 0.4 * 10**(-9) # lattice constant(m)
g = 2 * np.pi / a # reciprocal lattice constant(1/m)
U_1 = -0.8  # potential1(eV)
U_2 = -0.25  # potential2(eV)
k_0 = np.linspace(-g / 2,g / 2,100000)
m = 9.1 * 10**(-31) # electron mass(kg)
def lamb(k) :
    return 6.242 * 10**(18) * constants.hbar**2 * k**2 / (2 * m) #J -> eV

B = []
B_2 = []
B_3 = []
B_4 = []
B_5 = []

# calculation of eigenvalue
for i in k_0:
    A = np.array([[lamb(i - 2 * g), U_1, U_2, 0, 0],
                  [U_1, lamb(i - g), U_1, U_2, 0],
                  [U_2, U_1, lamb(i), U_1, U_2],
                  [0, U_2, U_1, lamb(i + g), U_1],
                  [0, 0, U_2, U_1, lamb(i + 2 * g)]]
                 ) # 5 by 5
    '''A =  np.array([
                  [lamb(i - g), U_1, U_2],
                  [U_1, lamb(i), U_1],
                  [U_2, U_1, lamb(i + g)],
                  ]
                 )''' # 3 by 3
    eigenvalues = LA.eigvals(A)
    B.append(max(eigenvalues))
    B_2.append(np.partition(eigenvalues.flatten(), -2)[-2])
    B_3.append(np.partition(eigenvalues.flatten(), -3)[-3])
    B_4.append(np.partition(eigenvalues.flatten(), -4)[-4])
    B_5.append(min(eigenvalues))

# bandgap
gap_1 = min(B_4) - max(B_5)
gap_2 = min(B_3) - max(B_4)
print(gap_1)
print(gap_2)


# plot
plt.plot(k_0,B, color = '0',linewidth=0.5)
plt.plot(k_0,B_2, color = '0',linewidth=0.5)
plt.plot(k_0,B_3, color = '0',linewidth=0.5)
plt.plot(k_0,B_4, color = '0',linewidth=0.5)
plt.plot(k_0,B_5, color = '0',linewidth=0.5)
plt.ylim(-0.2,50)
plt.xlabel('k(1/m)')
plt.ylabel('E(eV)')
plt.show()



## HW 1-2

# physical constant
alpha = -(max(B_5) + min(B_5)) / 2 # on-site energy(eV)
gamma =  (max(B_5) - min(B_5))/ 4 # interaction energy(eV)
print(alpha)
print(gamma)

# dispersion
e_k = - alpha - 2 * gamma * (np.cos(k_0 * a))

# plot
plt.plot(k_0,e_k, color = '0',linewidth=0.5)
plt.ylim(-0.2,50)
plt.xlabel('k(1/m)')
plt.ylabel('E(eV)')
plt.show()
