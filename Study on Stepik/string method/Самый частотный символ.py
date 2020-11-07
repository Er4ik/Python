s, counter1, counter, answ = input(), 0, 0, 0
for i in range(0,len(s)):
    counter1 = s.count(s[i])
    if counter1 >= counter:
        answ = s[i]
        counter = counter1
print(answ)
