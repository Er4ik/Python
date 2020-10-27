a,b,c = int(input()), int(input()), int(input())
if a < b+c and b < c+a and c < a+b:
    print('YES')
else:
    print('NO')
