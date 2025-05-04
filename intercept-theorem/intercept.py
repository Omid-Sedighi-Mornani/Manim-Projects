from manim import *
import sys
import math

sys.path.append("/Users/omidsedighi-mornani/Desktop/mathe/PROJECTS")
from Library.m_creature import MCreature
from Library.list_utils import ExtendedMathTex
from v_shape import VShape
from x_shape import XShape

BROWN = ManimColor("#4e3629")
OLIVE_GREEN = ManimColor("#6b8e23")
FIRE_RED = ManimColor("#f44336")


class AbstractScene(Scene):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.camera.background_color = "#fdf6e3"

        frame = SVGMobject("assets/test.svg")
        frame.stretch_to_fit_height(config.frame_height)
        frame.stretch_to_fit_width(config.frame_width)

        self.add(frame)


class IntroScene(AbstractScene):
    def construct(self):

        v_shape = VShape(
            ray_color=BROWN,
            dot_color=DARK_BROWN,
            short_line_color=OLIVE_GREEN,
            long_line_color=FIRE_RED,
        )
        x_shape = XShape(
            ray_color=BROWN,
            dot_color=DARK_BROWN,
            short_line_color=OLIVE_GREEN,
            long_line_color=FIRE_RED,
        )

        title = MarkupText(
            "Die Strahlensätze", font="Patrick Hand", color=BROWN, font_size=64
        ).to_edge(UP)

        first_formula = ExtendedMathTex(
            "{ZA", "\over", "ZA'}", "=", "{ZB", "\over", "ZB'}", color=BROWN
        ).to_edge(DOWN)

        second_formula = ExtendedMathTex(
            "{AB", "\over", "A'B'}", "=", "{ZB", "\over", "ZB'}", color=BROWN
        )

        colors = [OLIVE_GREEN, FIRE_RED, OLIVE_GREEN, FIRE_RED]
        indices = [0, 2, 4, 6]
        for index, color in zip(indices, colors):
            first_formula[index].set_color(color)
            second_formula[index].set_color(color)

        parallel_formula = MathTex("g", "\parallel", "h", color=BROWN)

        VGroup(first_formula, second_formula, parallel_formula).arrange(
            LEFT, buff=1
        ).to_edge(DOWN)

        VGroup(v_shape, x_shape).arrange(LEFT, buff=1)

        self.play(Write(title), Create(v_shape.ray1), Create(v_shape.ray2))
        self.play(Create(v_shape.line1), Create(v_shape.line2))
        self.play(
            FadeIn(v_shape.dots), FadeIn(v_shape.label_line1, v_shape.label_line2)
        )

        self.play(
            ReplacementTransform(v_shape.dots.copy(), x_shape.dots.copy()),
            ReplacementTransform(v_shape.line1.copy(), x_shape.line1),
            ReplacementTransform(v_shape.line2.copy(), x_shape.line2),
            ReplacementTransform(v_shape.ray1.copy(), x_shape.ray1),
            ReplacementTransform(v_shape.ray2.copy(), x_shape.ray2),
            ReplacementTransform(v_shape.label_line1.copy(), x_shape.label_line1),
            ReplacementTransform(v_shape.label_line2.copy(), x_shape.label_line2),
        )

        self.play(
            Create(v_shape.ZA),
            Create(x_shape.ZA),
            Create(v_shape.ZB),
            Create(x_shape.ZB),
            *[Write(element) for element in first_formula[[0, 4]]],
        )

        self.play(
            Indicate(
                VGroup(v_shape.ZA, v_shape.ZB, x_shape.ZA, x_shape.ZB), color=GREEN_A
            ),
            Indicate(first_formula[[0, 4]], color=GREEN_A),
        )

        self.play(Write(first_formula[[1, 3, 5]]))

        self.play(
            Create(v_shape.ZA_dash),
            Create(x_shape.A_dash),
            Create(v_shape.ZB_dash),
            Create(x_shape.ZB_dash),
            Write(first_formula[[2, 6]]),
        )

        self.play(
            Indicate(
                VGroup(
                    v_shape.ZA_dash, x_shape.ZA_dash, v_shape.ZB_dash, x_shape.ZB_dash
                ),
                color=RED_A,
            ),
            Indicate(first_formula[[2, 6]], color=RED_A),
        )

        self.play(Create(v_shape.AB), Create(x_shape.AB), Write(second_formula[[0, 4]]))
        self.play(
            Indicate(
                VGroup(v_shape.AB, x_shape.AB, v_shape.ZB, x_shape.ZB), color=GREEN_A
            ),
            Indicate(second_formula[[0, 4]], color=GREEN_A),
        )

        self.play(FadeIn(second_formula[1, 3, 5]))

        self.play(
            Create(v_shape.AB_dash),
            Create(x_shape.AB_dash),
            Write(second_formula[2, 6]),
        )
        self.play(
            Indicate(
                VGroup(
                    v_shape.AB_dash, x_shape.AB_dash, v_shape.ZB_dash, x_shape.ZB_dash
                ),
                color=RED_A,
            )
        )

        self.play(
            ReplacementTransform(v_shape.label_line1.copy(), parallel_formula[0]),
            ReplacementTransform(x_shape.label_line1.copy(), parallel_formula[0]),
            FadeIn(parallel_formula[1]),
            ReplacementTransform(v_shape.label_line2.copy(), parallel_formula[2]),
            ReplacementTransform(x_shape.label_line2.copy(), parallel_formula[2]),
        )

        self.wait(3)


class FirstScene(AbstractScene):
    def construct(self):
        pass


class SecondScene(AbstractScene):
    def construct(self):
        pass


class SummaryScene(AbstractScene):
    def construct(self):
        pass


class Thumbnail(Scene):
    def construct(self):
        pass
