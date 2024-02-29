import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 2-D Ising model in which a square lattice is populated with spin-1/2 particles with Monte Carlo simulation by using Metropolis algorithm

### Simulation the hysteresis loop for a ferromagnet(antiferromagnet) with paramagnetism and animation of this system

##constants
N = 30
g = 2
k_B = 1.380649 * 10 **(-23)
mu_B =  9.2740100783 * 10 **(-24)
T = 50
J = -10**(-2) * 1.60218 * 10 ** (-19)
n = 4000
t = range(n)

##Metropolis algorithm Procedure
Bv = np.linspace(0, 80, 100)
Bv = np.concatenate([Bv, 80-np.linspace(0, 80, 100)],0)
Bv = np.concatenate([Bv, -np.linspace(0, 80, 100)],0)
Bv = np.concatenate([Bv, np.linspace(0, 80, 100) - 80],0)
Bv = np.concatenate([Bv, np.linspace(0, 80, 100)],0)
M = []
Sp = (2 * np.random.randint(2, size=(N, N)) - 1) / 2
matrix = -g * mu_B * Sp
for j in Bv:
    for i in t:
        # 3. A.
        r_index = np.random.randint(N, size=(1, 2))
        # 3. B.
        E_1 = 0
        if r_index[0, 0] < N - 1 and r_index[0, 1] < N - 1 and r_index[0, 0] > 0 and r_index[0, 1] > 0:
            E_1 += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == N - 1 and r_index[0, 1] < N - 1 and r_index[0, 1] > 0:
            E_1 += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] < N - 1 and r_index[0, 1] == 0 and r_index[0, 0] > 0:
            E_1 += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N - 1])
        elif r_index[0, 0] == 0 and r_index[0, 1] < N - 1 and r_index[0, 1] > 0:
            E_1 += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] < N - 1 and r_index[0, 1] == N - 1 and r_index[0, 0] > 0:
            E_1 += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == N - 1 and r_index[0, 1] == 0:
            E_1 += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N - 1])
        elif r_index[0, 0] == N - 1 and r_index[0, 1] == N - 1:
            E_1 += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == 0 and r_index[0, 1] == N - 1:
            E_1 += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == 0 and r_index[0, 1] == 0:
            E_1 += -2 * -J * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N - 1])

        E_2 = g * j * matrix[r_index[0, 0], r_index[0, 1]]
        E = E_1 + E_2

        if E <= 0:
            Sp[r_index[0, 0], r_index[0, 1]] = -1 * Sp[r_index[0, 0], r_index[0, 1]]
        else:
            P = np.exp(-E / (k_B * T))
            a = np.random.rand()
            if a < P:
                Sp[r_index[0, 0], r_index[0, 1]] = -1 * Sp[r_index[0, 0], r_index[0, 1]]
        matrix = -g * mu_B * Sp

    M_tot = np.sum(matrix)
    M.append(M_tot)



plt.plot(Bv,M)
plt.xlabel('B[T]')
plt.ylabel('M[T]')
plt.show()


