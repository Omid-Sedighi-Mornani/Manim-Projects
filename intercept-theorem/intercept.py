from manim import *
import sys
import math

sys.path.append("/Users/omidsedighi-mornani/Desktop/mathe/PROJECTS")
from Library.m_creature import MCreature
from Library.list_utils import ExtendedMathTex, ExtendedVGroup, ExtendedText
from Library.extended_colors import *
from v_shape import VShape
from x_shape import XShape


class AbstractScene(Scene):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.camera.background_color = CREAM

        self.overview_title = MarkupText(
            "Die Strahlensätze", font="Patrick Hand", color=BROWN, font_size=64
        ).to_edge(UP)

        self.parallel_formula = ExtendedMathTex("g", "\parallel", "h", color=BROWN)

        self.first_formula = ExtendedMathTex(
            "{ZA", "\over", "ZA'}", "=", "{ZB", "\over", "ZB'}", color=BROWN
        ).to_edge(DOWN)

        self.second_formula = ExtendedMathTex(
            "{AB", "\over", "A'B'}", "=", "{ZB", "\over", "ZB'}", color=BROWN
        ).to_edge(DOWN)

        self.general_formula = ExtendedMathTex(
            "{kurz", "\over", "lang}", "=", "{kurz", "\over", "lang}", color=BROWN
        ).to_edge(DOWN)

        self.general_formula_reversed = ExtendedMathTex(
            "{lang", "\over", "kurz}", "=", "{lang", "\over", "kurz}", color=BROWN
        ).to_edge(DOWN)

        self.general_formula_flipped = ExtendedMathTex(
            "{kurz", "\over", "kurz}", "=", "{lang", "\over", "lang}", color=BROWN
        ).to_edge(DOWN)

        for formula in VGroup(
            self.first_formula, self.general_formula, self.second_formula
        ):
            formula[0, 4].set_color(OLIVE_GREEN)
            formula[2, 6].set_color(FIRE_RED)

        for formula in VGroup(
            self.general_formula_flipped, self.general_formula_reversed
        ):
            formula.set_color_by_tex("kurz", OLIVE_GREEN)
            formula.set_color_by_tex("lang", FIRE_RED)

        frame = SVGMobject("assets/whiteboard.svg")
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

        VGroup(self.first_formula, self.second_formula, self.parallel_formula).arrange(
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
            *[Write(element) for element in self.first_formula[[0, 4]]],
        )

        self.play(
            Indicate(
                VGroup(v_shape.ZA, v_shape.ZB, x_shape.ZA, x_shape.ZB), color=GREEN_A
            ),
            Indicate(self.first_formula[[0, 4]], color=GREEN_A),
        )

        self.play(Write(self.first_formula[[1, 3, 5]]))

        self.play(
            Create(v_shape.ZA_dash),
            Create(x_shape.ZA_dash),
            Create(v_shape.ZB_dash),
            Create(x_shape.ZB_dash),
            Write(self.first_formula[[2, 6]]),
        )

        self.play(
            Indicate(
                VGroup(
                    v_shape.ZA_dash, x_shape.ZA_dash, v_shape.ZB_dash, x_shape.ZB_dash
                ),
                color=RED_A,
            ),
            Indicate(self.first_formula[[2, 6]], color=RED_A),
        )

        self.play(
            Create(v_shape.AB), Create(x_shape.AB), Write(self.second_formula[[0, 4]])
        )
        self.play(
            Indicate(
                VGroup(v_shape.AB, x_shape.AB, v_shape.ZB, x_shape.ZB), color=GREEN_A
            ),
            Indicate(self.second_formula[[0, 4]], color=GREEN_A),
        )

        self.play(FadeIn(self.second_formula[1, 3, 5]))

        self.play(
            Create(v_shape.AB_dash),
            Create(x_shape.AB_dash),
            Write(self.second_formula[2, 6]),
        )
        self.play(
            Indicate(
                VGroup(
                    v_shape.AB_dash, x_shape.AB_dash, v_shape.ZB_dash, x_shape.ZB_dash
                ),
                color=RED_A,
            ),
            Indicate(self.second_formula[2, 6], color=RED_A),
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
            TransformMatchingShapes(short_label, self.general_formula[0]),
            FadeIn(self.general_formula[1]),
            TransformMatchingShapes(long_label, self.general_formula[2]),
        )

        self.play(FadeIn(self.general_formula[3]))

        self.play(
            TransformMatchingShapes(s, self.general_formula[4]),
            FadeIn(self.general_formula[5]),
            TransformMatchingShapes(l, self.general_formula[6]),
        )

        distances = ExtendedVGroup(
            v_shape.ZA, v_shape.ZA_dash, v_shape.ZB, v_shape.ZB_dash
        )

        for i in range(8, 16, 2):
            self.play(FadeIn(v_shape[i + 1]))

        for i, j in zip(range(0, 7, 2), range(4)):
            self.play(Indicate(distances[j], scale_factor=1.1))
            self.play(Transform(self.general_formula[i], self.first_formula[i]))
            self.wait()

        self.play(ReplacementTransform(self.general_formula, self.first_formula))

        self.play(
            FadeOut(v_shape[:20]),
            self.table.animate.scale(0.1).move_to(ORIGIN),
            self.first_formula.animate.scale(0.9).move_to(self.cell_locations[(2, 2)]),
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

        self.wait()
        self.play(
            self.table.animate.scale(10, about_point=self.cell_locations[(2, 3)]),
            ReplacementTransform(self.intercept_labels[1].copy(), title[:14]),
            FadeOut(self.overview_title),
            FadeOut(previous_formula),
            previous_formula.animate.scale(
                10, about_point=self.cell_locations[(2, 3)]
            ).set_opacity(0),
            FadeIn(title[14]),
            ReplacementTransform(self.shape_labels[0].copy(), title[15:]),
        )

        v_shape = VShape().move_to(ORIGIN)
        self.play(Create(v_shape[:2]))
        self.wait()

        self.play(Create(v_shape[2:4]), Write(v_shape[4:6]))

        self.wait()

        for i in range(6, 15, 2):
            self.play(Write(v_shape[i]))

        self.play(FadeIn(self.parallel_formula.to_edge(RIGHT)))

        short_label = (
            MathTex("kurz", color=OLIVE_GREEN)
            .next_to(v_shape.ZA, direction=DOWN)
            .shift(0.1 * LEFT)
        )

        long_label = MathTex("lang", color=FIRE_RED).next_to(
            v_shape.ray1, direction=DOWN, aligned_edge=RIGHT
        )

        self.play(Create(v_shape.ZB), Write(short_label))
        self.play(Create(v_shape.ZB_dash), Write(long_label))

        self.play(
            ReplacementTransform(v_shape.ZB.copy(), v_shape.AB),
            ReplacementTransform(v_shape.ZB_dash.copy(), v_shape.AB_dash),
            (s := short_label.copy()).animate.shift(1.5 * UP + 0.5 * LEFT),
            (l := long_label.copy()).animate.shift(1.5 * UP),
        )

        self.wait()

        self.play(
            TransformMatchingShapes(short_label, self.general_formula[0]),
            TransformMatchingShapes(long_label, self.general_formula[2]),
            FadeIn(self.general_formula[1]),
        )
        self.play(FadeIn(self.general_formula[3]))

        self.play(
            TransformMatchingShapes(s, self.general_formula[4]),
            TransformMatchingShapes(l, self.general_formula[6]),
            FadeIn(self.general_formula[5]),
        )

        distances = ExtendedVGroup(
            v_shape.AB, v_shape.AB_dash, v_shape.ZB, v_shape.ZB_dash
        )

        self.play(
            FadeIn(
                VGroup(
                    v_shape.label_A,
                    v_shape.label_B,
                    v_shape.label_A_dash,
                    v_shape.label_B_dash,
                    v_shape.label_Z,
                )
            )
        )

        for i, j in zip(range(0, 7, 2), range(4)):
            self.play(Indicate(distances[j], scale_factor=1.1))
            self.play(Transform(self.general_formula[i], self.second_formula[i]))
            self.wait()

        self.play(ReplacementTransform(self.general_formula, self.second_formula))
        self.play(
            self.table.animate.scale(0.1).move_to(ORIGIN),
            self.second_formula.animate.scale(0.9).move_to(self.cell_locations[(3, 2)]),
            previous_formula.animate.scale(0.1)
            .set_opacity(1)
            .move_to(self.cell_locations[(2, 2)]),
            FadeOut(v_shape),
            FadeTransform(title, self.overview_title),
            FadeOut(self.parallel_formula),
        )

        self.wait(3)


class ThirdScene(AbstractScene):
    def construct(self):
        previous_formulas = VGroup(
            self.first_formula.copy().scale(0.9).move_to(self.cell_locations[(2, 2)]),
            self.second_formula.copy().scale(0.9).move_to(self.cell_locations[(3, 2)]),
        )

        self.parallel_formula.to_edge(RIGHT)

        title = Text(
            "1.Strahlensatz - X-Figur", font="Patrick Hand", color=BROWN
        ).to_edge(UP)

        self.add(self.table, previous_formulas, self.overview_title)

        self.wait()
        self.play(
            self.table.animate.scale(10, about_point=self.cell_locations[(2, 3)]),
            previous_formulas.animate.scale(
                10, about_point=self.cell_locations[(2, 3)]
            ).set_opacity(0),
            FadeOut(self.overview_title),
            ReplacementTransform(self.intercept_labels[0].copy(), title[:14]),
            FadeIn(title[14]),
            ReplacementTransform(self.shape_labels[1].copy(), title[15:]),
        )

        x_shape = XShape().move_to(ORIGIN)
        self.play(Create(x_shape[:2]))
        self.play(Create(x_shape[2:4]))
        self.play(Write(x_shape[4:6]), Write(self.parallel_formula))
        self.play(FadeIn(x_shape[*range(6, 14 + 1, 2)]))

        short_label = MathTex("kurz", color=OLIVE_GREEN).next_to(
            x_shape.ZA, direction=UP
        )
        long_label = MathTex("lang", color=FIRE_RED).next_to(
            x_shape.ZA_dash, direction=DOWN
        )

        self.play(Create(x_shape.ZA), Create(x_shape.ZA_dash))
        self.play(FadeIn(VGroup(short_label, long_label)))

        self.play(Create(x_shape.ZB), Create(x_shape.ZB_dash))
        self.play(
            (s := short_label.copy()).animate.shift(1.3 * DOWN + 0.4 * RIGHT),
            (l := long_label.copy()).animate.shift(1.5 * UP + 0.3 * LEFT),
        )

        self.wait()

        self.play(
            TransformMatchingShapes(short_label, self.general_formula[0]),
            TransformMatchingShapes(long_label, self.general_formula[2]),
            TransformMatchingShapes(s, self.general_formula[4]),
            TransformMatchingShapes(l, self.general_formula[6]),
        )

        self.play(Write(self.general_formula[1, 3, 5]))

        self.play(FadeIn(x_shape[*range(7, 15 + 1, 2)]))

        distances = ExtendedVGroup(
            x_shape.ZA, x_shape.ZA_dash, x_shape.ZB, x_shape.ZB_dash
        )

        for i, j in zip(range(0, 7, 2), range(4)):
            self.play(Indicate(distances[j], scale_factor=1.2))
            self.play(Transform(self.general_formula[i], self.first_formula[i]))
            self.wait()

        self.play(ReplacementTransform(self.general_formula, self.first_formula))
        self.wait()

        self.play(
            self.table.animate.scale(0.1).move_to(ORIGIN),
            FadeOut(self.parallel_formula),
            FadeOut(x_shape[:-3]),
            self.first_formula.animate.scale(0.9).move_to(self.cell_locations[(2, 3)]),
            *[
                previous_formulas[idx]
                .animate.scale(0.1)
                .set_opacity(1)
                .move_to(self.cell_locations[position])
                for idx, position in enumerate([(2, 2), (3, 2)])
            ],
            FadeTransform(title, self.overview_title),
        )

        self.wait(3)


class FourthScene(AbstractScene):
    def construct(self):
        previous_formulas = ExtendedVGroup(
            self.first_formula.copy().scale(0.9).move_to(self.cell_locations[(2, 2)]),
            self.first_formula.copy().scale(0.9).move_to(self.cell_locations[(2, 3)]),
            self.second_formula.copy().scale(0.9).move_to(self.cell_locations[(3, 2)]),
        )
        self.add(self.table, self.overview_title, previous_formulas)

        title = Text(
            "2.Strahlensatz - X-Figur", font="Patrick Hand", color=BROWN
        ).to_edge(UP)

        self.play(
            self.table.animate.scale(10, about_point=self.cell_locations[(3, 3)]),
            ReplacementTransform(self.intercept_labels[1].copy(), title[:14]),
            FadeIn(title[14]),
            ReplacementTransform(self.shape_labels[1].copy(), title[15:]),
            FadeOut(self.overview_title),
            previous_formulas.animate.scale(
                10, about_point=self.cell_locations[(3, 3)]
            ).set_opacity(0),
        )

        self.wait()

        x_shape = XShape().move_to(ORIGIN)

        self.play(Create(x_shape[:4], run_time=2))
        self.play(FadeIn(x_shape[4:6], self.parallel_formula.to_edge(RIGHT)))
        self.play(FadeIn(x_shape[*range(6, 15 + 1)]))
        self.wait()

        self.play(Create(x_shape.ZB), Create(x_shape.AB))
        self.play(Create(x_shape.ZB_dash), Create(x_shape.AB_dash))
        self.play(FadeIn(self.general_formula))

        self.play(Indicate(x_shape.ZB), Indicate(x_shape.ZB_dash))
        self.play(
            ReplacementTransform(self.general_formula[4, 6], self.second_formula[4, 6])
        )

        self.wait()
        self.play(Indicate(x_shape.AB), Indicate(x_shape.AB_dash))
        self.play(
            ReplacementTransform(self.general_formula[0, 2], self.second_formula[0, 2])
        )
        self.play(ReplacementTransform(self.general_formula, self.second_formula))

        self.wait()
        second_formula_copy = self.second_formula.copy()

        self.play(
            self.second_formula[2, 6].animate.move_to(self.second_formula[0, 4]),
            self.second_formula[0, 4].animate.move_to(self.second_formula[2, 6]),
        )

        elements = [
            (x_shape.AB_dash, self.second_formula[2], RED_A),
            (x_shape.AB, self.second_formula[0], GREEN_A),
            (x_shape.ZB_dash, self.second_formula[6], RED_A),
            (x_shape.ZB, self.second_formula[4], GREEN_A),
        ]

        for shape_element, formula_element, color in elements:
            self.play(
                Indicate(shape_element, color=color),
                Indicate(formula_element, color=color, scale_factor=1.5),
            )
            self.wait()

        self.play(
            TransformMatchingTex(self.second_formula, self.general_formula_reversed)
        )

        self.play(
            self.general_formula_reversed[0].animate.move_to(
                self.general_formula_reversed[6]
            ),
            self.general_formula_reversed[6].animate.move_to(
                self.general_formula_reversed[0]
            ),
        )

        second_formula_flipped = ExtendedMathTex(
            "{ZB", "\over", "AB}", "=", "{ZB'", "\over", "AB'}", color=BROWN
        ).to_edge(DOWN)

        second_formula_flipped[0, 2].set_color(OLIVE_GREEN)
        second_formula_flipped[4, 6].set_color(FIRE_RED)

        elements = [
            (
                x_shape.ZB,
                self.general_formula_reversed[6],
                second_formula_flipped[0],
                GREEN_A,
            ),
            (
                x_shape.AB,
                self.general_formula_reversed[2],
                second_formula_flipped[2],
                GREEN_A,
            ),
            (
                x_shape.ZB_dash,
                self.general_formula_reversed[4],
                second_formula_flipped[4],
                RED_A,
            ),
            (
                x_shape.AB_dash,
                self.general_formula_reversed[0],
                second_formula_flipped[6],
                RED_A,
            ),
        ]

        for shape_element, source_element, target_element, color in elements:
            self.play(Indicate(shape_element, color=color))
            self.play(ReplacementTransform(source_element, target_element))
            self.wait()

        self.play(
            TransformMatchingTex(self.general_formula_reversed, second_formula_flipped)
        )

        self.wait()
        self.play(TransformMatchingTex(second_formula_flipped, second_formula_copy))

        self.play(
            self.table.animate.scale(0.1).move_to(ORIGIN),
            *[
                previous_formulas[idx]
                .animate.scale(0.1)
                .set_opacity(1)
                .move_to(self.cell_locations[position])
                for idx, position in enumerate([(2, 2), (2, 3), (3, 2)])
            ],
            FadeOut(x_shape),
            FadeOut(self.parallel_formula),
            second_formula_copy.animate.scale(0.9).move_to(self.cell_locations[(3, 3)]),
            FadeTransform(title, self.overview_title),
        )

        self.wait(3)
        self.play(
            Unwrite(
                self.table, previous_formulas, second_formula_copy, self.overview_title
            )
        )
        self.wait()


class EndScene(AbstractScene):
    def construct(self):
        mcreature = MCreature("BROWN")
        self.wait()
        self.play(FadeIn(mcreature))
        self.play(mcreature.speak("Danke für's Zuschauen!", font="Patrick Hand"))
        self.play(mcreature.blink_eyes())
        self.wait()
        self.play(mcreature.blink_eyes())
        self.play(
            mcreature.speak(
                "Bis zum nächsten Mal!", direction="DR", font="Patrick Hand"
            )
        )
        self.wait()
        self.play(mcreature.unspeak(), mcreature.unspeak())
        self.wait()
        self.play(mcreature.blink_eyes())
        self.play(mcreature.write_text())
        self.wait(2)
        self.play(FadeOut(mcreature), mcreature.unwrite_text())
        self.wait(3)


class SummaryScene(AbstractScene):
    def construct(self):
        pass


class Thumbnail(Scene):
    def construct(self):
        pass
