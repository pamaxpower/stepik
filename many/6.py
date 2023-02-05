'''
Генераторы множества
'''

# множество из первый букв элементов списка в алфаыитном порядке
words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
#myset = {el[0].lower() for el in words}
#print(*sorted(myset))


# множество из уникальных слов в нижнем регистре, 
# без знаков препинания, отсортированных в алфавитном порядке
sentence = 'My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'
s = [el.strip('!,.():?;-') for el in sentence.lower().split()]
myset1 = {i for i in s}
print(*sorted(myset1))
print()


# множество уникальных слов длинною меньше 4 символов в нижнем регистре, 
# без знаков препинания, отсортированных в алфавитном порядке
sentence = 'My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'
myset2 = {el.strip('!,.():?;-') for el in sentence.lower().split()}
print(*sorted({i for i in myset2 if len(i)<4}))


# уникальные имена файлов с расширением .png, не зависимо от регистра имен и расширений
files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
myset3 = {el.lower() for el in files if el[-3:].lower() == 'png'}
print(*sorted(myset3))
