'''
Вам доступен список pets, содержащий информацию о собаках и их владельцах.  
Каждый элемент списка – это кортеж вида (кличка собаки, имя владельца, 
фамилия владельца, возраст владельца).

Дополните приведенный код так, чтобы в переменной result хранился словарь, 
в котором для каждого владельца будут перечислены его собаки. 
Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), 
а значением – список кличек собак (сохранив исходный порядок следования).

Примечание 1. Не забывайте: кортежи являются неизменяемыми, 
поэтому могут быть ключами словаря.

Примечание 2. Обратите внимание, что у некоторых владельцев по несколько собак.
'''

pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

# ключом будет срез кортежа [1:], а значением 0 элемент

result = {}
for el in pets:
    val = []                        # пустой список для значения словаря
    if el[1:] not in result:        # если ключа нет:  
        val.append(el[0])           # то в список добавляем 0-элемент кортежа
        result[el[1:]] = val        # и присваиваем его ключу
    else:
        # если значение уже есть, то к значению по ключу добавляем 0-элемент
        result[el[1:]].append(el[0])

    
print(result)

# {('Parker', 'Wilson', 50): ['Hatiko'], 
#  ('Josh', 'King', 25): ['Rusty', 'Balto', 'Barry', 'Lassie'], 
#  ('John', 'Smith', 28): ['Fido'], 
#  ('Jake', 'Smirnoff', 18): ['Butch'], 
#  ('Emma', 'Wright', 18): ['Odi'], 
#  ('Hannah', 'Taylor', 40): ['Snape'], 
#  ('Martha', 'Robinson', 73): ['Horry', 'Chase'], 
#  ('Alex', 'Martinez', 65): ['Giro'], 
#  ('Simon', 'Nevel', 32): ['Zooma', 'Rocky'], 
#  ('Martha', 'Williams', 38): ['Ace']}