from math import *
a,b,c = float(input()),float(input()),float(input())
d,x1,x2 = 0,0,0
if a != 0:
    if b**2-4*a*c > 0:
        d = b**2-4*a*c
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
        print(min(x1,x2), max(x1,x2), sep = '\n')
    elif pow(b,2)-4*a*c < 0:
        print('Нет корней')
    else:
        print(-b/(2*a))
else:
    print('Нет корней')
    