from random import choice
from time import sleep

def thinking():
    """ Блок, когда шар думает """
    timeout = 1
    thoughts_count = 5
    thoughts = ['Хм... нужно подумать...', 'Интересно. Размышляю...', 'Вот это да! Дай мне секунду...', 
                'Сложная проблема, но я справлюсь...', 'Так, нужно пару секунд на размышления...']
    for _ in range(thoughts_count):
        print(choice(thoughts))
        sleep(timeout)
        print('...')
        sleep(timeout)

