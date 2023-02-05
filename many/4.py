'''
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset3 = myset1.union(myset2)           # {1, 2, 3, 4, 5, 6, 7, 8}
#myset1.update(myset2)                   # {1, 2, 3, 4, 5, 6, 7, 8}
myset4 = myset1 | myset2                # {1, 2, 3, 4, 5, 6, 7, 8}

myset5 = myset1.intersection(myset2)    # {3, 4}
#myset1.intersection_update(myset2)      # {3, 4}
myset7 = myset1 & myset2                # {3, 4}

myset8 = myset1.difference(myset2)      # {1, 2, 5}
myset9 = myset1 - myset2                # {1, 2, 5}
#myset2.difference_update(myset1)        # {6, 7, 8}

myset10 = myset1.symmetric_difference(myset2)   # {1, 2, 5, 6, 7, 8}
myset12 = myset2.symmetric_difference(myset1)   # {1, 2, 5, 6, 7, 8}
myset11 = myset1 ^ myset2                       # {1, 2, 5, 6, 7, 8}
#myset1.symmetric_difference_update(myset2)      # {1, 2, 5, 6, 7, 8}
'''

# s1 = set(input().split())
# s2 = set(input().split())

# print(len(s1 & s2))
# # print(len(set(input().split()) & set(input().split())))

# print(*sorted(list(map(int, s1 & s2))))
# #print(*sorted(list(map(int, set(input().split()) & set(input().split())))))

# print(*sorted(list(map(int, s1 - s2))))
# #print(*sorted(list(map(int, set(input().split()) - set(input().split())))))

# =========================================================================

# Общие цифры
s = [input() for _ in range(int(input()))]

res = set(map(int, s[0]))
for el in s:
    res &= set(map(int, el))
print(*sorted(res))

#print(*sorted(set.intersection(*(set(input()) for i in range(int(input()))))))