n = 0
count = 0
while n >= 0:
    if n == 5:
        count += 1
    n = int(input())
    if n < 0 or n > 5:
        break
print(count)
