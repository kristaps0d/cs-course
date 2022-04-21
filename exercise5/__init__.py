from random import seed
from tkinter import X
from view import ViewWidget
import calculations as calc

if __name__ == '__main__':
    viewport = ViewWidget(500, 500)

    points = calc.list_comprehension(n=10, allowed_range=(-150, 150))
    bounds = calc.list_bounds(points)

    viewport.draw_points(points, color=(0, 255, 100))
    viewport.draw_rectangle(*bounds, color=(255, 100, 0))
    print('Taisnstūra stūri', *bounds, f': (S: {abs(bounds[0][0]-bounds[1][0]) * abs(bounds[0][1]-bounds[1][1])}px)')

    furthest_point = calc.furthest_point(points)
    radius = calc.calculate_radius((0, 0), furthest_point)
    viewport.draw_circle((0, 0), radius)
    print(radius)

    viewport.interrupt_loop()
