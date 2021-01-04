def check_num(num):# функция проверки числа на буквы из таблицы систем исчисления
  num_res = list(num)
  digs_words = "0123456789ABCDEF"
  digs_words = list(digs_words) # создаем список и заполняем его
  for i in range(len(num_res)):
    if num_res[i].isalpha(): # проверка, состоит ли значение только из букв
      for j in range(len(digs_words)):
        if num_res[i] == digs_words[j]: # проверка равенства элемента из num элементу digs_words
          num_res[i] = j
  return num_res

def base_num_check(base): # Функция проверки корректности ввода начальной системы исчисления
  if (base.isdigit() == False):
    base = input("\nВведите корректное число в диапазоне от 1 до 16\n")
    return base_num_check(base)
  else:
    base = int(base)
    return base

def base_res_num_check(base_res): # Функция проверки корректности ввода конечной системы исчисления
  if (base_res.isdigit() == False):
    base_res = input("\nВведите корректное число в диапазоне от 1 до 16\n")
    return base_res_num_check(base_res)
  else:
    base_res = int(base_res)
    return base_res

def check_num2(num, base):# функция проверки корректности ввода числа
  num1 = list(num)
  if (num.isalnum() == False):
    num = input("\nВведите корректное число для перевода в другую систему:\n")
    return check_num2(num, base)
  elif (base > 10):
    flag = False
    words = "ABCDEF"
    for i in range(len(num1)):
      if num1[i] in words:
        flag = True
        break
    if flag:
      return num
    else:
      num = input("\nВведите корректное число для перевода в другую систему исчисления:\n")
      return check_num2(num, base)
  elif base <= 10:
    flag = True
    if num.isdigit():
      for i in range(len(num1)):
        if int(num1[i]) >= base:
          flag = False
    else:
      num = input("\nВведите корректное число, состоящее только из цифр:\n")
      return check_num2(num, base)
    if flag:
      return num
    else:
      num = input("\nВведите корректное число, состоящее только из цифр:\n")
      return check_num2(num, base)

def conv2dec(num, base):# функция перевода числа в десятичную систему исчисления
  counter = 0
  num_res = 0
  for i in range(len(num)-1,-1,-1):
    num_res += int(num[i]) * (base ** counter)# выражение для вычисления 10-чного значения
    counter += 1
  return num_res

def dec2any(num, base_res):# функция перевода числа в заданную систему исчисления
  res = []# создаем результирующий список
  if base_res > 10:
    digs_words = "0123456789ABCDEF"
    digs_words = list(digs_words) # создаем список и заполняем его
    while num // base_res > 1:
      res.append(digs_words[num % base_res])
      num //= base_res
  while num > 0:
    res.append(num % base_res)# заполняем список числами нужной нам системы исчисления
    num //= base_res
  res.reverse()# правильное значение для систем счисления
  return res

# основная программа
base = input("Введите систему исчисления числа:\n")# ввод числа системы исчисления
base = base_num_check(base)
while (base < 2) or (base > 16):
  base = input("\nВведите корректное число в диапазоне от 2 до 16 включительно:\n")
  base = base_num_check(base)
num = input("\nВведите число, которое хотите перевести в другую систему исчисления:\n")# ввод числа
num = check_num2(num, base)
num1 = num
base_res = input("\nВведите систему исчисления, в котороую хотите перевести число:\n")# ввод числа результирующей системы исчисления
base_res = base_res_num_check(base_res)
while (base_res < 2) or (base_res > 16):
  base_res = input("\nВведите корректное число:\n")
  base_res = base_res_num_check(base_res)
if base > 10:
  num = check_num(num)
num = conv2dec(num, base)
if base_res == 10:
  print(f"\nЧисло {num1} в {base_res}-чной системе исчисления:")
  print(num)
else:
  num = dec2any(num, base_res)
  print(f"\nЧисло {num1} в {base_res}-чной системе исчисления:")
  print(*num, sep = '')
