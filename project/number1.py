# импорт всего необходимого
from random import randrange as rr
from time import sleep

# рандомное число по условиям игрока
def random_number():
    num = 0
    print('Хочешь ввести свой диапозон цифр или будем угадывать цифру от 1 до 100?')
    ch = input('Напиши "свой" или напиши "100": ')    
    if '100' in ch:
        flag = True
        num = rr(1, 101)
        return flag, num
    else:
        flag = False
        print('Тогда вводи диапазон сам')
        a = input('Введи начало диапазона - это должна быть цифра: ')
        while a.isdigit() == False:
            print('Нужно ввести цифру, идиот! Давай снова.')
            a = input('Введи начало диапазона: ')
        b = input('Введи конец диапазона - это должна быть цифра: ')
        while b.isdigit() == False:
            print('Нужно ввести цифру, идиот! Давай снова.')
            b = input('Введи конец диапазона: ')
        num = rr(int(a), int(b) + 1)
        return flag, num, a, b        

# число ли
def is_valid(n):
    return n.isdigit() and 0 < int(n) < 101

# сама игруля
def input_number(num):
    if num[0] == True:
        a, b = 1, 100
    else:
        a, b = num[2], num[3]
    print(f'Я загадал число от {a} до {b}. Попробуй угадать его. Введи цифру: ')
    trying = 0
    while True:
        n = input()
        if is_valid(n):
            trying += 1
            if int(n) > num[1]:
                print('Слишком много, попробуй еще раз')
            elif int(n) < num[1]:
                print('Слишком мало, попробуй еще раз')
            elif int(n) == num[1]:
                print('Ты угадал, поздравляю!', 'Было попыток:', trying)
                sleep(1)
                play_again()
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100? Введи: ')

# играем ли ещё
def play_again():
    print('...', 'Игра окончена. Сыграем ещё?', 'Напиши "да" или "нет"', sep='\n')
    ask = input()
    if ask.lower() == 'да':
        num = random_number()
        input_number(num)
    else:
        print("Не хочешь? Ну тогда досвидули =*")

# СТАРТ ИГРЫ
print('Добро пожаловать в числовую угадайку!')
sleep(1)
num = random_number()
input_number(num)