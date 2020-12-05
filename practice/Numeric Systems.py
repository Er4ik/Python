def check_num(num):# функция проверки числа на буквы из табл. систем счисления
  num_res = list(num)
  digs = "0123456789"
  words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  words_low = words.lower()
  digs_words = digs + words + words_low
  digs_words = list(digs_words) # создаем список и заполняем его
  for i in range(len(num_res)):
    if num_res[i].isalpha(): # проверка, состоит ли только из букв
      for j in range(len(digs_words)):
        if num_res[i] == digs_words[j]: # проверка равенства эл-та из num эл-ту digs_words
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
  while num > 0:
    res.append(num % base_res)# заполняем список числами нужной нам системы счисления
    num //= base_res
  res.reverse()# правильное значение для систем счисления
  return res

num = input()# ввод числа
base = int(input())# ввод числа системы счисления
base_res = int(input())# ввультирующей системы счисления
if num.isalnum():# проверка введеного числа на наличие букв и цифр
  num = check_num(num)# присваиваем num значение, которое возвращает функция check_num
num = conv2dec(num, base)
if base_res == 10:
  print(num)
else:
  num = dec2any(num, base_res)
  print(*num)
