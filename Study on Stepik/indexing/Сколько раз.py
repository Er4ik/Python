s = input()
n = 0
count, count1 = 0, 0
for i in range(0,len(s)):
    if '+' == s[i]:
        count += 1
    if '*' == s[i]:
        count1 += 1
print("Символ + встречается", count, 'раз')
print("Символ * встречается", count1, 'раз')
