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
    py5.frame_rate(10)
    py5.background(0)
    py5.stroke_weight(0)


def draw():
    for y in range(10):
        py5.stroke(rainbow[y % len(rainbow)])
        py5.fill(rainbow[y % len(rainbow)])
        draw_line(50 * y)


def draw_line(y):
    prev_y = y
    up = True
    for x in range(0, py5.width, 2):
        if up:
            new_y = prev_y + py5.random_int(7)
        else:
            new_y = prev_y - py5.random_int(7)

        py5.line(x, prev_y, x + 2, new_y)
        prev_y = new_y
        up = not up


py5_tools.animated_gif("2024-12-09.gif", count=100, period=0.1, duration=0.1)
py5.run_sketch()
