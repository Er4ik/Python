s = input()
count, count1 = 0, 0
for i in range(0,len(s)):
    if s[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        count += 1
    if s[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        count1 += 1
print('Количество гласных букв равно',count)
print('Количество согласных букв равно',count1)
