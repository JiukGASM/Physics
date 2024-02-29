import numpy as np
import matplotlib.pyplot as plt
import sys

# 2-D Ising model in which a square lattice is populated with spin-1/2 particles with Monte Carlo simulation by using Metropolis algorithm

### Simulation the 1/T dependency of Paramagnetism and animation of paramagnetism

##constants
N = 30
B = 10
g = 2
k_B = 1.380649 * 10 **(-23)
mu_B =  9.2740100783 * 10 **(-24)
n = 2000
t = range(n)

##Metropolis algorithm Procedure
Tv = np.linspace(1, 1000, 2000)
M = []
for j in Tv:
    matrix = -g * mu_B * (2 * np.random.randint(2, size=(N, N)) - 1) / 2 # magnetic moment configuration
    for i in t:
        # 3. A.
        r_index = np.random.randint(N, size=(1, 2))
        # 3. B.
        E = B * matrix[r_index[0, 0], r_index[0, 1]]
        if E <= 0:
            matrix[r_index[0, 0], r_index[0, 1]] = -1 * matrix[r_index[0, 0], r_index[0, 1]]
        else:
            P = np.exp(-E / (k_B * j))
            a = np.random.rand()
            if a < P:
                matrix[r_index[0, 0], r_index[0, 1]] = -1 * matrix[r_index[0, 0], r_index[0, 1]]
    M_tot = np.sum(matrix)
    M.append(M_tot)
chi = np.divide(M,B)

plt.plot(Tv,chi)
plt.xlabel('T[K]')
plt.ylabel('\u03C7')
plt.show()





'''## animation
#constant
T = 10

#Metropolis algorithm Procedure
matrix = -g * mu_B * (2 * np.random.randint(2, size=(N, N)) - 1) / 2
b = np.empty((N,N))
M = []
for i in t:
    # 3. A.
    r_index = np.random.randint(N, size=(1, 2))
    # 3. B.
    E = g * B * matrix[r_index[0, 0], r_index[0, 1]]
    if E < 0:
        matrix[r_index[0, 0], r_index[0, 1]] = -1 * matrix[r_index[0, 0], r_index[0, 1]]
    else:
        P = np.exp(- E / (k_B * T))
        a = np.random.rand()
        if a < P:
            matrix[r_index[0, 0], r_index[0, 1]] = -1 * matrix[r_index[0, 0], r_index[0, 1]]
    M_tot = np.sum(matrix)
    M.append(M_tot)
    b = np.dstack((b , matrix))
b = np.swapaxes(b,0,2)

#draw animation
fig, axs = plt.subplots(2, 1, layout="constrained",
                        figsize=(8, 7), facecolor='lightskyblue')

for i, img in enumerate(b):
    axs[0].clear()
    axs[0].imshow(np.transpose(img), origin='upper', vmax= mu_B, vmin=-mu_B, cmap='GnBu')
    axs[1].plot(i,M[i], marker='o', color='lightskyblue')
    axs[0].set_title(f"frame {i}")
    plt.pause(0.001)
axs.set_aspect(0.001)

#save as gif
ani = animation.FuncAnimation(fig, update, len(b), interval=1)
ani.save('/Users/leejiuk1/Documents/CAU/LectureInCAU/4th/Solid-state Physics/HW/HW3/para1.gif', writer='imagemagick', fps=25)'''

