n = int(input())
count = []
flag = True
num = ''
while flag == True:
    if n % 2 == 0:
        count.append(0)
    if n % 2 == 1:
        count.append(1)
    if n // 2 == 0:
        if n % 2 == 0:
            count.append(0)
        flag = False
    n //= 2
count.reverse()
for i in range(0,len(count)):
    num += str(count[i])
print(num)
