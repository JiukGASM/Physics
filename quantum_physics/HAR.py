import numpy as np
import matplotlib.pyplot as plt

delta_r = 0.001
r = np.arange(0, 40, delta_r)


# constant
Z = 1

a_0 = 1 # 5.29177 * 10 ** (-11) # meter, bohr radius of the ground state

R_10 = 2 * (Z / a_0) ** (1.5) * np.exp(- Z * r / a_0)

R_20 = 2 * (Z / (2 * a_0) ) ** (1.5) * (1 - (Z * (r / (2 * a_0))))  * np.exp(- Z * r / (2 * a_0) )

R_21 = (1 / 3 ** (1/2)) * (Z / (2 * a_0)) ** (3 / 2) * ( Z * r / a_0) * np.exp(- Z * r / (2 * a_0) )

R_30 = 2 * (Z / (3 * a_0)) ** 1.5 * (1 - (2 * Z * r / (3 * a_0)) + (2 * (Z * r) ** 2 / (27 * (a_0) ** 2)) ) * np.exp(- Z * r / (3 * a_0) )

R_31 = 4 * (2 ** (1/2)) / 9 * (Z / (3 * a_0)) ** 1.5 * (Z * r / a_0) * (1 - (Z * r / (6 * a_0))) * np.exp(- Z * r / (3 * a_0) )

R_32 = (2 / 27) * (2 / 5) ** (1/2) * (Z / (3 * a_0)) ** 1.5 * (Z * r / a_0) ** 2 * np.exp(- Z * r / (3 * a_0) )

def P(R):
    return r ** 2 * R ** 2

plt.subplot(313)
plt.plot(r, P(R_30) , label = 'n = 3, l = 0')
plt.plot(r, P(R_31) , color = "red" , label = 'n = 3, l = 1')
plt.plot(r, P(R_32) , color = "green" , label = 'n = 3, l = 2')
plt.legend(loc="upper right")
plt.grid(True)
plt.subplot(312)
plt.plot(r, P(R_20) , label = 'n = 2, l = 0')
plt.plot(r, P(R_21) , color = "red" , label = 'n = 2, l = 1')
plt.legend(loc="upper right")
plt.grid(True)
plt.subplot(311)
plt.plot(r, P(R_10) , label = 'n = 1, l = 0')
plt.legend(loc="upper right")
plt.grid(True)

plt.show()