a = int(input())
m,n,s = max(a//100,a%10,a%100//10),min(( a//100,a%10,a%100//10)),(a//100+a%10+a%100//10)
if m-n == s-m-n:
    print('Число интересное')
else:
    print('Число неинтересное')