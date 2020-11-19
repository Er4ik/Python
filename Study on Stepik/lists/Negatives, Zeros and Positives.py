num = int(input())
res, res1, res2 = [], [], []
digit = 0
for i in range(num):
    digit = int(input())
    if digit < 0:
        res.append(digit)
    elif digit == 0:
        res1.append(digit)
    else:
        res2.append(digit)
res.extend(res1)
res.extend(res2)
print(*res, sep = '\n')
