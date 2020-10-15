from math import *
n = int(input())
x = 0
y = 9
count = 0
while n != 0:
    x = n % 10
    n //= 10
    if x > count:
        count = x
    if x <= y:
        y = x
print('Максимальная цифра равна',count)
print('Минимальная цифра равна',y)
  