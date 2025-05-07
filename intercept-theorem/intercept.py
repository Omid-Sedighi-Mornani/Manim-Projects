from manim import *
import sys
import math

sys.path.append("/Users/omidsedighi-mornani/Desktop/mathe/PROJECTS")
from Library.m_creature import MCreature
from Library.list_utils import ExtendedMathTex, ExtendedVGroup, ExtendedText
from v_shape import VShape
from x_shape import XShape

BROWN = ManimColor("#4e3629")
OLIVE_GREEN = ManimColor("#6b8e23")
FIRE_RED = ManimColor("#f44336")


class AbstractScene(Scene):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.camera.background_color = "#fdf6e3"

        self.overview_title = MarkupText(
            "Die Strahlensätze", font="Patrick Hand", color=BROWN, font_size=64
        ).to_edge(UP)

        self.parallel_formula = ExtendedMathTex("g", "\parallel", "h", color=BROWN)

        frame = SVGMobject("assets/test.svg")
        frame.stretch_to_fit_height(config.frame_height)
        frame.stretch_to_fit_width(config.frame_width)
        frame.set_z_index(-99)

        self.intercept_labels = ExtendedVGroup(
            Text("1. Strahlensatz", font="Patrick Hand", color=BROWN),
            Text("2.Strahlensatz", font="Patrick Hand", color=BROWN),
        )

        self.shape_labels = ExtendedVGroup(
            Text("V-Figur", font="Patrick Hand", color=BROWN),
            Text("X-Figur", font="Patrick Hand", color=BROWN),
        )

        self.table = Table(
            [["", ""], ["", ""]],
            row_labels=list(self.intercept_labels),
            col_labels=list(self.shape_labels),
            top_left_entry=Text("Varianten", font="Patrick Hand", color=BROWN),
        ).set_color(BROWN)

        # Get the locations of the cells in the table
        self.cell_locations = {
            (row, col): self.table.get_cell((row, col)).get_center()
            for row in range(1, len(self.intercept_labels) + 2)
            for col in range(1, len(self.shape_labels) + 2)
        }

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

        VGroup(first_formula, second_formula, self.parallel_formula).arrange(
            LEFT, buff=1
        ).to_edge(DOWN)

        VGroup(v_shape, x_shape).arrange(LEFT, buff=1)

        self.play(
            Write(self.overview_title), Create(v_shape.ray1), Create(v_shape.ray2)
        )
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
            ),
            Indicate(second_formula[2, 6], color=RED_A),
        )

        self.play(
            ReplacementTransform(v_shape.label_line1.copy(), self.parallel_formula[0]),
            ReplacementTransform(x_shape.label_line1.copy(), self.parallel_formula[0]),
            FadeIn(self.parallel_formula[1]),
            ReplacementTransform(v_shape.label_line2.copy(), self.parallel_formula[2]),
            ReplacementTransform(x_shape.label_line2.copy(), self.parallel_formula[2]),
        )

        self.wait(3)


class FirstScene(AbstractScene):
    def construct(self):
        title = Text(
            "1. Strahlensatz - V-Figur", font="Patrick Hand", color=BROWN
        ).to_edge(UP)
        self.play(Write(self.table))
        self.wait()
        self.play(
            self.table.animate.scale(10, about_point=self.cell_locations.get((2, 2))),
            ReplacementTransform(self.intercept_labels[0].copy(), title[0:14]),
            ReplacementTransform(self.shape_labels[0].copy(), title[15:]),
            FadeIn(title[14]),
        )

        v_shape = VShape().move_to(ORIGIN)

        self.play(Create(v_shape[:2]))
        self.play(FadeIn(v_shape.Z), FadeIn(v_shape.label_Z))

        ray1_label = ExtendedText("Strahl", color=BROWN, font="Patrick Hand").next_to(
            v_shape.ray1, direction=DOWN
        )
        ray2_label = (
            ray1_label.copy()
            .rotate(45 * DEGREES)
            .next_to(v_shape.ray2, direction=LEFT, buff=-1)
        )

        self.play(Write(ray1_label), Write(ray2_label))
        self.wait(2)
        self.play(Unwrite(ray1_label), Unwrite(ray2_label))

        self.play(Create(v_shape[2:4]))

        line_label = Text("Gerade", color=BROWN, font="Patrick Hand").next_to(
            v_shape.line1, direction=DOWN, aligned_edge=LEFT
        )

        self.play(Write(line_label))
        self.wait(2)
        self.play(FadeTransform(line_label, v_shape[4:6]))

        self.parallel_formula.to_edge(RIGHT, buff=2)

        self.play(
            ReplacementTransform(v_shape[4:6].copy(), self.parallel_formula[0, 2]),
            FadeIn(self.parallel_formula[1]),
        )

        for i in range(8, 16, 2):
            self.play(FadeIn(v_shape[[i]]))

        short_label = (
            MathTex("kurz", color=OLIVE_GREEN)
            .next_to(v_shape.ZA, direction=DOWN)
            .shift(0.1 * LEFT)
        )

        long_label = MathTex("lang", color=FIRE_RED).next_to(
            v_shape.ray1, direction=DOWN, aligned_edge=RIGHT
        )

        general_formula = ExtendedMathTex(
            "{kurz", "\over", "lang}", "=", "{kurz", "\over", "lang}", color=BROWN
        )

        first_formula = ExtendedMathTex(
            "{ZA", "\over", "ZA'}", "=", "{ZB", "\over", "ZB'}", color=BROWN
        ).to_edge(DOWN)

        for formula in VGroup(first_formula, general_formula):
            formula[0, 4].set_color(OLIVE_GREEN)
            formula[2, 6].set_color(FIRE_RED)

        general_formula.to_edge(DOWN)
        first_formula.move_to(general_formula)

        self.play(Create(v_shape.ZA))
        self.play(Write(short_label))
        self.wait()
        self.play(Create(v_shape.ZA_dash))
        self.play(Write(long_label))

        self.play(
            Create(v_shape.ZB),
            Create(v_shape.ZB_dash),
            (s := short_label.copy()).animate.shift(1.5 * UP).shift(0.5 * LEFT),
            (l := long_label.copy()).animate.shift(2 * UP),
        )

        self.wait()

        self.play(
            TransformMatchingShapes(short_label, general_formula[0]),
            FadeIn(general_formula[1]),
            TransformMatchingShapes(long_label, general_formula[2]),
        )

        self.play(FadeIn(general_formula[3]))

        self.play(
            TransformMatchingShapes(s, general_formula[4]),
            FadeIn(general_formula[5]),
            TransformMatchingShapes(l, general_formula[6]),
        )

        distances = ExtendedVGroup(
            v_shape.ZA, v_shape.ZA_dash, v_shape.ZB, v_shape.ZB_dash
        )

        for i in range(8, 16, 2):
            self.play(FadeIn(v_shape[i + 1]))

        for i, j in zip(range(0, 7, 2), range(4)):
            self.play(Indicate(distances[j], scale_factor=1.1))
            self.play(Transform(general_formula[i], first_formula[i]))
            self.wait()

        self.play(ReplacementTransform(general_formula, first_formula))

        self.play(
            FadeOut(v_shape[:20]),
            self.table.animate.scale(0.1).move_to(ORIGIN),
            first_formula.animate.scale(0.9).move_to(self.cell_locations[(2, 2)]),
            FadeTransform(title, self.overview_title),
            FadeOut(self.parallel_formula),
        )

        self.wait(3)


class SecondScene(AbstractScene):
    def construct(self):
        title = Text(
            "2.Strahlensatz - V-Figur", font="Patrick Hand", color=BROWN
        ).to_edge(UP)
        previous_formula = (
            ExtendedMathTex(
                "{ZA", "\over", "ZA'}", "=", "{ZB", "\over", "ZB'}", color=BROWN
            )
            .scale(0.9)
            .move_to(self.cell_locations[(2, 2)])
        )

        previous_formula[0, 4].set_color(OLIVE_GREEN)
        previous_formula[2, 6].set_color(FIRE_RED)
        self.add(self.table, self.overview_title, previous_formula)
        self.play(
            self.table.animate.scale(10, about_point=self.cell_locations[(2, 3)]),
            Transform(self.intercept_labels[1], title[:14]),
            FadeOut(self.overview_title),
            FadeOut(previous_formula),
            FadeIn(title[14]),
            Transform(self.shape_labels[0], title[15:]),
        )
        self.wait(3)


class SummaryScene(AbstractScene):
    def construct(self):
        pass


class Thumbnail(Scene):
    def construct(self):
        pass
