n,b = int(input()),'YES'
while n // 10 != 0 :
    a = n % 10  
    n = n // 10
    if a > n % 10:
        b = 'NO'
print(b)
