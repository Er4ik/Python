string = input().split('.')
flag = True
for i in range(len(string)):
    if 0 <= int(string[i]) <= 255:
        flag = True
    else:
        flag = False
        break
if flag == True:
    print('YES')
else:
    print('NO')
