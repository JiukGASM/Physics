# A is odd
A = 209
Z = 83
B = 15.5*A - 16.8*A**(2/3) - 0.72*Z*(Z-1)*A**(-1/3) - 23*((A-2*Z)**2)/A
B_c = -0.72*Z*(Z-1)*A**(-1/3)
print(B)
print(B_c)

# A,Z are even
A = 256
Z = 100
B = 15.5*A - 16.8*A**(2/3) -0.72*Z*(Z-1)*A**(-1/3) - 23*((A-2*Z)**2)/A + 34*(A)**(-3/4)
B_c = -0.72*Z*(Z-1)*A**(-1/3)
print(B/A)
print(B_c)