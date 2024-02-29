import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 2-D Ising model in which a square lattice is populated with spin-1/2 particles with Monte Carlo simulation by using Metropolis algorithm

### Simulation the temperature dependency of magnetization for a ferromagnet(antiferromagent) and animation of this system

##constants
N = 30
g = 2
k_B = 1.380649 * 10 **(-23)
mu_B =  9.2740100783 * 10 **(-24)
J = -10**(-2) * 1.60218 * 10 ** (-19)
n = 4000
t = range(n)

##Metropolis algorithm Procedure
Tv = np.linspace(0.001, 50, 1000)
M = []
for j in Tv:
    Sp = -np.ones((N, N)) / 2
    matrix = -g * mu_B * Sp
    for i in t:
        # 3. A.
        r_index = np.random.randint(N, size=(1, 2))
        # 3. B.
        E = 0
        if r_index[0, 0] < N - 1 and r_index[0, 1] < N - 1 and r_index[0, 0] > 0 and r_index[0, 1] > 0:
            E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == N - 1 and r_index[0, 1] < N - 1 and r_index[0, 1] > 0:
            E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] < N - 1 and r_index[0, 1] == 0 and r_index[0, 0] > 0:
            E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N - 1])
        elif r_index[0, 0] == 0 and r_index[0, 1] < N - 1 and r_index[0, 1] > 0:
            E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] < N - 1 and r_index[0, 1] == N - 1 and r_index[0, 0] > 0:
            E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == N - 1 and r_index[0, 1] == 0:
            E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N - 1])
        elif r_index[0, 0] == N - 1 and r_index[0, 1] == N - 1:
            E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == 0 and r_index[0, 1] == N - 1:
            E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == 0 and r_index[0, 1] == 0:
            E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N - 1])


        if E <= 0:
            Sp[r_index[0, 0], r_index[0, 1]] = -1 * Sp[r_index[0, 0], r_index[0, 1]]
        else:
            P = np.exp(-E / (k_B * j))
            a = np.random.rand()
            if a < P:
                Sp[r_index[0, 0], r_index[0, 1]] = -1 * Sp[r_index[0, 0], r_index[0, 1]]
        matrix = -g * mu_B * Sp

    M_tot = np.sum(matrix)
    M.append(M_tot)

plt.plot(Tv,M)
plt.xlabel('T[K]')
plt.ylabel('\u03C7')
plt.show()


'''## animation
#constant
T = 0.001

#Metropolis algorithm Procedure
Sp = -np.ones((N, N)) / 2
matrix = -g * mu_B * Sp
b = np.empty((N,N))
M = []
for i in t:
    # 3. A.
    r_index = np.random.randint(N, size=(1, 2))
    # 3. B.
    E = 0

    if r_index[0, 0] < N - 1 and r_index[0, 1] < N - 1 and r_index[0, 0] > 0 and r_index[0, 1] > 0:
        E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
    elif r_index[0, 0] == N - 1 and r_index[0, 1] < N-1  and r_index[0, 1] > 0:
        E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
    elif r_index[0, 0] < N - 1 and r_index[0, 1] == 0 and r_index[0, 0] > 0 :
        E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N-1])
    elif r_index[0, 0] == 0 and r_index[0, 1] < N - 1 and r_index[0, 1] > 0:
        E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N-1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
    elif r_index[0, 0] < N - 1 and r_index[0, 1] == N - 1 and r_index[0, 0] > 0:
        E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
    elif r_index[0, 0] == N - 1 and r_index[0, 1] == 0 :
        E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0],N-1])
    elif r_index[0, 0] == N - 1 and r_index[0, 1] == N - 1 :
        E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
    elif r_index[0, 0] == 0 and r_index[0, 1] == N - 1 :
        E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N-1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
    elif r_index[0, 0] == 0 and r_index[0, 1] == 0 :
        E += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N-1, r_index[0, 1]]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                        + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N-1])


    if E < 0:
        Sp[r_index[0, 0], r_index[0, 1]] = -1 * Sp[r_index[0, 0], r_index[0, 1]]
    else:
        P = np.exp(- E / (k_B * T))
        a = np.random.rand()
        if a < P:
            Sp[r_index[0, 0], r_index[0, 1]] = -1 * Sp[r_index[0, 0], r_index[0, 1]]
    matrix = -g * mu_B * Sp
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
axs.set_aspect(0.001)'''

