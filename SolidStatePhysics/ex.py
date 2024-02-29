import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from numpy import linalg as LA

## HW1-3

# physical constant
a = 0.4 * 10**(-9) # lattice constant(m)
g = 2 * np.pi / a # reciprocal lattice constant(1/m)
U_1 = -0.8  # potential1(eV)
k_x_0 = np.linspace(-g,g,50)
k_y_0 = np.linspace(-g,g,50)
m = 9.1 * 10**(-31) # electron mass(kg)

def lamb(k_x,k_y) :
    return 6.242 * 10**(18) * constants.hbar**2 * (k_x**2 + k_y**2) / (2 * m) #J -> eV

B = []
B_2 = []
B_3 = []
B_4 = []
B_5 = []
# calculation of eigenvalue
for i in k_x_0:
    C = []
    C_2 = []
    C_3 = []
    C_4 = []
    C_5 = []
    for j in k_y_0:
        A = np.array([[lamb((i-g),j), U_1, 0, U_1, U_1],
                      [U_1, lamb((i+g),j), 0, U_1, U_1],
                      [U_1, U_1, lamb(i,j), U_1, U_1],
                      [U_1, U_1, 0, lamb(i,(j+g)), U_1],
                      [U_1, U_1, 0, U_1, lamb(i,(j-g))]]
                     )
        eigenvalues = LA.eigvals(A)
        C.append(eigenvalues[0])
        C_2.append(eigenvalues[1])
        C_3.append(eigenvalues[2])
        C_4.append(eigenvalues[3])
        C_5.append(eigenvalues[4])

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

k_x_0,k_y_0 = np.meshgrid(k_x_0, k_y_0)

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
'''dem3d=ax.plot_surface(k_x_0,k_y_0,B,cmap='coolwarm')
dem3d=ax.plot_surface(k_x_0,k_y_0,B_2,cmap='coolwarm')
dem3d=ax.plot_surface(k_x_0,k_y_0,B_3,cmap='coolwarm')
dem3d=ax.plot_surface(k_x_0,k_y_0,B_4,cmap='coolwarm')
dem3d=ax.plot_surface(k_x_0,k_y_0,B_5,cmap='coolwarm')'''
# dem3d=ax.scatter(k_x_0,k_y_0,B_5,c = "0.7")
dem3d=ax.scatter(k_x_0,k_y_0,B,c = "0",s = 0.1)
dem3d=ax.scatter(k_x_0,k_y_0,B_2,c = "0",s = 0.1)
dem3d=ax.scatter(k_x_0,k_y_0,B_3,c = "0",s = 0.1)
dem3d=ax.scatter(k_x_0,k_y_0,B_4,c = "0",s = 0.1)
dem3d=ax.scatter(k_x_0,k_y_0,B_5,c = "0",s = 0.1)

plt.show()

'''fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
dem3d=ax.scatter(k_x_0,k_y_0,B,marker=",",cmap='coolwarm')
plt.show()'''