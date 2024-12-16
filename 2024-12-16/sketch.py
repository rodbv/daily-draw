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
    py5.no_fill()
    py5.frame_rate(10)


def draw():
    py5.background(0)
    num_curves = 10
    spacing = py5.height / (num_curves + 1)
    for i in range(num_curves):
        py5.stroke(rainbow[i % len(rainbow)])
        y = (i + 1) * spacing
        py5.bezier(
            0,
            y,
            py5.width / 3,
            y + random.uniform(-50, 50),
            2 * py5.width / 3,
            y + random.uniform(-50, 50),
            py5.width,
            y,
        )

    if py5.is_key_pressed and py5.key == "s":
        py5_tools.animated_gif("2024-12-16.gif", count=10, period=0.1, duration=0.1)


py5.run_sketch()
