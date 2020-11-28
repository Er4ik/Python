def Head():
    import random
    global dig
    dig = random.randrange(1,100)
    print('Добро пожаловать в числовую угадайку', 'Введите число от 1 до 100:', sep = '\n')

def is_valid():
    global num
    num = input()
    if num.isdigit():
        return True
    else:
        return False

def check(num):
    flag1 = True
    counter = 0
    while flag1:
        if dig < num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            num = int(input())
            counter += 1
        elif dig > num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            num = int(input())
            counter += 1
        elif dig == num:
            counter += 1
            print('Вы угадали, поздравляем!')
            print('Вам для этого понадобилось', counter, 'попыток.')
            flag1 = False
            break

Head()
flag = True
while flag:
    if is_valid():
        num = int(num)
        flag = False
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
check(num)
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
