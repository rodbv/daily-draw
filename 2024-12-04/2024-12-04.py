import py5


def setup():
    py5.size(500, 500)
    py5.background(0)
    py5.stroke_weight(0)


def draw():
    for col in range(0, 600, 85):
        for row in range(0, 500, 45):
            draw_rainbow(col - 22.5 if row % 2 == 0 else col, row)

    if py5.is_key_pressed and py5.key == "s":
        print("Saving")
        py5.save_frame("2024-12-04.png")

    py5.no_loop()


def draw_rainbow(x, y):
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

    for radius in range(90, 10, -10):
        py5.fill(rainbow.pop())
        py5.circle(x, y, radius)


py5.run_sketch(block=False)
