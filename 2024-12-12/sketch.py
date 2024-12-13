import py5
import random
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
    py5.background("white")
    py5.stroke("green")
    py5.stroke_weight(0)
    py5.fill("green")
    py5.frame_rate(10)

    # randomize positions
    global positions
    positions = []
    for _ in range(50):
        positions.append((py5.random_int(400), py5.random_int(400)))


def draw():
    global positions
    for x, y in positions:
        draw_tree(x, y)


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


py5_tools.animated_gif("2024-12-09.gif", count=20, period=0.1, duration=0.1)
py5.run_sketch()
