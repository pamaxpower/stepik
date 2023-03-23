"""
Правилдо трех сигм (std)
"""
mX = 0
std = 1
x =1
if mX-std < x < mX+std:
    y = 0.68
elif mX-2*std < x < mX+2*std:
    y = 0.954
elif mX-3*std < x < mX+3*std:
    y = 0.9972
print(y)