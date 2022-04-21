import turtle, numpy as np
from PIL import Image

t = turtle.Turtle(shape='square')

t.speed(0)
t.shapesize(0.1)

screen = turtle.Screen()
screen.setup(500, 500)

# really slow code,
# but a fun idea
# turtle library is sloow

def divide_pixels():
    width, height = t.screen.screensize()
    return (width, height)

def px_coords(pos=(0, 0)):
    width, height = divide_pixels()
    x_mid, y_mid = (width // 2), (height // 2)
    x, y = pos

    # convert fixed position to a relative one
    rel_x, rel_y = (x - x_mid), (y - y_mid)
    return (rel_x, rel_y)

def return_home():
    # move logic
    t.penup()
    t.end_fill()
    t.goto(px_coords((0, 0)))

def draw_pixel(position, color="red"):
    x, y = position

    # move logic
    t.penup()
    t.end_fill()
    t.goto(x, y)

    t.color(color)
    t.stamp()

def test_grid():
    # simple grid
    for x in [0, 50, 100, 150, 200, 250, 300, 350, 400]:
        draw_pixel(px_coords((x, 100)), "red")

    for y in [0, 50, 100, 150, 200, 250, 300, 350, 400]:
        draw_pixel(px_coords((50, y)), "red")

    # pixel resolution test
    for x in range(divide_pixels()[0]//2+1):
        color ='red'

        # draw pixels
        if x % 2 == 0:
            color = 'green'
        
        draw_pixel(px_coords((x, 200)), color)

def img_to_array(link):
    img = Image.open(link)
    arr_img = np.asarray(img)
    return arr_img


def draw_array(array):
    screen.colormode(255)
    t.pensize(2)
    max_y = len(array)

    for y, y_data in enumerate(array):
        for x, x_data in enumerate(y_data):
            color = tuple(x_data)
            draw_pixel(px_coords((x, max_y-y)), color)

def run():
    print("To close app, press ctrl + c in console!")
    
    test_grid()
    draw_array(img_to_array('./image.jpg'))

    return_home()
    while True:
        try:
            pass
        except KeyboardInterrupt:
            quit()