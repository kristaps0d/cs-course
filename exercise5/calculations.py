import math
import random

def list_comprehension(list=[], seed=None, n=10, allowed_range=(-100, 100), method=random.randint):
    if seed is not None:
        random.seed(seed)

    for i in range(n):
        list.append((method(*allowed_range), method(*allowed_range)))
    return list

def list_bounds(list:list):
    x_max, x_min, y_max, y_min = 0, 0, 0, 0
    for i in list:
        (x, y) = i

        # new larger x value
        if x_max < x : x_max = x
        # new smaller x value
        if x_min > x : x_min = x

        # new larger y value
        if y_max < y : y_max = y
        # new smaller y value
        if y_min > y : y_min = y

    return [(x_min, y_min), (x_max, y_max)]

def furthest_point(list:list):
    x_max, y_max = 0, 0
    for i in list:
        (x, y) = i

        if x_max < x and y_max < y:
            x_max, y_max = x, y
        
        if x_max < x and y_max == y:
            x_max, y_max = x, y

        if x_max == x and y_max < y:
            x_max, y_max = x, y

    return (x_max, y_max)

def calculate_radius(point1:tuple, point2:tuple):
    (x1, y1), (x2, y2) = point1, point2
    w, h = (x2 - x1), (y2 - y1)
    return math.sqrt(w**2 + h**2)
