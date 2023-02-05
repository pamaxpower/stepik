from random import *
from display_hangman import *

word_list = ['дом', 'лес', 'жар', 'пух', 'кит', 'эль', 'ямб', 'сыр', 'мёд',
             'юла']


def get_word(s):
    return choice(s)


def print_word(word1, list1):
    for j in word1:
        if j in list1:
            print(j, end=' ')
        else:
            print('_', end=' ')
    print()


def play(s):
    word_completion = '_ ' * len(s)  # строка, содержащая символы _ на каждую букву задуманного слова
    flag = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество промахов

    print('Давайте играть в угадайку слов!\n')
    print(f'\t{s}')
    print(f'Начинаем игру. У вас {tries} промахов\n')
    print('\nНачинаем игру!!!\n')
    print(f'{word_completion}\n')
    while True:
        wrd = input('Назовете букву или угадаете слово целиком? ')
        if wrd in s:
            print('+')
            guessed_letters.append(wrd)
            for j in s:
                if j not in guessed_letters:
                    print('Есть такая буква!!!\n')
                    print(f'Откройте букву {wrd}')
                    print_word(s, guessed_letters)
                    flag = False
                    break
                flag = True
            if flag:
                print_word(s, guessed_letters)
                print('Поздравляю!!! Вы угадали слово')
                break
        else:
            guessed_letters.append(wrd)
            tries -= 1
            print('Неверно! Неправильное слово')
            print(f'Осталось {tries} попыток')
            print_word(s, guessed_letters)

        if tries == 0:
            print_word(s, guessed_letters)
            print('ИГРА ОКОНЧЕНА. ВЫ ПРОИГРАЛИ')
            break


word = get_word(word_list)
play(word)
