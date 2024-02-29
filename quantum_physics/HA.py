import numpy as np
import matplotlib.pyplot as plt


lim = 8
num = 300000

z = (np.random.rand(num) - 0.5) * 2 * lim
y = (np.random.rand(num) - 0.5) * 2 * lim
x = (np.random.rand(num) - 0.5) * 2 * lim


r = (x**2 + y**2 + z**2)**(1/2)
theta = np.arccos(z / r)
# constant
Z = 1
a_0 = 1 #5.29177 * 10 ** (-11) # meter, bohr radius of the ground state

#function

#(1,0,0)
R_10 = 2 * (Z / a_0) ** (1.5) * np.exp(- Z * r / a_0) #nl
Y_00 = 1 / (4 * np.pi) ** 0.5 #lm
U_100 = ( R_10 * Y_00 ) ** 2
#(2,0,0)
R_20 = 2 * (Z / (2 * a_0) ) ** (1.5) * (1 - (Z * (r / (2 * a_0))))  * np.exp(- Z * r / (2 * a_0) )
U_200 = ( R_20 * Y_00 ) ** 2
#(2,1,0)
R_21 = (1 / 3 ** (1/2)) * (Z / (2 * a_0)) ** (3 / 2) * ( Z * r / a_0) * np.exp(- Z * r / (2 * a_0) )
Y_10 = ( 3 / ( 4 * np.pi ) ) ** 0.5 * np.cos(theta)
U_210 = ( R_21 * Y_10 ) ** 2
#(2,1,1)
R_21 = (1 / 3 ** (1/2)) * (Z / (2 * a_0)) ** (3 / 2) * ( Z * r / a_0) * np.exp(- Z * r / (2 * a_0) )
Y_11 = - ( 3 / ( 8 * np.pi ) ) ** 0.5 * np.sin(theta)
U_211 = ( R_21 * Y_11 ) ** 2
#(3,0,0)
R_30 = 2 * (Z / (3 * a_0)) ** 1.5 * (1 - (2 * Z * r / (3 * a_0)) + (2 * (Z * r) ** 2 / (27 * (a_0) ** 2)) ) * np.exp(- Z * r / (3 * a_0) )
U_300 = ( R_30 * Y_00 ) ** 2
#(3,1,0)
R_31 = 4 * (2 ** (1/2)) / 9 * (Z / (3 * a_0)) ** 1.5 * (Z * r / a_0) * (1 - (Z * r / (6 * a_0))) * np.exp(- Z * r / (3 * a_0) )
Y_10 = ( 3 / ( 4 * np.pi ) ) ** 0.5 * np.cos(theta)
U_310 = ( R_31 * Y_10 ) ** 2
#(3,1,1)
R_31 = 4 * (2 ** (1/2)) / 9 * (Z / (3 * a_0)) ** 1.5 * (Z * r / a_0) * (1 - (Z * r / (6 * a_0))) * np.exp(- Z * r / (3 * a_0) )
Y_11 = - ( 3 / ( 8 * np.pi ) ) ** 0.5 * np.sin(theta)
U_311 = ( R_31 * Y_11 ) ** 2
#(3,2,0)
R_32 = (2 / 27) * (2 / 5) ** (1/2) * (Z / (3 * a_0)) ** 1.5 * (Z * r / a_0) ** 2 * np.exp(- Z * r / (3 * a_0) )
Y_20 = Y_20 = ( 5 / ( 16 * np.pi ) ) ** 0.5 * ( 3 * np.cos(theta) ** 2 - 1)
U_320 = ( R_32 * Y_20 ) ** 2
#(3,2,1)
R_32 = (2 / 27) * (2 / 5) ** (1/2) * (Z / (3 * a_0)) ** 1.5 * (Z * r / a_0) ** 2 * np.exp(- Z * r / (3 * a_0) )
Y_21 = - ( 15 / ( 8 * np.pi ) ) ** 0.5 * np.cos(theta) * np.sin(theta)
U_321 = ( R_32 * Y_21 ) ** 2
#(3,2,2)
R_32 = (2 / 27) * (2 / 5) ** (1/2) * (Z / (3 * a_0)) ** 1.5 * (Z * r / a_0) ** 2 * np.exp(- Z * r / (3 * a_0) )
Y_22 = (15 / (32 * np.pi) ) ** 0.5 * np.sin(theta) ** 2
U_322 = ( R_32 * Y_22 ) ** 2

#drawing
fig = plt.figure(figsize=(10,8))
ax = plt.axes(projection="3d")
ax.scatter3D(x, y, z, c = U_321, alpha=0.3, marker=',', s = 0.1, cmap='nipy_spectral', label='l=3,m=2,n=1')
plt.legend(loc="upper right")
plt.show()
