s = input()
flag = True
for i in range(0,10):
    if str(i) in s:
        flag = False
        break
if flag == True:
    print('Цифр нет')
else:
    print('Цифра')
