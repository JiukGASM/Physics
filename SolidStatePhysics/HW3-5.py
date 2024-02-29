import numpy as np
import matplotlib.pyplot as plt

# 2-D Ising model in which a square lattice is populated with spin-1/2 particles with Monte Carlo simulation by using Metropolis algorithm

##constants
N = 100
B = 1
g = 2
k_B = 1.380649 * 10 **(-23)
mu_B =  9.2740100783 * 10 **(-24)
J1 = 10**(-2) * 1.60218 * 10 ** (-19)
J2 = -10**(-2) * 1.60218 * 10 ** (-19)
n = 1000000
t = range(n)

##Metropolis algorithm Procedure
Tv = np.linspace(0.01, 150, 2000)
M = []
for j in Tv:
    Sp = -np.ones((N, N)) / 2
    matrix = -g * mu_B * Sp
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

##Metropolis algorithm Procedure
Tv = np.linspace(0.01, 150, 2000)
M1 = []
for j in Tv:
    Sp = -np.ones((N, N)) / 2
    matrix = -g * mu_B * Sp
    for i in t:
        # 3. A.
        r_index = np.random.randint(N, size=(1, 2))
        # 3. B.
        E_1 = 0
        if r_index[0, 0] < N - 1 and r_index[0, 1] < N - 1 and r_index[0, 0] > 0 and r_index[0, 1] > 0:
            E_1 += -2 * -J1 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == N - 1 and r_index[0, 1] < N - 1 and r_index[0, 1] > 0:
            E_1 += -2 * -J1 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] < N - 1 and r_index[0, 1] == 0 and r_index[0, 0] > 0:
            E_1 += -2 * -J1 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N - 1])
        elif r_index[0, 0] == 0 and r_index[0, 1] < N - 1 and r_index[0, 1] > 0:
            E_1 += -2 * -J1 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] < N - 1 and r_index[0, 1] == N - 1 and r_index[0, 0] > 0:
            E_1 += -2 * -J1 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == N - 1 and r_index[0, 1] == 0:
            E_1 += -2 * -J1 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N - 1])
        elif r_index[0, 0] == N - 1 and r_index[0, 1] == N - 1:
            E_1 += -2 * -J1 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == 0 and r_index[0, 1] == N - 1:
            E_1 += -2 * -J1 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == 0 and r_index[0, 1] == 0:
            E_1 += -2 * -J1 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N - 1])

        E_2 = g * B * matrix[r_index[0, 0], r_index[0, 1]]
        E = E_1 + E_2

        if E <= 0:
            Sp[r_index[0, 0], r_index[0, 1]] = -1 * Sp[r_index[0, 0], r_index[0, 1]]
        else:
            P = np.exp(-E / (k_B * j))
            a = np.random.rand()
            if a < P:
                Sp[r_index[0, 0], r_index[0, 1]] = -1 * Sp[r_index[0, 0], r_index[0, 1]]
        matrix = -g * mu_B * Sp

    M_tot = np.sum(matrix)
    M1.append(M_tot)

chi1 = np.divide(M1, B)

##Metropolis algorithm Procedure
Tv = np.linspace(0.01, 150, 2000)
M2 = []
for j in Tv:
    Sp = -np.ones((N, N)) / 2
    matrix = -g * mu_B * Sp
    for i in t:
        # 3. A.
        r_index = np.random.randint(N, size=(1, 2))
        # 3. B.
        E_1 = 0
        if r_index[0, 0] < N - 1 and r_index[0, 1] < N - 1 and r_index[0, 0] > 0 and r_index[0, 1] > 0:
            E_1 += -2 * -J2 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == N - 1 and r_index[0, 1] < N - 1 and r_index[0, 1] > 0:
            E_1 += -2 * -J2 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] < N - 1 and r_index[0, 1] == 0 and r_index[0, 0] > 0:
            E_1 += -2 * -J2 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N - 1])
        elif r_index[0, 0] == 0 and r_index[0, 1] < N - 1 and r_index[0, 1] > 0:
            E_1 += -2 * -J2 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] < N - 1 and r_index[0, 1] == N - 1 and r_index[0, 0] > 0:
            E_1 += -2 * -J2 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == N - 1 and r_index[0, 1] == 0:
            E_1 += -2 * -J2 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N - 1])
        elif r_index[0, 0] == N - 1 and r_index[0, 1] == N - 1:
            E_1 += -2 * -J2 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[0, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == 0 and r_index[0, 1] == N - 1:
            E_1 += -2 * -J2 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], 0]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] - 1])
        elif r_index[0, 0] == 0 and r_index[0, 1] == 0:
            E_1 += -2 * -J2 * (Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0] + 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[N - 1, r_index[0, 1]]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], r_index[0, 1] + 1]
                            + Sp[r_index[0, 0], r_index[0, 1]] * Sp[r_index[0, 0], N - 1])

        E_2 = g * B * matrix[r_index[0, 0], r_index[0, 1]]
        E = E_1 + E_2

        if E <= 0:
            Sp[r_index[0, 0], r_index[0, 1]] = -1 * Sp[r_index[0, 0], r_index[0, 1]]
        else:
            P = np.exp(-E / (k_B * j))
            a = np.random.rand()
            if a < P:
                Sp[r_index[0, 0], r_index[0, 1]] = -1 * Sp[r_index[0, 0], r_index[0, 1]]
        matrix = -g * mu_B * Sp

    M_tot = np.sum(matrix)
    M2.append(M_tot)

chi2 = np.divide(M2, B)



plt.plot(Tv,chi, label='paramagnet')
plt.legend(loc='upper right')
plt.plot(Tv,chi1, label='ferromagnet')
plt.legend(loc='upper right')
plt.plot(Tv,chi2, label='antiferromagent')
plt.legend(loc='upper right')
plt.xlabel('T[K]')
plt.ylabel('\u03C7')
plt.show()
