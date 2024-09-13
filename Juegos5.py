

from random import *
from turtle import *
from freegames import path


# Preparación de los tiles y estado
car = path('car.gif')
tiles = list(range(8)) * 2  # Lista de 8 pares de números
state = {'mark': None}
hide = [True] * 16  # Grid 4x4
tap_count = 0  # Contador de taps


# Definir una lista de colores
colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'brown', 'cyan']


def square(x, y):
    """Dibuja un cuadrado blanco con contorno negro en (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convierte coordenadas (x, y) en el índice del cuadro."""
    return int((x + 100) // 50 + ((y + 100) // 50) * 4)


def xy(count):
    """Convierte el índice del cuadro en coordenadas (x, y)."""
    return (count % 4) * 50 - 100, (count // 4) * 50 - 100


def get_tile_color(tile):
    """Devuelve el color asociado a un tile específico."""
    return colors[tile % len(colors)]  # Asigna color basado en el número


def tap(x, y):
    """Actualiza la marca y destapa los cuadros según el tap."""
    global tap_count
    tap_count += 1  # Incrementar contador de taps
    print(f'Tap count: {tap_count}')  # Mostrar el número de taps
    spot = index(x, y)
    mark = state['mark']


    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


    # Verificar si todos los cuadros se han destapado
    if all(not h for h in hide):
        print("¡Todos los cuadros han sido revelados!")


def draw():
    """Dibuja la imagen y los cuadros."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()


    # Dibujar los cuadros y números/tiles
    for count in range(16):  # Grid 4x4
        if hide[count]:
            x, y = xy(count)
            square(x, y)


    mark = state['mark']


    # Dibujar el número cuando se selecciona una ficha
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 15, y + 5)
        tile_color = get_tile_color(tiles[mark])  # Obtener el color basado en el número
        color(tile_color)
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))


    update()
    ontimer(draw, 100)


# Inicializar el juego
shuffle(tiles)
setup(220, 220, 370, 0)  # Ajustado para cuadrícula 4x4
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

