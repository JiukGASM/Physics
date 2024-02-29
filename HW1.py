# 1.   Taylor series e.g. y(x) = exp(x)
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,0.02)
z = 1 + x + 0.5*x*x + 1/6*x*x*x + 1/24 * x ** 4 # 4차항까지 taylor expansion approx.
z2 = 1 + x + 0.5*x*x + 1/6*x*x*x # 3차항까지 taylor expansion approx.
z3 = 1 + x + 0.5*x*x # 2차항까지 taylor expansion approx.
y2 = np.exp(x) # actual expo function

plt.subplot(311) #subplot 1by3,1
plt.plot(x, z, "r",x,y2,"b--")
plt.axis([-2.5,2.5,-5,5])
plt.subplot(312) #subplot 1by3,2
plt.plot(x, z2, "r",x,y2,"b--")
plt.axis([-2.5,2.5,-5,5])
plt.subplot(313) #subplot 1by3,3
plt.plot(x, z3, "r",x,y2,"b--")
plt.axis([-2.5,2.5,-5,5])
plt.show()
