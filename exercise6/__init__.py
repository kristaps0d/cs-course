# 12-Apr-2022
# Author- Kristaps Mihelsons

import enum
from cv2 import circle
from circle import Circle
import number

print('''
         ╔╗   ╔╗
         ║║   ║║
╔══╦╦═╦══╣║╔══╣║
║╔═╬╣╔╣╔═╣║║║═╬╝
║╚═╣║║║╚═╣╚╣║═╬╗
╚══╩╩╝╚══╩═╩══╩╝
''')

circles = number.random_circles(12)
min_dist_index = None

for i, circle in enumerate(circles):
    distance = circle.distance()

    if min_dist_index is None:
        min_dist_index = i
        
    if distance < circles[min_dist_index].distance():
        min_dist_index = i

    print(f'Circle {i}:{" ":^5} {circle}')

print(f'\nClosest circle to the center {min_dist_index}: {circles[min_dist_index]}')

circle = number.random_circles(1)[0]
print(circle)