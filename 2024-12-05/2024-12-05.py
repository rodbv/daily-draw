import py5
import py5_tools

global iter


def setup():
    py5.size(500, 500)
    py5.background(0)
    py5.stroke_weight(0)
    global iter
    iter = 0


def draw():
    global iter
    iter += 1
    idx = 0
    for col in range(0, 600, 85):
        for row in range(0, 500, 45):
            draw_rainbow(col - 22.5 if row % 2 == 0 else col, row, iter + idx)
            idx += 1

    if py5.is_key_pressed and py5.key == "s":
        py5_tools.animated_gif("2024-12-05.gif", count=30, duration=0.1)


def draw_rainbow(x, y, black_pos):
    rainbow = [
        "#000000",
        "#70369d",
        "#4b369d",
        "#487de7",
        "#79c314",
        "#faeb36",
        "#ffa500",
        "#e81416",
    ]

    rainbow[black_pos % len(rainbow)] = "#000000"

    for radius in range(90, 10, -10):
        py5.fill(rainbow.pop())
        py5.circle(x, y, radius)


py5.run_sketch(block=False)
