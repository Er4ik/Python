num = int(input())
res = []
for i in range(num):
    digit = int(input())
    res.append(digit**2+2*digit+1)
    print(digit)
print()
print(*res, sep = '\n')
