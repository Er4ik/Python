x = int(input())
count = 0
while x != 0:
    if x // 25 > 0:
        count += x // 25        
        x %= 25
    if x // 10 > 0:
        count += x // 10
        x %= 10
    if x // 5 > 0:
        count += x // 5
        x %= 5
    if x // 1 > 0:
        count += x // 1
        x %= 1
print(count)