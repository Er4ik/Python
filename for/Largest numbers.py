n = int(input())
temp = 0
temp2 = 1
for i in range(n):
    x = int(input())
    if x > temp and temp < temp2:
        temp = x
    elif x > temp2:
        temp2 = x
print(max(temp, temp2))
print(min(temp, temp2))
