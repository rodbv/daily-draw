import py5

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
    for row in range(9):
        color = rainbow[row % 7]
        py5.stroke(color)
        draw_tape(row)


def draw():
    if py5.is_key_pressed and py5.key == "s":
        py5.save_frame("2024-12-08.png")


def draw_tape(row):
    a = 0
    for i in range(100):
        py5.line(4 * i, row * 50, 4 * i, (row * 50) + 40 * py5.cos(a))
        a += py5.TWO_PI / 30


py5.run_sketch()
