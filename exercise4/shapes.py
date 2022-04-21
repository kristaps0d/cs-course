import turtle

t = turtle.Turtle()
t.pensize(1)

x, y = t.screen.screensize()
x_mid, y_mid = (x // 2), (y // 2)

# trijsturis
def trijsturis(t):
    t.pendown()
    t.fd(300)
    t.lt((90 - 65) + 90)

    t.fd(175)
    t.lt((90 - 80) + 90)

    t.fd(278)
    t.lt((90 - 35) + 90)
    t.penup()
    t.fd(350)

# bulta
def bulta(t):
    t.pendown()
    t.fd(100)
    t.rt(90)
    t.fd(30)
    t.lt(135)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(135)
    t.fd(30)
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(85)
    t.lt(90)
    t.penup()


# plakne
def plakne(t, home=(0, 0)):
    # first centering
    t.penup()
    t.goto(home)
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.pendown()
    t.goto((home[0] + 200, home[1]))
    t.stamp()
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.goto(home)
    t.goto((home[0], home[1] + 200))
    t.setheading(90)
    t.stamp()
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.goto(home)
    t.setheading(0)
    t.goto((home[0] - 200, home[1]))
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.goto(home)
    t.goto((home[0], home[1] - 200))
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')
    t.penup()

    t.goto((home[0] + 200, home[1] - 200))
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.goto((home[0] + 200, home[1] + 200))
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.goto((home[0] - 200, home[1] + 200))
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.goto((home[0] - 200, home[1] - 200))
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.goto(home)

def piecsturis(t, home=(0, 0)):
    # first centering
    t.penup()
    t.pensize(2)
    t.goto(home)
    
    t.goto((home[0] - 50, home[1] - 50))
    
    t.pendown()
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.goto((home[0] + 50, home[1] - 50))
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.goto((home[0] + 81, home[1] + 45))
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.goto((home[0], home[1] + 103))
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.goto((home[0] - 81, home[1] + 45))
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.goto((home[0] - 50, home[1] - 50))
    t.write(f'({t.pos()[0]:.0f}, {t.pos()[1]:.0f})')

    t.penup()
    t.pensize(1)
    t.goto(home)

if __name__ == '__main__':
    home = (-100, -200)

    plakne(t, home)
    piecsturis(t, home)



while True:
    try:
        pass
    except KeyboardInterrupt:
        quit()
