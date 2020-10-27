count = 0
n = str(input())
while n != 'стоп':
    if n == 'хватит':
        break
    if n == 'достаточно':
        break
    n = str(input())
    count += 1
print(count)
