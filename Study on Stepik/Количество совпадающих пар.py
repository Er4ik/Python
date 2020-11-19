string = input().split()
counter = 0
for i in range(len(string)):
    for j in range(len(string)):
        if i == j:
            continue
        if string[j] == string[i]:
            counter += 1
print(counter//2)
