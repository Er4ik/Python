n, flag = int(input()), True
for i in range (2,n+1):
    if n % i == 0:
        flag = False
        break
if flag == False:
    print(i)
else:
    print(n)
    