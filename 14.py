import numpy as np
a = np.array([1,2,3])
N = 10
mass = 20.0*np.ones((N,1))

print(a)
print(mass*mass.T)
print(np.mean(mass,1))
print(max(1,2))