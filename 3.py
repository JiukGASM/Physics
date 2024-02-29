# if

# x = int(input("please type number:"))
#
# if x<0:
#     x = 0
#     print("Negative number into zero")
# elif x == 0:
#     print("zero")
# elif x == 1:
#     print("One")
# else:
#     print("more")


#for
# students =["jiuk","hyunwoo","jihyung","myunggil"]
#
# for names in students:
#     print(names, len(names))
#
# numbers = [1,2,3,4,5,6,7]
# for i in numbers:
#     print(i)
#
#
# for i in range(5):
#     print(i)
#
# for i in range(0,5):
#     print(i)
#
# for i in range(0,5,1):
#     print(i)

## overloaded  + 가 스트링, 인트등 다양한 것에 대해서 정의되어있는 것을 말
#
# print(list(range(5)))
# print(list(range(0,50,5)))
# print(list(range(0,10,-5)))
#
# for i in range(-10,50,2):
#     print(i)
#
#
# students =["jiuk","hyunwoo","jihyung","myunggil"]
#
# for i in range(len(students)):
#     print(i, students[i])


# for i in range(2,10): # 2,3,4,5,6,7,8,9
#     print(i)
#     for j in range(2,i):
#         print("what is j =",j)
#         if i%j == 0:
#             print("you get out")
#             break
#
#         # else:print("remainder is not zero")
#
#     else:
#         print(i, " is prime number")

##function

# def fib2(n): #argument 없이도 만들 수 있어  fib2()같
#     a,b = 0, 1
#     while a < n:
#         print(a)
#         a,b = b, a+b
#
# fib2(10)
# fib2(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

# def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"): #변수들의 위치 중요 or 언급해서 대
#     print("-- This parrot wouldn't", action, end=" ")
#     print("if you put", voltage, "volts though it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
#
#
# parrot(voltage=5.0, action="vooom")

# fruits = ["Orange","Apple","Banana","Apple","Kiwi"]
# print(fruits.count("Apple"))
# print(fruits)
# fruits.reverse()
# fruits.append("gyul")
# print(fruits)
# fruits.sort()
# fruits.pop() # return the last item and remove it

# sqrt = []
# sqrt.append(1)
# sqrt.append(4)
# sqrt.append(9)
# sqrt.append(16)
# sqrt.append(25)
# sqrt.append(36)
# jegobs = []
# for x in range(10):
#     jegobs.append(x**2)
# print(jegobs)
# xx = [x**2 for x in range(10)]