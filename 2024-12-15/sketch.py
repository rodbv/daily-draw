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
    py5.background(0)
    py5.frame_rate(10)


def draw():
    for row in range(9):
        color = rainbow[(py5.frame_count + row) % len(rainbow)]
        py5.stroke(color)
        draw_tape(row, shift_x=py5.frame_count)

    if py5.is_key_pressed and py5.key == "s":
        py5_tools.animated_gif("2024-12-15.gif", count=10, period=0.1, duration=0.1)


def draw_tape(row, shift_x):
    a = 0
    for i in range(100):
        py5.line(4 * i, row * 50, 4 * i, (row * 50) + 40 * py5.cos(a))
        a += py5.TWO_PI / 30


py5.run_sketch()
