from manim import *
import sys

sys.path.append("/Users/omidsedighi-mornani/Desktop/mathe/PROJECTS")
from Library.m_creature import MCreature
from Library.list_utils import *
from v_shape import VShape
from x_shape import XShape


class TestScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        x_shape = XShape()
        self.add(x_shape)
