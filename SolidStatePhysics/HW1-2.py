import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from numpy import linalg as LA

## HW1-3

# physical constant
a = 0.4 * 10**(-9) # lattice constant(m)
g = 2 * np.pi / a # reciprocal lattice constant(1/m)
U_1 = -0.8  # potential1(eV)
k_x_0 = np.linspace(-g / 2, g / 2, 1000)
k_y_0 = np.linspace(-g / 2, g / 2, 1000)
m = 9.1 * 10**(-31) # electron mass(kg)

def lamb(k_x,k_y) :
    return 6.242 * 10**(18) * constants.hbar**2 * (k_x**2 + k_y**2) / (2 * m) #J -> eV

# calculation of eigenvalue

B = []
B_2 = []
B_3 = []
B_4 = []
B_5 = []

for i in k_x_0:
    C = []
    C_2 = []
    C_3 = []
    C_4 = []
    C_5 = []
    for j in k_y_0:
        A = np.array([[lamb((i-g),j), 0, U_1, 0, 0],
                      [0, lamb((i+g),j), U_1, 0, 0],
                      [U_1, U_1, lamb(i,j), U_1, U_1],
                      [0, 0, U_1, lamb(i,(j+g)), 0],
                      [0, 0, 0, U_1, lamb(i,(j-g))]]
                     )
        eigenvalues = LA.eigvals(A)
        C.append(max(eigenvalues))
        C_2.append(np.partition(eigenvalues.flatten(), -2)[-2])
        C_3.append(np.partition(eigenvalues.flatten(), -3)[-3])
        C_4.append(np.partition(eigenvalues.flatten(), -4)[-4])
        C_5.append(min(eigenvalues))

    B.append(C)
    B_2.append(C_2)
    B_3.append(C_3)
    B_4.append(C_4)
    B_5.append(C_5)


B = np.array(B)
B_2 = np.array(B_2)
B_3 = np.array(B_3)
B_4 = np.array(B_4)
B_5 = np.array(B_5)


# plot
k_x_0,k_y_0 = np.meshgrid(k_x_0, k_y_0)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
dem3d=ax.plot_surface(k_x_0,k_y_0,B,cmap='viridis')
dem3d=ax.plot_surface(k_x_0,k_y_0,B_2,cmap='viridis')
dem3d=ax.plot_surface(k_x_0,k_y_0,B_3,cmap='viridis')
dem3d=ax.plot_surface(k_x_0,k_y_0,B_4,cmap='viridis')
dem3d=ax.plot_surface(k_x_0,k_y_0,B_5,cmap='viridis')
ax.set_xlabel('k_x(1/m)')
ax.set_ylabel('k_y(1/m)')
ax.set_zlabel('E(eV)')
ax.set_zlim(-1,5)
plt.show()


## HW 1-4

# physical constant
alpha = - (max(np.maximum.reduce(B_5)) + min(np.minimum.reduce(B_5))) / 2 # on-site energy(eV)
gamma = (max(np.maximum.reduce(B_5)) - min(np.minimum.reduce(B_5))) / 8 # interaction energy(eV)
print(alpha)
print(gamma)

# dispersion
e_k = -alpha -2 * gamma * (np.cos(k_x_0 * a) + np.cos(k_y_0 * a))

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
dem3d=ax.plot_surface(k_x_0,k_y_0,e_k,cmap='viridis')
ax.set_xlabel('k_x(1/m)')
ax.set_ylabel('k_y(1/m)')
ax.set_zlabel('E(eV)')
ax.set_zlim(-1,5)
plt.show()