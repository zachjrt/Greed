import pyray

from shared.color import Color
from shared.point import Point

pyray.init_window(800, 600, "Greed")
pyray.set_target_fps(60)

pyray.draw_text('Hello', 400, 300, 12, Color(255, 255, 255))