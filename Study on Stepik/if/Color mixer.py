a,b = str(input()),str(input())
if (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный'):
    print('фиолетовый')
elif (a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный'):
    print('оранжевый')
elif (a == 'желтый' and b == 'синий') or (a == 'синий' and b == 'желтый'):
    print('зеленый')
elif a == b == 'красный':
    print('красный')
elif a == b == 'желтый':
    print('желтый')
elif a == b == 'синий':
    print('синий')
else:
    print('ошибка цвета')