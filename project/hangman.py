from random import *
from display_hangman import *

word_list = ['дом', 'лес', 'жар', 'пух', 'кит', 'эль', 'ямб', 'сыр', 'мёд',
             'юла']


def get_word(s):
    return choice(s)


def rules_game(ans):
    ans_yes = ['д', 'да', 'lf', 'y', 'yes']
    # ans_no = ['н', 'нет', 'ytn', 'n', 'no']
    if ans in ans_yes:
        print('\nПравила такие: ')
        print(f'Это виселица: {display_hangman(6)} ')
        print('При каждом неверном ответе, я буду пририсовывать ваши части тела))))')
        print('Игра идет до 6 ошибок, после чего вы проигрываете')
    else:
        print('\nНе хотите - как хотите')
        print('Но предупреждаю, что незнание правил не освобождает вас от игры по ним')


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
    n = input('Хотите узнать правила игры? ')
    rules_game(n)
    print('\nНачинаем игру!!!\n')
    print(f'{word_completion}\n')
    while True:
        print(f'{randrange(100, 1001, 100)} очков на барабане.')
        wrd = input('Назовете букву или угадаете слово целиком? ')
        if not wrd.isalpha():  # проверка на введенную букву
            print('Это не буква. Введите заново!')
            continue
        if wrd in guessed_letters or wrd in guessed_words:  # проверка на "уже было"
            print('Это уже было')
            continue
        if len(wrd) > 1:  # пользователь ввело слово
            if wrd == s:
                print('Поздравляю! Вы угадали слово!')
                break
            else:
                guessed_words.append(wrd)
            tries -= 1
            print('Неверно! Неправильное слово')
            print(f'Осталось {tries} попыток')
            print(display_hangman(tries))
            print_word(wrd, guessed_letters)
            continue
        if wrd in s:
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
            print(display_hangman(tries))
            print_word(s, guessed_letters)

        if tries == 0:
            print_word(s, guessed_letters)
            print('ИГРА ОКОНЧЕНА. ВЫ ПРОИГРАЛИ')
            break


word = get_word(word_list)
play(word)
