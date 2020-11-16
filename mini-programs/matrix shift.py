import random 
a = int(input('Enter a: '))
b = int(input('Enter b(b>a): '))
n = int(input('Enter n: '))

def matrix():
  lst=[]
  for i in range(n):
    lst.append([])
    for j in range(n):
      lst[i].append(random.randint(a, b))                
  print('Дано масив')
  for i in range(n):
    print(' '.join(map(str,lst[i])))
  print()
  return lst 

def shift(lst):
  final_list = []
  for row in lst:
    steps = min(row)
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            row.append(row.pop(0))
    else:
        for i in range(steps):
            row.append(row.pop(0))
    print(' '.join(map(str,row)))


shift(matrix())
input()