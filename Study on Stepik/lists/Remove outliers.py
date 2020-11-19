n = int(input())
res = []
num, num1 = 0, 1000000
counter, counter1 = 0, 0
for i in range(n):
    res.append(int(input()))
    if num < res[i]:
        num = res[i]
        counter = i
    if num1 > res[i]:
        num1 = res[i]
        counter1 = i
del res[counter]
if len(res)-1 < counter1:
    del res[counter1 -1]
else:
    del res[counter1]
print(*res, sep ="\n")
