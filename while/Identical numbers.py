num, x = int(input()), 0
y = num % 10
flag = True
while num != 0:
    x = num % 10
    if x != y:
        flag = False
        break
    else:
        flag = True
    num //= 10
if flag == True:
    print ("YES")
else:
    print ("NO")

