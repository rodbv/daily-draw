import py5
import py5_tools


def setup():
    py5.size(500, 500)
    py5.background(0, 0, 0)


def draw():
    diameter = 10
    for row in range(50):
        for col in range(50):
            py5.fill(row % 255, col % 255, row * col % 255, 100)
            py5.circle(col * diameter, row * diameter, diameter)

    if py5.is_key_pressed and py5.key == "s":
        # save on current dir of script
        py5.save_frame("2024-12-02.png")


py5.run_sketch(block=False)
