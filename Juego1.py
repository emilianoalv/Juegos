from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    radius = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5 / 2
    goto(start.x + radius, start.y)
    setheading(0)
    circle(radius)

    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    goto(end.x, start.y)  # Draw base
    goto((start.x + end.x) / 2, end.y)  # Draw peak
    goto(start.x, start.y)  # Return to base start

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'n')
onkey(lambda: color('white'), 'w')
onkey(lambda: color('green'), 'v')
onkey(lambda: color('blue'), 'a')
onkey(lambda: color('red'), 'q')
onkey(lambda: color('yellow'), 'y')  # Nuevo color amarillo
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
