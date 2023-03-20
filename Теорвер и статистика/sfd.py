import numpy as np
a = [77,79,67,95,87,91,98,100,104,105]

#print(f'среднее арифметическое: {sum(a)/len(a)}')
print(f'среднее арифметическое: {np.mean(a)}')
print(f'медиана: {np.median(a)}')
print(f'Интерквартильно расстояние: {np.quantile(a,0.75)-np.quantile(a,0.25)}')
print(f'дисперсия: {np.var(a,ddof=1)}')
print(f'среднее квадратичное отклонение: {np.std(a,ddof=1)}') 