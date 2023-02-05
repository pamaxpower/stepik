'''
n = int(input()) # первая
m = int(input()) # вторая
k = int(input()) # третья
x = int(input()) # первая + вторая
y = int(input()) # вторая + третья
z = int(input()) # первая + третья
t = int(input()) # первая + вторая + третья
a = int(input()) # всего


# m-x-y     # только деревня
# n-x       # только море
# k-y       # только горы
# x         # деревня + море
# y         # деревня + горы
# z         # ДВИ
# print(m-x-y+n-x+k-y+x+y+z)    # всего учеников

a-(n+m) # только третья
a-(m+k) # только первая
a-(n+k) # только вторая

#print(a-(n+m)+a-(m+k)+a-(n+k))
print((a-x)+(a-y)+(a-z))
'''
my_set = {}
print(my_set, type(my_set))
my_set = set([])
print(my_set, type(my_set))
my_set = set([''])
print(my_set, type(my_set))
my_set = set(())
print(my_set, type(my_set))
my_set = set('')
print(my_set, type(my_set))
my_set = set()
print(my_set, type(my_set))