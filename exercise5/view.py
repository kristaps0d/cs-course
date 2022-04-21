import turtle

class ViewWidget(object):
    def __init__(self, width=400, height=400):
        self.turtle = turtle.Turtle(shape='square')
        self.screen = turtle.Screen()
        self.dimensions = (width, height)

        self.screen.setup(*self.dimensions)
        self.screen.colormode(255)
        self.turtle.shapesize(0.2)
        self.turtle.speed(0)

    def draw_points(self, list:list, color:tuple=(0, 0, 0), size:int=1):
        for i in list:
            (x, y) = i
            self.draw_point(x, y, color, size)

    def draw_points_intesect(self, list:list, size:int=1):
        for i in list:
            (x, y) = i

    def draw_rectangle(self, point1:tuple, point2:tuple, color:tuple=(0, 0, 0), size:int=1):
        (x1, y1), (x2, y2) = point1, point2
        self.draw_line((x1, y1), (x1, y2), color, size)
        self.draw_line((x1, y2), (x2, y2), color, size)
        self.draw_line((x2, y2), (x2, y1), color, size)
        self.draw_line((x2, y1), (x1, y1), color, size)

    def draw_circle(self, center:tuple=(0, 0), radius:int=0, color:tuple=(0, 0, 0), size:int=1):
        (x, y) = center

        self.turtle.goto(x, y-radius)
        self.turtle.circle(radius)


    def draw_line(self, point1:tuple, point2:tuple, color:tuple=(0, 0, 0), size:int=1):
        self.turtle.penup()
        self.turtle.goto(*point1)
        self.turtle.color(color)
        self.turtle.pensize(size)
        self.turtle.pendown()
        self.turtle.goto(*point2)

    def draw_point(self, x:int, y:int, color:tuple=(0, 0, 0), size:int=1):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.color(color)
        self.turtle.pensize(size)
        self.turtle.stamp()

    def interrupt_loop(self):
        while True:
            try:
                pass
            except KeyboardInterrupt:
                break
    