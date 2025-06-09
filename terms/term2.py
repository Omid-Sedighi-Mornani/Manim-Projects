from manim import *
from MF_Tools import *
import sys

sys.path.append("/Users/omidsedighi-mornani/Desktop/mathe/PROJECTS")
from Library.m_creature import MCreature
from Library.list_utils import (
    ExtendedMathTex,
    ExtendedGroup,
    ExtendedVGroup,
)
from Library.extended_colors import *
from shapes import Boxes


class AbstractScene(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.camera.background_color = CREAM
        self.board = SVGMobject("assets/chalkboard2.svg").scale(2)
        self.add(self.board)

    def stretch_board(self):
        self.board.stretch_to_fit_height(
            config.frame_height * 1.1
        ).stretch_to_fit_width(config.frame_width * 1.1)


class IntroScene(AbstractScene):
    def construct(self):
        mcreature = MCreature(theme="BROWN")
        title = Text(
            "Vereinfache",
            font="Patrick Hand",
            color=BROWN,
            stroke_color=BROWN,
        ).to_edge(UP)

        terms = (
            ExtendedVGroup(
                ExtendedMathTex(r"2 \cdot (x + y)"),
                ExtendedMathTex(r"2 \cdot x + 2 \cdot y"),
            )
            .scale(1.5)
            .arrange(DOWN)
            .move_to(self.board)
            .set_color(WHITE)
        )

        terms[0][0][3].set_color(GREEN_A)
        terms[0][0][5].set_color(RED_A)
        terms[1][0][2].set_color(GREEN_A)
        terms[1][0][6].set_color(RED_A)

        self.play(Write(title))
        self.play(Write(terms[0]))
        self.wait()
        self.play(
            TransformByGlyphMap(
                terms[0],
                terms[1],
                ([0], [0, 4]),
                ([1], [1, 5]),
                ([2, 6], []),
                ([3], [2]),
                ([5], [6]),
                ([4], [3]),
                from_copy=True,
            )
        )
        self.play(FadeIn(mcreature))
        self.play(mcreature.blink_eyes())
        self.play(
            mcreature.speak(
                "Distribu-was??", direction="DR", duration=2, scale_factor=0.7
            )
        )

        self.wait()
        self.play(
            mcreature.unspeak(),
            Unwrite(title, run_time=1),
            self.board.animate(run_time=2)
            .stretch_to_fit_height(config.frame_height * 1.1)
            .stretch_to_fit_width(config.frame_width * 1.1),
            Unwrite(terms),
            FadeOut(mcreature),
        )
        self.wait(3)


class FirstScene(AbstractScene):
    def construct(self):

        self.stretch_board()
        title = Text("Das Distributivgesetz", font="Patrick Hand").to_edge(UP)

        general_formula = ExtendedMathTex("a \cdot (b + c) ")

        general_formula_simplified = ExtendedMathTex("= a \cdot b + a \cdot c")

        formula = (
            ExtendedVGroup(general_formula, general_formula_simplified)
            .scale(1.5)
            .arrange(RIGHT)
            .next_to(title, direction=DOWN, buff=1)
        )

        subtitle = Text("Konkretes Beispiel:", font="Patrick Hand").next_to(
            formula, direction=DOWN, buff=1
        )

        formula_example = (
            ExtendedVGroup(
                ExtendedMathTex("2 \cdot (3 + 4)"),
                ExtendedMathTex("= 2 \cdot 3 + 2 \cdot 4"),
            )
            .scale(1.5)
            .arrange(RIGHT)
            .next_to(subtitle, direction=DOWN, buff=0.5)
        )

        glyph_map = [
            ([0], [1], {"path_arc": -PI / 2}),
            ([0], [5], {"path_arc": -PI / 2, "delay": 4}),
            ([1], [2], {"path_arc": PI / 2, "delay": 1}),
            ([1], [6], {"path_arc": PI / 2, "delay": 5}),
            ([2, 6], []),
            ([3], [3], {"path_arc": PI / 2, "delay": 2}),
            ([4], [4], {"path_arc": PI / 2, "delay": 3}),
            ([5], [7], {"path_arc": PI / 2, "delay": 6}),
            ([], [0]),
        ]

        self.play(Write(title))
        self.wait()
        self.play(Write(general_formula))
        self.wait()
        self.play(Wiggle(general_formula[0][0]))
        self.play(Wiggle(general_formula[0][3]), Wiggle(general_formula[0][5]))
        self.play(
            TransformByGlyphMap(
                general_formula,
                general_formula_simplified,
                *glyph_map,
                from_copy=True,
                run_time=12,
            )
        )

        surr_rect = SurroundingRectangle(formula, color=WHITE, buff=0.25)

        self.play(DrawBorderThenFill(surr_rect))

        self.play(Write(subtitle))
        self.wait()
        self.play(Write(formula_example[0]))
        self.wait()
        self.play(
            TransformByGlyphMap(
                formula_example[0],
                formula_example[1],
                *glyph_map,
                from_copy=True,
                run_time=10,
            )
        )

        self.wait()

        title_transformed = Text(
            "Das Distributivgesetz - eine Visualisierung", font="Patrick Hand"
        ).to_edge(UP)

        self.play(
            FadeOut(formula, subtitle),
            ReplacementTransform(title, title_transformed[:20]),
            FadeIn(title_transformed[20:]),
            formula_example.animate.next_to(title_transformed, direction=DOWN, buff=1),
        )

        boxes_short = Boxes(
            width=3,
            height=2,
            side_length=0.75,
            fill_opacity=1,
            buff=0.1,
            show_labels=True,
        )

        boxes_long = Boxes(
            width=4,
            height=2,
            side_length=0.75,
            fill_opacity=1,
            buff=0.1,
            show_labels=True,
        )

        boxes = (
            VGroup(boxes_short, boxes_long)
            .arrange(RIGHT, buff=2)
            .next_to(formula_example, direction=DOWN, buff=1)
        )

        formula_example_copy = ExtendedVGroup(
            ExtendedMathTex("2 \cdot (3 + 4)"),
            ExtendedMathTex("2 \cdot 3 + 2 \cdot 4"),
        ).scale(1.3)

        for f in formula_example_copy:
            f.to_edge(DOWN, buff=0.75)

        boxes_united = Boxes(
            width=7,
            height=2,
            side_length=0.75,
            fill_opacity=1,
            buff=0.1,
        )

        self.play(FadeIn(boxes_short))
        self.play(
            ReplacementTransform(
                formula_example[1][0][1:4].copy(), formula_example_copy[1][0][0:3]
            )
        )
        self.wait()
        self.play(
            ReplacementTransform(
                formula_example[1][0][4].copy(), formula_example_copy[1][0][3]
            )
        )
        self.play(FadeIn(boxes_long))
        self.play(
            ReplacementTransform(
                formula_example[1][0][5:].copy(), formula_example_copy[1][0][4:]
            )
        )

        self.play(
            boxes_short[-1].animate.set_color(BLUE),
            boxes_long[-1].animate.set_color(BLUE),
            formula_example_copy[1][0][2, 6].animate.set_color(BLUE_A),
        )
        self.play(
            boxes_short[:, 0].animate.set_color(RED),
            boxes_long[:, 0].animate.set_color(RED),
            formula_example_copy[1][0][0, 4].animate.set_color(RED_A),
        )

        self.wait()
        self.play(*[box.hide_labels() for box in boxes])

        self.play(
            boxes.animate.arrange(RIGHT, buff=0.1).next_to(
                formula, direction=DOWN, buff=1
            )
        )
        boxes_united.move_to(boxes)
        boxes_united.label_width = Tex("(3+4)")
        boxes_united[-1].set_color(BLUE)
        boxes_united[:, 0].set_color(RED)
        self.play(FadeTransform(boxes, boxes_united))
        self.play(boxes_united.show_labels())

        glyph_map_reversed = [
            ([0, 4], [0]),
            ([1, 5], [1]),
            ([], [2, 6]),
            ([2], [3]),
            ([3], [4]),
            ([6], [5]),
        ]

        formula_example_copy[0][0][0].set_color(RED_A)
        formula_example_copy[0][0][3, 5].set_color(BLUE_A)
        self.play(
            TransformByGlyphMap(
                formula_example_copy[1], formula_example_copy[0], *glyph_map_reversed
            )
        )
        self.wait()

        formula_example_simplified = (
            MathTex("2 \cdot 7").scale(1.3).to_edge(DOWN, buff=1)
        )
        formula_example_simplified[0][0].set_color(RED_A)
        formula_example_simplified[0][2].set_color(BLUE_A)

        formula_example_finished = MathTex(14).scale(1.3).to_edge(DOWN, buff=1)
        self.play(
            TransformByGlyphMap(
                formula_example_copy[0],
                formula_example_simplified,
                ([0], [0]),
                ([1], [1]),
                ([2, 3, 4, 5, 6], [2]),
            )
        )
        self.wait()
        self.play(
            TransformMatchingTex(formula_example_simplified, formula_example_finished)
        )
        self.wait()
        self.play(
            ExtendedGroup(*self.mobjects).animate.scale(0.5).to_corner(UR, buff=1)
        )

        mcreature = MCreature(theme="BROWN")
        self.play(FadeIn(mcreature))
        self.play(mcreature.move_iris(UR))
        self.play(
            mcreature.speak(
                "Ausmultiplizieren ist ja einfach!",
                scale_factor=0.7,
                direction="DR",
                duration=2,
            )
        )
        self.play(mcreature.move_iris(DL))
        self.play(mcreature.blink_eyes())
        self.play(mcreature.unspeak())
        self.play(mcreature.blink_eyes())
        self.play(
            mcreature.speak(
                "Wie funktioniert dann Ausklammern?",
                scale_factor=0.7,
                direction="DR",
                duration=2,
            )
        )

        self.play(
            FadeOut(surr_rect, boxes_united),
            Unwrite(formula_example_finished),
            Unwrite(formula_example),
            Unwrite(title_transformed),
        )
        self.play(
            FadeOut(mcreature),
            mcreature.unspeak(),
            self.board.animate(run_time=2)
            .stretch_to_fit_width(config.frame_width * 1.1)
            .stretch_to_fit_height(config.frame_height * 1.1)
            .move_to(ORIGIN),
        )
        self.wait(3)


class SecondScene(AbstractScene):
    def construct(self):
        self.stretch_board()

        title = Text(
            "Das Distributivgesetz - Ausklammern", font="Patrick Hand"
        ).to_edge(UP)

        term_example = ExtendedVGroup(
            ExtendedMathTex("2", "\cdot", "x", "+", "2", "\cdot", "y"),
            ExtendedMathTex("2", "\cdot", "(", "x", "+", "y", ")"),
        ).scale(1.5)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(term_example[0]))
        self.wait()
        self.play(term_example[0][0, 4].animate.set_color(YELLOW))
        self.play(
            Wiggle(term_example[0][0]),
            Wiggle(term_example[0][4]),
        )

        arcs = VGroup(
            CurvedArrow(
                term_example[1][0].get_top(),
                term_example[1][3].get_top(),
                color=BLUE_E,
                angle=-PI / 2,
            ),
            CurvedArrow(
                term_example[1][0].get_top(),
                term_example[1][5].get_top(),
                color=RED_E,
                angle=-PI / 2,
            ),
        )

        term_example[1][0].set_color(YELLOW)
        term_example.save_state()

        self.play(
            ReplacementTransform(
                term_example[0][0, 4], term_example[1][0], path_arc=PI / 2
            ),
            ReplacementTransform(term_example[0][1, 5], term_example[1][1]),
            ReplacementTransform(term_example[0][2], term_example[1][3]),
            ReplacementTransform(term_example[0][3], term_example[1][4]),
            ReplacementTransform(term_example[0][6], term_example[1][5]),
            FadeIn(term_example[1][2, 6]),
        )

        self.wait()
        self.play(FadeIn(arcs))
        self.wait()
        self.play(Restore(term_example), FadeOut(term_example[1]), FadeOut(arcs))
        self.wait()
        self.play(Unwrite(term_example[0]))

        variable_term = ExtendedMathTex("2", "x", "+", "3", "x").scale(1.5)
        variable_term_simplified = ExtendedMathTex("(", "2", "+", "3", ")", "x").scale(
            1.5
        )
        variable_term_finished = ExtendedMathTex("5", "x").scale(1.5)

        variable_term_simplified[-1].set_color(YELLOW)
        variable_term_finished[-1].set_color(YELLOW)

        self.play(FadeIn(variable_term))
        self.play(variable_term[1, 4].animate.set_color(YELLOW))
        self.play(
            ReplacementTransform(
                variable_term[0, 2, 3], variable_term_simplified[1, 2, 3]
            ),
            ReplacementTransform(
                variable_term[1, 4], variable_term_simplified[5], path_arc=PI / 2
            ),
            FadeIn(variable_term_simplified[0, 4]),
        )
        self.wait(2)
        self.play(
            TransformMatchingTex(
                variable_term_simplified,
                variable_term_finished,
                transform_mismatches=True,
            )
        )

        self.wait()

        self.play(Unwrite(variable_term_finished))

        transformed_title = Text(
            "Ausklammern mit Potenzen", font="Patrick Hand"
        ).to_edge(UP)

        self.play(
            ReplacementTransform(title[21:], transformed_title[:11]),
            FadeOut(title[:21]),
            FadeIn(transformed_title[11:]),
        )

        variable_term = ExtendedMathTex("x", "^2", "+", "3", "x").scale(1.5)
        variable_term_simplified = ExtendedMathTex(
            "x", "\cdot", "x", "+", "3", "\cdot", "x"
        ).scale(1.5)
        variable_term_finished = ExtendedMathTex(
            "x", "\cdot", "(", "x", "+", "3", ")"
        ).scale(1.5)

        self.play(FadeIn(variable_term))
        self.wait()
        self.play(Indicate(variable_term[0]))
        self.play(TransformMatchingTex(variable_term, variable_term_simplified))
        self.wait()

        variable_term_finished[0].set_color(YELLOW)
        self.play(variable_term_simplified[2, 6].animate.set_color(YELLOW))
        self.play(
            ReplacementTransform(
                variable_term_simplified[2, 6], variable_term_finished[0]
            ),
            ReplacementTransform(
                variable_term_simplified[0, 3, 4], variable_term_finished[3, 4, 5]
            ),
            ReplacementTransform(
                variable_term_simplified[1, 5], variable_term_finished[1]
            ),
            FadeIn(variable_term_finished[2, 6]),
        )
        self.wait()

        self.play(FadeOut(variable_term_finished, shift=UP))

        complex_term = ExtendedMathTex(
            "r", "^2", "+", "3", "r", "^3", "-", "7", "r", "^2", "s"
        ).scale(1.5)

        complex_term_simplified = ExtendedMathTex(
            "r", "^2", "(", "1", "+", "3", "r", "-", "7", "s", ")"
        ).scale(1.5)

        self.wait()
        self.play(Write(complex_term))

        self.wait()
        self.play(complex_term[0, 1, 4, 5, 8, 9].animate.set_color(YELLOW))
        self.wait()
        complex_term_simplified[0, 1, 6].set_color(YELLOW)
        complex_term_simplified.shift(DOWN)

        self.play(complex_term.animate.shift(UP))

        divided_bys = VGroup(
            *[
                MathTex("\over", "r", "^2")
                .set_color(RED_A)
                .scale(1.5)
                .next_to(mob, direction=DOWN)
                for mob in [complex_term[0, 1], complex_term[4, 5], complex_term[8, 9]]
            ]
        )

        for divided_by in divided_bys:
            self.play(FadeIn(divided_by, shift=0.5 * DOWN))

        self.play(
            ReplacementTransform(
                complex_term[0, 1, 4, 8, 9].copy(),
                complex_term_simplified[0, 1],
            )
        )
        self.play(FadeIn(complex_term_simplified[2, -1]))
        self.play(
            ReplacementTransform(
                ExtendedVGroup(complex_term[0, 1], divided_bys[0]).copy(),
                complex_term_simplified[3],
            )
        )
        self.play(
            ReplacementTransform(complex_term[2].copy(), complex_term_simplified[4])
        )
        self.play(
            ReplacementTransform(complex_term[3].copy(), complex_term_simplified[5]),
            ReplacementTransform(
                ExtendedVGroup(complex_term[4, 5], divided_bys[1]).copy(),
                complex_term_simplified[6],
            ),
        )
        self.play(
            ReplacementTransform(
                complex_term[6, 7].copy(), complex_term_simplified[7, 8]
            )
        )
        self.play(
            ReplacementTransform(complex_term[-1].copy(), complex_term_simplified[-2])
        )

        self.wait()

        formula = ExtendedVGroup(
            complex_term, MathTex("=").scale(1.5), complex_term_simplified
        )

        self.play(
            FadeOut(divided_bys), FadeIn(formula[1]), formula.animate.arrange(RIGHT)
        )

        self.wait(2)

        mcreature = MCreature(theme="BROWN").to_corner(DL)
        self.play(
            ExtendedGroup(*self.mobjects).animate.scale(0.5).to_corner(UR, buff=1)
        )

        self.play(FadeIn(mcreature))

        self.play(
            mcreature.speak("Zu schwer?", direction="DR", scale_factor=0.6, duration=2)
        )
        self.play(mcreature.blink_eyes())
        self.play(
            mcreature.speak(
                "Nicht\nschlimm!", direction="UR", scale_factor=0.6, duration=2
            )
        )
        self.play(mcreature.blink_eyes())

        self.wait()

        self.play(
            Unwrite(formula),
            FadeOut(transformed_title),
            mcreature.unspeak(),
            mcreature.unspeak(),
        )

        self.wait(3)


class EndScene(AbstractScene):
    def construct(self):
        self.stretch_board()
        self.board.scale(0.5).to_corner(UR, buff=1)
        mcreature = MCreature(theme="BROWN").to_corner(DL)
        self.add(mcreature)
        self.play(mcreature.blink_eyes())
        self.play(
            mcreature.speak(
                "Hier ein paar Aufgaben zum Üben!",
                direction="DR",
                scale_factor=0.6,
                duration=2,
            )
        )

        titles = ExtendedVGroup(
            Text("Klammere aus:", font="Patrick Hand"),
            Text("Multipliziere aus:", font="Patrick Hand"),
        ).scale(0.6)

        exclude_formulas = (
            ExtendedVGroup(
                ExtendedMathTex("6x + 9"), ExtendedMathTex("4xy - 8x^2 + 12x")
            )
            .scale(0.75)
            .arrange(DOWN, buff=0.1)
        )

        multiply_formulas = (
            ExtendedVGroup(ExtendedMathTex("3(x+5)"), ExtendedMathTex("-x(x+y)"))
            .scale(0.75)
            .arrange(DOWN, buff=0.1)
        )

        titles[0].move_to(self.board.get_top() + 0.5 * DOWN, aligned_edge=UP)
        exclude_formulas.next_to(titles[0], direction=DOWN)
        titles[1].next_to(exclude_formulas, direction=DOWN)
        multiply_formulas.next_to(titles[1], direction=DOWN)

        self.play(Write(titles[0]))
        self.play(Write(exclude_formulas), mcreature.blink_eyes())
        self.wait()
        self.play(Write(titles[1]))
        self.play(Write(multiply_formulas), mcreature.blink_eyes())

        self.play(mcreature.blink_eyes())
        self.wait()
        self.play(mcreature.blink_eyes())

        self.play(
            FadeOut(self.board, run_time=2),
            Unwrite(exclude_formulas),
            Unwrite(multiply_formulas),
            FadeOut(titles),
            mcreature.unspeak(),
        )

        self.play(
            mcreature.speak("Bis zum nächsten Mal!", scale_factor=0.6, duration=2)
        )
        self.play(mcreature.raise_eyebrows(func=there_and_back_with_pause, duration=3))
        self.wait()
        self.play(mcreature.blink_eyes())
        self.play(mcreature.write_text(duration=2))
        self.play(mcreature.unspeak(duration=2))
        self.play(mcreature.blink_eyes())
        self.wait()
        self.play(mcreature.blink_eyes())

        self.wait(3)


class Thumbnail(AbstractScene):
    def construct(self):
        self.stretch_board()
        self.board.scale(0.5).to_corner(UR, buff=1)

        text = MarkupText(
            "Willst du das\n<u>endlich verstehen?</u>", font="Patrick Hand", color=BROWN
        ).to_corner(UL)
        title = Text("Klammere aus:", font="Patrick Hand").scale(1.5)
        term = MathTex("x", "^2", "+", "2", "x").scale(1.5)
        term.set_color_by_tex("x", DARK_BROWN)

        title.move_to(self.board.get_top() + DOWN)
        term.move_to(self.board.get_center())

        mcreature = MCreature(theme="BROWN").to_corner(DL)
        mcreature.static_move_eyebrows(direction=UP)
        mcreature.add_speech("Wie geht das??", scale_factor=0.8, direction="DR")

        self.add(mcreature, title, term, text)
