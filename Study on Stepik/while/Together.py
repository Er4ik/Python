n = int(input())
m = n
summ = 0 
mult = 1
count = 0
while n != 0:
    summ += n % 10
    mult *= n % 10
    count += 1
    n //= 10
print(summ, count, mult, summ/count, m//(10**(count-1)), m//(10**(count-1))+m%10, sep = '\n') 