n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
del l[1::2]
print(l)
