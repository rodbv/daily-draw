import py5


def setup():
    global diameter

    py5.size(500, 500)
    py5.background(255, 120, 44)
    diameter = 1


def draw():
    global diameter

    if py5.is_key_pressed and py5.key == "s":
        py5.save_frame("####.png")
        print("Saved!")

    if not py5.is_mouse_pressed:
        return

    diameter += 1

    py5.fill(py5.random(255), py5.random(255), py5.random(255), 100)
    py5.circle(py5.mouse_x, py5.mouse_y, diameter % 100)


py5.run_sketch()
