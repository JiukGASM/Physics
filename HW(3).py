import numpy as np
import matplotlib.pyplot as plt

#(a)
## data
F = np.array([2.0, 4.0, 6.0, 8.0, 10, 12, 14, 16, 18, 20, 22]) # [N]
L = np.array([15, 32, 49, 64, 79, 98, 112, 126, 149, 175, 190]) # [mm]
L = L/1000. # [mm] -> [m]

## drawing
plt.plot(F,L,'o')
plt.grid()
plt.show()

#(b)
## brute force fit model : f = ax + b
mini = 9999

for a in range(100,2000,1):
    a = a/100000.

    for b in range(-100,300,1):
        b = b/1000.

        s = 0.0 # initialize s value
        for i in range (11):
            x = 2 * (i + 1)
            ff = a * x + b
            s +=  (L[i]-ff) * (L[i]-ff)

        if (s < mini) :
            mini = s
            print(a, b, 1./a, -b/a, s)


x = np.arange(15,190,0.1)
x = x/1000.
f = []
for i in x:
    f.append(115.47 * i + 0.577) # best fit line F = a * L + b

plt.plot(f,x,'r-',F,L,'bo')
plt.grid()
plt.show()


#(c)


#(d)
k = 115.47 # [N/m]

#(e)
x_2 = 105 #[mm]
x_2 = x_2/1000. #[m]
F = 115.47 *  x_2 + 0.577
print(F)
# 12.70135 N
