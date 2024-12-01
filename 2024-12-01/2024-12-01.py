import py5
import py5_tools


def setup():
    py5.size(500, 500)
    py5.background(0, 0, 0)


def draw():
    diameter = 10
    for i in range(50):
        for j in range(50):
            py5.fill(py5.random(255), py5.random(255), py5.random(255), 100)
            py5.circle(j * diameter, (i + j) * diameter, diameter)

    if py5.is_key_pressed and py5.key == "s":
        py5_tools.animated_gif("2024-12-01.gif", count=10, period=0.1, duration=0.1)


py5.run_sketch(block=False)
