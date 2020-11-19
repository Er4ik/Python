n = int(input())
l = []
count = 0
for i in range(1,n+1):
    i = int(input())
    count += 1
    if count > 1:
        l.append(n+i)
    n = i
print(l)
