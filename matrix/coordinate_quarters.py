count_points = int(input())

count1 = count2 = count3 = count4 = 0
for p in range(count_points):
    point = input().split()
    if int(point[0]) > 0 and int(point[1]) > 0:
        count1 += 1
    elif int(point[0]) < 0 and int(point[1]) > 0:
        count2 += 1
    elif int(point[0]) < 0 and int(point[1]) < 0:
        count3 += 1
    elif int(point[0]) > 0 and int(point[1]) < 0:
        count4 += 1

print(f'Первая четверть: {count1}')
print(f'Вторая четверть: {count2}')
print(f'Третья четверть: {count3}')
print(f'Четвертая четверть: {count4}')



