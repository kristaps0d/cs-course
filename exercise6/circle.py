# 12-Apr-2022
# Author- Kristaps Mihelsons
import math, random

class Circle(object):
    def __init__(self, radius:float, center:list=[0, 0]):
        self.radius, self.center = radius, center

    def area(self) -> float:
        return (math.pi * math.pow(self.radius, 2))

    def circumfrance(self) -> float:
        return (2 * math.pi * self.radius)

    def distance(self, point2:tuple=(0, 0)) -> float:
        (x1, y1), (x2, y2) = self.center, point2
        x, y = abs(x2 - x1), abs(y2 - y1)
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    def __setattr__(self, name: str, value:any) -> None:
        self.__dict__[name] = value

    def __getattr__(self, name: str) -> any:
        return self.__dict__[name]

    def __repr__(self) -> str:
        return f'({self.center}, {self.radius})'

    def get_x(self):
        return self.center[0]

    def get_y(self):
        return self.center[1]

    def get_radius(self):
        return self.radius