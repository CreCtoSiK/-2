'''
Дано множество A из N точек на плоскости и точка B (точки заданы своими 
координатами х, у). Найти точку из множества A, наиболее близкую к точке B. 
Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по 
формуле: 
R = √(x2 – x1)2 + (у2 – y1)2. 
Для хранения данных о каждом наборе точек следует использовать по два списка: первый 
список для хранения абсцисс, второй — для хранения ординат.
'''

import math

def find_closest_point(A_x, A_y, B_x, B_y):
    min_distance = float('inf')  