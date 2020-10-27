n = int(input())
a = int(1)
b = int(1)
if n == 1:
    print('1')
elif n == 2:
    print(1, 1)
else:
    print(1, 1, "", end='')
    for i in range(n - 2):
        c = a + b
        print(c, "", end='')
        a = b
        b = c
