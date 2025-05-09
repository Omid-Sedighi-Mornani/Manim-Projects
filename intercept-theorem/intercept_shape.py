from manim import *
import sys

sys.path.append("/Users/omidsedighi-mornani/Desktop/mathe/PROJECTS")
from Library.list_utils import ExtendedVGroup
from Library.extended_colors import *


class InterceptShape(ExtendedVGroup):
    def __init__(
        self,
        ray_color=BROWN,
        short_line_color=OLIVE_GREEN,
        long_line_color=FIRE_RED,
        dot_color=DARK_BROWN,
        *args,
        **kwargs
    ):
        self.ray_color = ray_color
        self.short_line_color = short_line_color
        self.long_line_color = long_line_color
        self.dot_color = dot_color
        super().__init__(*args, **kwargs)
