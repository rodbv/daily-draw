import random

import py5
import py5_tools

rainbow = [
    "#70369d",
    "#4b369d",
    "#487de7",
    "#79c314",
    "#faeb36",
    "#ffa500",
    "#e81416",
]


def setup():
    py5.size(400, 400)
    py5.stroke("green")
    py5.stroke_weight(0)
    py5.fill("green")
    py5.frame_rate(10)

    # randomize positions
    global positions
    positions = []
    for _ in range(80):
        positions.append((py5.random_int(400), py5.random_int(400)))


def draw():
    global positions
    py5.background("white")
    for x, y in positions:
        draw_tree(x, y)
    draw_snow()
    draw_snowman()


def draw_snow():
    for _ in range(100):
        x = py5.random_int(400)
        y = py5.random_int(400)
        if py5.random(1) > 0.5:
            py5.fill("white")
        else:
            py5.fill("lightgray")
        py5.circle(x, y, 2)


def draw_snowman():
    # Body
    py5.fill("white")
    py5.circle(200, 300, 30)
    py5.circle(200, 275, 25)
    py5.circle(200, 255, 20)

    # Eyes
    py5.fill("black")
    py5.circle(195, 255, 2)
    py5.circle(205, 255, 2)

    # nose
    py5.fill("orange")
    py5.circle(200, 258, 2)

    # Arms
    py5.stroke("brown")
    py5.stroke_weight(1)
    py5.line(185, 275, 175, 265)
    py5.line(215, 275, 225, 265)

    py5.stroke_weight(0)

    # Hat
    py5.fill("black")
    py5.rect(185, 245, 30, 3)
    py5.rect(190, 235, 20, 10)


def draw_tree(x, y):
    py5.fill("brown")
    py5.square(x - 5, y + 30, 10)
    py5.fill("green")
    draw_triangle(x, y)
    draw_triangle(x, y + 7)
    draw_triangle(x, y + 14)
    py5.fill(random.choice(rainbow))
    py5.circle(x, y, 4)


def draw_triangle(x, y):
    py5.triangle(x, y, x - 10, y + 20, x + 10, y + 20)


py5_tools.animated_gif("2024-12-12.gif", count=20, period=0.1, duration=0.1)
py5.run_sketch()
