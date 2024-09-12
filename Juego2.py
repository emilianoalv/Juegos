from turtle import *
from random import randrange,choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Colores posibles
colores = ['blue', 'green', 'yellow', 'purple', 'orange']

# Colores aleatorios
color_serpiente= choice(colores)
color_comida = choice([color for color in colores if color != color_serpiente])

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def mover_comida():
    mover_direccion = choice([vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)])  # Movimiento al azar
    posicion_nueva = food + mover_direccion
    
    if inside(posicion_nueva):  # Verifica que la comida está dentro de los límites
        food.move(mover_direccion)

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color_serpiente)

    square(food.x, food.y, 9, color_comida)

    update()
    mover_comida()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
