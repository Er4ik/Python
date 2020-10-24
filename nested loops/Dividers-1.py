a = int(input())
b = int(input())
count = 0
count1 = 0
n = 0
for i in range (a,b+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += j
    if count >= count1:
        count1 = count
        n = i
print(n, count1)
