
p1 = input()
p2 = input()

# 1 вариант. Через условия
if p1 == 'Спок' and p2 == 'ножницы' or p1 == 'Спок' and p2 == 'камень':
    print('player1')
elif p1 == 'ножницы' and p2 == 'бумага' or p1 == 'ножницы' and p2 == 'ящерица':
    print('player1')
elif p1 == 'бумага' and p2 == 'камень' or p1 == 'бумага' and p2 == 'Спок':
    print('player1')
elif p1 == 'камень' and p2 == 'ящерица' or p1 == 'камень' and p2 == 'ножницы':
    print('player1')
elif p1 == 'ящерица' and p2 == 'Спок' or p1 == 'ящерица' and p2 == 'бумага':
    print('player1')
elif p1 == p2:
    print('ничья')
else:
    print('player2')


# 2 вариант. Через списки
var = ['Спок', 'ножницы', 'бумага', 'камень', 'ящерица']       # список вариантов
ans = ['ничья', 'player2', 'player1', 'player2', 'player1']       # список результатов
# var.index(p1) - ищем индексы вхождений элементов
# находим их разность
# находим элемент в списке по индексу, равному разности
if var.index(p1) - var.index(p2) == 0:
    print('Ничья')
elif (var.index(p1) - var.index(p2)) % 2 == 0:
    print()
print(ans[var.index(p1) - var.index(p2)])
