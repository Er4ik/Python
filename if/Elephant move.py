a,b,c,d = int(input()),int(input()),int(input()),int(input())
if (c-a == d-b or c-a == b-d) or (d-b == c-a or d-b == a-c):
    print('YES')
else:
    print('NO')