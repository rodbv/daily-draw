import py5
import py5_tools


def setup():
    py5.size(500, 500)
    py5.background(0, 0, 0)
    py5.stroke_weight(2)


def draw():
    # draw a senoid

    py5.fill(255, 0, 0)

    for i in range(-20, 20):
        py5.stroke(0, py5.random(255), 0)
        for x in range(0, 500, 10):
            y = (i * 50) + 100 * py5.sin(py5.radians(x))
            py5.point(x, y)

    if py5.is_key_pressed and py5.key == "s":
        py5_tools.animated_gif("2024-12-03.gif", count=10, period=0.1, duration=0.1)


py5.run_sketch(block=False)
