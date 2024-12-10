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
    py5.stroke("lightgreen")
    py5.stroke_weight(1)


def draw():
    if py5.frame_count == py5.height:
        py5.no_loop()
        return

    for slot in range(1, 400, 40):
        py5.point(slot, py5.frame_count)
        py5.point(py5.frame_count, slot)


py5_tools.animated_gif("2024-12-10.gif", count=60, period=0.1, duration=0.1)
py5.run_sketch()
