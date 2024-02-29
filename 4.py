import numpy as np
import matplotlib.pyplot as plt
# # t = np.arange(-1,1,0.02)
# t = np.linspace(-10,10,100) # 3rd argument = number of sample
# y = np.exp(t)
# plt.figure()
# # plt.plot(t,y)
# # plt.show()
# z = np.sin(t)*np.sin(t)*np.sin(t)
# plt.plot(t,z,"red") # 3rd argument is option
# plt.show()

# t1 = np.arange(-1,1,0.5)
# y1 = np.exp(t1)
# t2 = np.arange(-1,1,0.2)
# y2 = np.exp(t2)
# t3 = np.arange(-1,1,0.1)
# y3 = np.exp(t3)
# plt.figure()
# plt.subplot(131) #subplot 1by3,1
# plt.plot(t1,y1)
# plt.subplot(132) #subplot 1by3,2
# plt.plot(t2,y2)
# plt.subplot(133) #subplot 1by3,3
# plt.plot(t3,y3)
#
# plt.show()

x = np.arange(-10,10,0.05)
y0 = x * 0.0 + 1#1
y1 = x * 1 # x
z = 1 + x
plt.subplot(311)
plt.grid(True)
plt.plot(x,y0)
plt.subplot(312)
plt.grid(True)
plt.plot(x,y1)
plt.subplot(313)
plt.grid(True)
plt.plot(x,z)

plt.show()

