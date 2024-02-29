

from math import *

print(atan(0.2))
print(6**4)
print(pow(6,4))
# print(factorial(1/2))
print(gamma(-3/2)) #(1/2)!
print(factorial(10)) #10!
print((2+3j/(3+4j))) #(2+3i)/(3+4i)



import numpy as np
x  = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print(x)
print(np.add(x,y))
print(x@y) #dot product

## string
print("spam")
print('spam')
#print('spam's egg') #error
print("spam's egg")

word ="python"
print(word[0])
print(word[-1]) # python -> 0,1,2,3,4,5 / -6,-5,-4,-3,-2,-1
print(word[0:2]) #[0],[1]
print(word[-4:]) #[-1][-2][-3][-4]

## list (collection of item)
sqrts = [1, 1.4, 2.2]
print(sqrts)
print(sqrts[2])
print(sqrts + [3, 3.5])
nsqrts = sqrts + [3, 3.5]
nsqrts[0] = 0.001
print(nsqrts)
nsqrts.append(100) # add item at end of the list
print(nsqrts)

nsqrts.append("wow") # we can add different type of item to the list
print(nsqrts)

a,b = 0,1

#fibonacci
n = int(input())
fib = [0,1]
for i in range(n):
    fib.append(fib[i]+fib[i+1])

print(fib)



