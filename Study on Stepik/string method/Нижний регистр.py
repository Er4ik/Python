s = input()
count = 0
count1 = 0
for i in range(0, len(s)):
    n = s[i]
    if n == n.lower():
        count += 1
    for j in range(1,10):
            if str(j) in n:
                count1 += 1
print(count-count1)
