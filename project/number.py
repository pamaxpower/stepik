from random import *
from time import sleep
import os
cls = lambda: os.system('cls')



num = randint(1, 100)
print('\nДобро пожаловать в числовую угадайку\n')
print('Я загадал какое-то число от 1 до 100. Попробуйте его угадать\n')

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100


while True:
    your_num = input('Введите ваше число от 1 до 100:\t')
    
    if is_valid(your_num) == True:
        your_num = int(your_num)

        if your_num < num:
            print('\n\t\tВаше число МЕНЬШЕ загаданного, попробуйте еще разок\n')
        elif your_num > num:
            print('\n\t\tВаше число БОЛЬШЕ загаданного, попробуйте еще разок\n')
        else:
            print('ВЫ УГАДАЛИ. ПОЗДРАВЛЯЕМ!!!\n')

            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            sleep(5)
            cls()
            break

    
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')

