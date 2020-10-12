a = int(input())
if (a % 2 != 0) or (6 <= a <= 20 and a % 2 == 0):
    print('YES')
elif (a % 2 == 0) and (2 <= a <= 5 or a >20):
    print('NO')