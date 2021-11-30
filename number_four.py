import math
import time

num_1=int(input("Enter first number"))
num_2=int(input("Enter second number"))

start1=time.time()
l = []
for i in range(num_1,num_2+1):
    if i > 1:

        for factor in range(2,i):
            if i % factor == 0:
                break
            else:
                l.append(i)
print(len(l))