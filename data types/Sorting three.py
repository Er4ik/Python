a, b, c = int(input()), int(input()), int(input())
min, max = min(a, b, c), max(a, b, c)
print(max, a + b + c - min - max, min, sep = '\n')