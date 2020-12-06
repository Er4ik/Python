def check_num(num):# функция проверки числа на буквы из таблицы систем счисления
  num_res = list(num)
  digs_words = "0123456789ABCDEF"
  digs_words = list(digs_words) # создаем список и заполняем его
  for i in range(len(num_res)):
    if num_res[i].isalpha(): # проверка, состоит ли переменная только из букв
      for j in range(len(digs_words)):
        if num_res[i] == digs_words[j]: # проверка равенства элемента из num элементу digs_words
          num_res[i] = j
  return num_res


def conv2dec(num, base):# функция перевода числа в десятичную систему счисления
  counter = 0
  num_res = 0
  for i in range(len(num)-1,-1,-1):
    num_res += int(num[i]) * (base ** counter)# выражение для вычисления 10-чного значения
    counter += 1
  return num_res

def dec2any(num, base_res):# функция перевода числа в заданную систему счисления
  res = []# создаем результирующий список
  if base_res > 10:
    digs_words = "0123456789ABCDEF"
    digs_words = list(digs_words) # создаем список и заполняем его
    while num // base_res > 1:
      res.append(digs_words[num % base_res])
      num //= base_res
  while num > 0:
    res.append(num % base_res)# заполняем список числами нужной нам системы счисления
    num //= base_res
  res.reverse()# правильное значение для систем счисления
  return res

# основная программа
num = input("Введите число, которое хотите перевести в другую систему счисления:\n")# ввод числа
if (num.isalnum() == False):
  num = input("Введите корректное число:\n")
base = int(input("\nВведите систему счисления данного числа:\n"))# ввод числа системы счисления
while (base < 2) or (base > 62):
  base = int(input("Введите корректное число:\n"))
base_res = int(input("\nВведите систему счисления, в котороую хотите перевести число:\n"))# ввод числа результирующей системы счисления
while (base_res < 2) or (base_res > 62):
  base_res = int(input("Введите корректное число:\n"))
if num.isalnum():# проверка введеного числа на наличие букв и цифр
  num = check_num(num)
num = conv2dec(num, base)
if base_res == 10:
  print("\nЧисло в", base_res, "системе счисления:")
  print(num)
else:
  num = dec2any(num, base_res)
  print("\nЧисло в", base_res, "системе счисления:")
  print(*num, sep = '')
