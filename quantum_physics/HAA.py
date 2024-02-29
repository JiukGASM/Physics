import numpy as np
import matplotlib.pyplot as plt

delta_theta = 0.001
theta = np.arange(0, 2 * np.pi , delta_theta)


Y_00 = 1 / (4 * np.pi) ** 0.5

Y_11 = - ( 3 / ( 8 * np.pi ) ) ** 0.5 * np.sin(theta)

Y_10 = ( 3 / ( 4 * np.pi ) ) ** 0.5 * np.cos(theta)

Y_22 = (15 / (32 * np.pi) ) ** 0.5 * np.sin(theta) ** 2

Y_21 = - ( 15 / ( 8 * np.pi ) ) ** 0.5 * np.cos(theta) * np.sin(theta)

Y_20 = ( 5 / ( 16 * np.pi ) ) ** 0.5 * ( 3 * np.cos(theta) ** 2 - 1)



def P(Y):
    return Y ** 2

plt.figure(figsize=(7,7))
plt.subplot(321)
plt.plot(P(Y_00) * np.sin(theta), P(Y_00) * np.cos(theta) , label = 'l = 0, m = 0')
plt.legend(loc="upper right")
plt.grid(True)
plt.axis('equal')
plt.subplot(322)
plt.plot(P(Y_11) * np.sin(theta), P(Y_11) * np.cos(theta) , color = "red" , label = 'l = 1, m = 1')
plt.legend(loc="upper right")
plt.grid(True)
plt.axis('equal')
plt.subplot(323)
plt.plot(P(Y_10) * np.sin(theta), P(Y_10) * np.cos(theta) , color = "blue" , label = 'l = 1, m = 0')
plt.legend(loc="upper right")
plt.grid(True)
plt.axis('equal')
plt.subplot(324)
plt.plot(P(Y_22) * np.sin(theta), P(Y_22) * np.cos(theta) , color = "green" , label = 'l = 2, m = 2')
plt.legend(loc="upper right")
plt.grid(True)
plt.axis('equal')
plt.subplot(325)
plt.plot(P(Y_21) * np.sin(theta), P(Y_21) * np.cos(theta) , color = "orange" , label = 'l = 2, m = 1')
plt.legend(loc="upper right")
plt.grid(True)
plt.axis('equal')
plt.subplot(326)
plt.plot(P(Y_20) * np.sin(theta), P(Y_20) * np.cos(theta) , color = "black" , label = 'l = 2, m = 0')
plt.legend(loc="upper right")
plt.grid(True)
plt.axis('equal')


plt.show()