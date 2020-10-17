n = int(input())
count = 0
m = n
while n != 0:
    count += 1
    n //= 10
print(m//10**(count-2)%10)
