#fibonacci
# n = int(input())
# fib = [0,1]
# for i in range(n):
#     fib.append(fib[i]+fib[i+1])
#
# print(fib)

# or

# (a, b = b, a+b) != (a = b and b = a+b)

from math import *

#quiz
#1
s = "20182268"
a = (complex((int(s[0])),(int(s[1]))) *complex((int(s[2])),(int(s[3])))) / (complex((int(s[4])),(int(s[5]))) * complex((int(s[6])),(int(s[7]))))
print(a)
a = ((2 + 0j) *(1 + 8j)) / ((2 + 2j) * (6 + 8j))
print(a)

#2
import numpy as np
x  = np.array([[2,0],[1,8]])
y = np.array([[2,2],[6,8]])
A = x@y #dot product
print(A)
print(4+4+50+66)