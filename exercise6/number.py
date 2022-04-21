# 12-Apr-2022
# Author- Kristaps Mihelsons
import random
from circle import Circle


def random_integer(min:int=-50, max:int=50) -> int:
    return random.randint(min, max)

def random_range(min:int=-50, max:int=50, dimensions:int=2, data:list=[]) -> list:
    return tuple([random_integer(min, max) for i in range(dimensions)])

def random_circles(count:int=1, center_range:tuple=(-50, 50), radius_range:tuple=(1, 10), data:list=[]):
    return [Circle(random_integer(*radius_range), random_range(*center_range)) for i in range(count)]