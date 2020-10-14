from math import *
a = int(input())
count = 0
for i in range (1,a+1):
    count += (1/i)
count -= log(a)
print (count)
