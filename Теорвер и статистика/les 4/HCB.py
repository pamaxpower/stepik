"""
Непрерывная случайная величина
"""
import math
import numpy as np

def find_dispersion(array, mean):
    array.sort()
    

def normal_distribution(array,x):
    """
    Принимает на вход массив и некую случайную величину и возвращает нормальное распределение.
    Пояснения к расчетам:
    x - случайная величина
    mX - мат.ожидание (среднее арифметическое)
    dispersion - дисперсия
    std - стандартное отклонение
    degree_index - показатель степени, в который надо возмести число Эйлера
    """
    array.sort()
    mX = sum(array)/len(array)
    s = 0
    for i in range(len(array)):
        s += (array[i]-mX)**2
    dispersion = s/len(array)
    std = math.sqrt(dispersion)
    degree_index = math.pow(x-mX,2) / 2 * math.pow(dispersion,2)

    return 1 / (std * math.sqrt(2*math.pi)) * math.pow(math.e, -degree_index)

def SND(x):
    """
    SND - стандартное нормальное распределение
     """
    
    #z = (x-mX)/d

    # dispersion = 1
    # std = math.sqrt(dispersion)
    # degree_index = math.pow(x-mX,2) / 2 * math.pow(dispersion,2)

    # a = 1 / (std * math.sqrt(2*math.pi)) * math.pow(math.e, -degree_index)
    # b = 1/ math.sqrt(2*math.pi) * math.pow(math.e,-math.pow(x,2)/2)
    
    zzz = 1/(math.sqrt(2*math.pi)) * math.pow(math.e, -(x**2)/2)

    return zzz

print(np.random.normal(0,1,size=(-1, 1)))
