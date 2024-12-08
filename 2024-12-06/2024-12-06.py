import random

import py5


def setup():
    py5.size(600, 600)
    py5.background(255)
    draw_maze(0, 0, py5.width, py5.height)


def draw_maze(x, y, width, height):
    if width > 10 and height > 10:
        py5.fill(
            py5.color(
                random.choice(  # wow so Mondrian-esque
                    [
                        "red",
                        "blue",
                        "yellow",
                        "white",
                        "black",
                    ]
                )
            )
        )
        py5.no_stroke()
        py5.rect(x, y, width, height)

        if py5.random(1) > 0.5:
            py5.stroke(0)
            py5.line(x, y + height / 2, x + width, y + height / 2)
            draw_maze(x, y, width, height / 2)
            draw_maze(x, y + height / 2, width, height / 2)
        else:
            py5.stroke(0)
            py5.line(x + width / 2, y, x + width / 2, y + height)
            draw_maze(x, y, width / 2, height)
            draw_maze(x + width / 2, y, width / 2, height)


py5.run_sketch()
