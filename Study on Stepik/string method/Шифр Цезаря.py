n = int(input())
s = input()
res = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(s)):
    res += alphabet[alphabet.find(s[i])-n]
print(res)
