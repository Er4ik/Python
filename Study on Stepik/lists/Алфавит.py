abc = 'abcdefghijklmnopqrstuvwxyz'
l = []
for i in range(1,len(abc)+1):
    l.append(abc[i-1]*i)
print(l)
