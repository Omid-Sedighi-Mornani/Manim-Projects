from manim import *
import sys

sys.path.append("/Users/omidsedighi-mornani/Desktop/mathe/PROJECTS")
from Library.m_creature import MCreature


class FundamentalScene(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.camera.background_color = GRAY_D

    def clear_mobjects(self):
        self.play(FadeOut(Group(*self.mobjects)))


class IntroScene(FundamentalScene):
    def construct(self):
        binomialFormulas = VGroup(
            MathTex(
                "(",
                "a",
                "+",
                "b",
                ")",
                "^{2}",
                "=",
                "a",
                "^{2}",
                "+",
                "2",
                "a",
                "b",
                "+",
                "b",
                "^{2}",
            ),
            MathTex(
                "(",
                "a",
                "-",
                "b",
                ")",
                "^{2}",
                "=",
                "a",
                "^{2}",
                "-",
                "2",
                "a",
                "b",
                "+",
                "b",
                "^{2}",
            ),
            MathTex(
                "(",
                "a",
                "+",
                "b",
                ")",
                "(",
                "a",
                "-",
                "b",
                ")",
                "=",
                "a",
                "^{2}",
                "-",
                "b",
                "^{2}",
            ),
        )

        binomialFormulas.arrange(DOWN)
        self.play(FadeIn(binomialFormulas[0]))

        self.play(Transform(binomialFormulas[0].copy(), binomialFormulas[1]))

        self.play(
            Transform(binomialFormulas[0][:5].copy(), binomialFormulas[2][:5]),
            Transform(binomialFormulas[1][:5].copy(), binomialFormulas[2][5:10]),
        )

        self.play(FadeIn(binomialFormulas[2][10]))

        self.play(
            Transform(binomialFormulas[1][7:10].copy(), binomialFormulas[2][11:14]),
            Transform(binomialFormulas[0][14:16].copy(), binomialFormulas[2][14:16]),
        )

        self.play(
            *[
                formula.animate.set_color_by_tex("a", BLUE).set_color_by_tex(
                    "b", ORANGE
                )
                for formula in binomialFormulas
            ]
        )

        orders = VGroup(
            *[
                MathTex(f"{i+1}.").next_to(binomialFormulas[i], direction=LEFT)
                for i in range(3)
            ]
        )
        title = MarkupText(
            "Die <span color='#bbb'>binomischen</span> Formeln",
            font="Helvetica",
            font_size=48,
        ).shift(2 * UP)
        self.play(FadeIn(orders))
        self.play(Write(title))
        mcreature = MCreature(theme="GRAY")
        self.play(DrawBorderThenFill(mcreature))
        self.play(mcreature.blink_eyes())
        self.play(mcreature.move_iris(direction=UR))
        self.wait(2)
        self.play(mcreature.speak("??", direction="DR", size=40))
        self.wait()
        self.play(mcreature.move_iris(direction=DOWN))

        for _ in range(4):
            self.wait()
            self.play(mcreature.blink_eyes())

        self.clear_mobjects()
        self.wait(2)


class Binom1Scene(FundamentalScene):
    def construct(self):

        title = MarkupText(
            "1. <span color='#bbb'>binomische</span> Formel", font="Helvetica"
        ).to_edge(UP)
        self.play(Write(title))
        a_square = Square(side_length=2, color=BLUE, fill_opacity=0.5).shift(0.5 * DL)
        a_label_down = MathTex("a", color=BLUE).next_to(a_square, direction=DOWN)
        a_label_left = MathTex("a", color=BLUE).next_to(a_square, direction=LEFT)
        a_square_label = MathTex("a^2", color=BLUE).move_to(a_square.get_center())
        ab_right = Rectangle(
            width=1, height=1e-3, color=ORANGE, fill_opacity=0.5
        ).next_to(a_square, RIGHT, aligned_edge=DOWN, buff=0)
        ab_up = Rectangle(width=1e-3, height=1, color=ORANGE, fill_opacity=0.5).next_to(
            a_square, direction=UP, aligned_edge=LEFT, buff=0
        )
        b_label_up = MathTex("b", color=ORANGE).next_to(ab_up, direction=LEFT)
        b_label_right = MathTex("b", color=ORANGE).next_to(
            ab_right, direction=DOWN, buff=0.5
        )
        b_label_right.shift(
            ab_right.get_bottom() - b_label_right.get_bottom() + 0.5 * DOWN
        )
        self.play(DrawBorderThenFill(a_square))
        self.play(FadeIn(a_label_down, a_label_left))
        self.play(Write(a_square_label))
        self.play(Write(ab_up), Write(ab_right))
        self.play(Write(b_label_right), Write(b_label_up))
        self.play(
            ab_right.animate.stretch_to_fit_height(a_square.height).align_to(
                a_square, direction=DOWN
            ),
            ab_up.animate.stretch_to_fit_width(a_square.width).align_to(
                a_square, direction=LEFT
            ),
        )

        ab_label_up = MathTex("ab", color=ORANGE).move_to(ab_up)
        ab_label_right = ab_label_up.copy().move_to(ab_right)
        self.play(Write(ab_label_right), Write(ab_label_up))
        b_length = ValueTracker(0)
        b_square = always_redraw(
            lambda: Square(
                side_length=b_length.get_value(), color=GREEN, fill_opacity=0.5
            ).next_to(ab_up, direction=RIGHT, aligned_edge=DOWN, buff=0)
        )
        self.add(b_square)
        self.play(b_length.animate.set_value(1))
        b_square_label = MathTex("b^2", color=GREEN).move_to(b_square)
        self.play(Write(b_square_label))

        ab_brace_left = Brace(VGroup(a_square, ab_up), direction=LEFT, buff=0.7)
        text_brace_left = ab_brace_left.get_tex("a+b")
        ab_brace_down = Brace(VGroup(a_square, ab_right), direction=DOWN, buff=0.7)
        text_brace_down = ab_brace_down.get_tex("a+b")

        self.play(
            Write(ab_brace_left),
            Write(ab_brace_down),
            Write(text_brace_left),
            Write(text_brace_down),
        )
        self.wait(2)
        self.play(
            Unwrite(ab_brace_down),
            Unwrite(ab_brace_left),
            Unwrite(text_brace_down),
            Unwrite(text_brace_left),
        )

        binom_unformed_1 = MathTex(
            "(",
            "a",  # 1
            "+",
            "b",  # 3
            ")",
            "(",
            "a",  # 6
            "+",
            "b",  # 8
            ")",  # 9
            "=",
            "a^2",  # 11
            "+",
            "ab",  # 13
            "+",
            "ab",  # 15
            "+",
            "b^2",  # 17
        ).to_edge(edge=DOWN)
        binom_1 = MathTex(
            "(",
            "a",  # 1
            "+",
            "b",  # 3
            ")",
            "^2",
            "=",
            "a^2",  # 11
            "+",
            "2ab",  # 15
            "+",
            "b^2",  # 17
        ).move_to(binom_unformed_1)

        for tex, color in [
            ("a", BLUE),
            ("b", ORANGE),
            ("ab", ORANGE),
            ("b^2", GREEN),
            ("a^2", BLUE),
        ]:
            binom_unformed_1.set_color_by_tex(tex, color)
            binom_1.set_color_by_tex(tex, color)

        self.play(
            ReplacementTransform(a_label_left.copy(), binom_unformed_1[1]),
            ReplacementTransform(b_label_up.copy(), binom_unformed_1[3]),
            FadeIn(binom_unformed_1[2]),
            ReplacementTransform(a_label_down.copy(), binom_unformed_1[6]),
            ReplacementTransform(b_label_right.copy(), binom_unformed_1[8]),
            FadeIn(binom_unformed_1[7]),
        )

        self.play(FadeIn(VGroup(*[binom_unformed_1[i] for i in [0, 4, 5, 9]])))

        self.play(FadeIn(binom_unformed_1[10]))
        self.play(ReplacementTransform(a_square_label.copy(), binom_unformed_1[11]))
        self.play(
            ReplacementTransform(ab_label_up.copy(), binom_unformed_1[13]),
            ReplacementTransform(ab_label_right.copy(), binom_unformed_1[15]),
            FadeIn(binom_unformed_1[12]),
            FadeIn(binom_unformed_1[14]),
        )
        self.play(
            FadeIn(binom_unformed_1[16]),
            ReplacementTransform(b_square_label.copy(), binom_unformed_1[17]),
        )
        self.play(TransformMatchingTex(binom_unformed_1, binom_1))
        self.wait(3)

        self.clear_mobjects()


class Binom2Scene(FundamentalScene):
    def construct(self):

        title = MarkupText(
            "2. <span color='#bbb'>binomische</span> Formel", font="Helvetica"
        ).to_edge(UP)

        self.play(Write(title))
        a_square = Square(side_length=3, color=GRAY_B)
        a_square_label = MathTex("a^2", color=GRAY_B).move_to(a_square)
        a_brace_left = Brace(a_square, direction=LEFT, buff=0.7, color=GRAY_B)
        text_brace_left = a_brace_left.get_tex("a").set_color(GRAY_B)

        a_brace_down = Brace(a_square, direction=DOWN, buff=0.7, color=GRAY_B)
        text_brace_down = a_brace_down.get_tex("a").set_color(GRAY_B)

        self.play(Create(a_square))
        self.play(Write(a_square_label))
        self.play(Write(a_brace_left), Write(text_brace_left))
        self.play(Write(a_brace_down), Write(text_brace_down))

        ab_down = Rectangle(
            width=1, height=1e-3, color=ORANGE, fill_opacity=0.3
        ).next_to(a_square, direction=LEFT, aligned_edge=DOWN, buff=-1)
        b_label_down = MathTex("b", color=ORANGE).next_to(ab_down, direction=DOWN)
        ab_left = Rectangle(
            width=1e-3, height=1, color=ORANGE, fill_opacity=0.3
        ).next_to(
            a_square,
            direction=LEFT,
            aligned_edge=UP,
            buff=0,
        )
        b_label_left = MathTex("b", color=ORANGE).next_to(ab_left, direction=LEFT)
        self.play(Create(ab_down), Create(ab_left))
        self.play(Write(b_label_down), Write(b_label_left))
        self.play(
            ab_down.animate.stretch_to_fit_height(a_square.height).align_to(
                a_square, direction=DOWN
            ),
            ab_left.animate.stretch_to_fit_width(a_square.width).align_to(
                a_square, direction=LEFT
            ),
        )

        ab_label_left = MathTex("ab", color=ORANGE).move_to(ab_left)
        ab_label_down = MathTex("ab", color=ORANGE).move_to(ab_down)
        self.play(Write(ab_label_down), Write(ab_label_left))
        self.play(Unwrite(a_square_label))

        b_square = Square(side_length=1, color=GREEN, fill_opacity=0.1).next_to(
            a_square,
            direction=LEFT,
            aligned_edge=UP,
            buff=-1,
        )
        b_square_label = MathTex("b^2", color=GREEN_E).move_to(b_square)
        self.play(Write(b_square_label), FadeIn(b_square))

        a_min_b_square = Square(side_length=2, color=BLUE, fill_opacity=0.3).next_to(
            a_square, direction=RIGHT, aligned_edge=DOWN, buff=-2
        )
        a_min_b_label_down = MathTex("(a-b)", color=BLUE).next_to(
            a_min_b_square, direction=DOWN
        )
        a_min_b_label_right = MathTex("(a-b)", color=BLUE).next_to(
            a_min_b_square, direction=RIGHT
        )

        a_min_b_label_down.shift(
            a_min_b_square.get_bottom() - a_min_b_label_down.get_bottom() + 0.65 * DOWN
        )

        a_min_b_square_label = MathTex("(a-b)^2", color=BLUE).move_to(a_min_b_square)

        self.play(FadeIn(a_min_b_square))
        self.play(Write(a_min_b_label_down), Write(a_min_b_label_right))
        self.play(Write(a_min_b_square_label))
        self.play(FadeOut(title))
        self.play(VGroup(*self.mobjects).animate.to_edge(UP))
        scale_factor = 0.7
        a_min_b = VGroup(a_min_b_square, a_min_b_square_label)
        a = VGroup(a_square, MathTex("a^2", color=GRAY_B).move_to(a_square))
        self.add(a_square_label)
        ab_d = VGroup(ab_down, ab_label_down)
        ab_l = VGroup(ab_left, ab_label_left)
        b = VGroup(b_square, b_square_label)
        binom_2_graphic = (
            VGroup(
                a_min_b.copy().scale(scale_factor),
                MathTex("="),
                a.copy().scale(scale_factor),
                MathTex("-"),
                ab_d.copy().scale(scale_factor),
                MathTex("-"),
                ab_l.copy().scale(scale_factor),
                MathTex("+"),
                b.copy().scale(scale_factor),
            )
            .arrange(RIGHT)
            .to_edge(DOWN)
        )

        self.play(ReplacementTransform(a_min_b.copy(), binom_2_graphic[0]))

        for idx, obj in enumerate(VGroup(a, ab_d, ab_l, b).copy()):
            self.play(FadeIn(binom_2_graphic[2 * idx + 1]))
            self.play(ReplacementTransform(obj, binom_2_graphic[2 * (idx + 1)]))

        binom_unformed_2 = MathTex(
            "(a-b)^2", "=", "a^2", "-", "ab", "-", "ab", "+", "b^2"
        ).move_to(binom_2_graphic)

        binom_2 = MathTex("(a-b)^2", "=", "a^2", "-", "2", "ab", "+", "b^2").move_to(
            binom_unformed_2
        )

        for tex, color in [
            ("(a-b)^2", BLUE),
            ("a^2", GRAY_B),
            ("ab", ORANGE),
            ("b^2", GREEN),
        ]:
            binom_unformed_2.set_color_by_tex(tex, color)
            binom_2.set_color_by_tex(tex, color)

        self.wait(1)
        self.play(
            *[
                TransformMatchingShapes(graphic, unformed)
                for graphic, unformed in zip(binom_2_graphic, binom_unformed_2)
            ]
        )
        self.play(TransformMatchingTex(binom_unformed_2, binom_2))

        self.play(Write(SurroundingRectangle(binom_2, color=GRAY_B, buff=0.3)))

        self.wait(3)
        self.clear_mobjects()


class Binom3Scene(FundamentalScene):
    def construct(self):
        a_square = Square(side_length=3, color=RED)
        a_label_down = MathTex("a", color=RED).next_to(a_square, direction=DOWN)
        a_label_left = MathTex("a", color=RED).next_to(a_square, direction=LEFT)
        a_square_label = MathTex("a^2", color=RED).move_to(a_square)
        ab_right = Rectangle(width=1, height=1e-3, color=BLUE).next_to(
            a_square, direction=RIGHT, aligned_edge=DOWN, buff=0
        )
        ba_left = Rectangle(width=1e-3, height=1, color=BLUE).next_to(
            a_square, direction=UP, aligned_edge=LEFT, buff=-1
        )
        b_label_down = MathTex("b", color=BLUE).next_to(ab_right, direction=DOWN)
        b_label_left = MathTex("b", color=BLUE).next_to(ba_left, direction=LEFT)

        b_label_down.shift(
            ab_right.get_bottom() - b_label_down.get_bottom() + 0.5 * DOWN
        )

        title = MarkupText(
            "Die 3. <span color='#bbb'>binomische</span> Formel", font="Helvetica"
        ).to_edge(UP)

        self.play(Write(title))
        self.play(Create(a_square))
        self.play(Write(a_label_left), Write(a_label_down))
        self.play(Write(a_square_label))
        self.play(Create(ab_right))
        self.play(Write(b_label_down))
        self.play(
            ab_right.animate.stretch_to_fit_height(a_square.height).align_to(
                a_square, direction=DOWN
            )
        )
        self.play(Create(ba_left))
        self.play(Write(b_label_left))
        self.play(
            ba_left.animate.stretch_to_fit_width(4).align_to(a_square, direction=LEFT)
        )

        split_rect = (
            VGroup(
                *[
                    Rectangle(height=2, width=w, color=RED, fill_opacity=0.5)
                    for w in [1, 3]
                ]
            )
            .arrange(LEFT, buff=0)
            .align_to(a_square, direction=LEFT)
            .align_to(a_square, direction=DOWN)
        )

        split_copy = (
            split_rect[0].copy().rotate(90 * DEGREES).align_to(a_square, direction=UL)
        )

        a_plus_b_brace = Brace(
            VGroup(a_square, ab_right), direction=DOWN, color=RED, buff=0.5
        )
        a_minus_b_brace = Brace(split_rect, direction=LEFT, color=RED, buff=0.5)
        a_plus_b_label = a_plus_b_brace.get_tex("(a+b)").set_color(RED)
        a_minus_b_label = a_minus_b_brace.get_tex("(a-b)").set_color(RED)
        a_minus_b_brace_up = Brace(split_copy, direction=UP, color=RED)
        a_minus_b_label_up = a_minus_b_brace_up.get_tex("(a-b)").set_color(RED)
        b_square = Square(side_length=1, color=BLUE, fill_opacity=0.5).next_to(
            split_copy, direction=RIGHT, buff=0
        )
        b_brace = Brace(b_square, direction=UP, color=BLUE)
        b_brace_label = b_brace.get_tex("b").set_color(BLUE)
        b_square_label = MathTex("b^2", color=BLUE).move_to(b_square)

        self.play(
            FadeIn(a_plus_b_brace),
            Write(a_plus_b_label),
            FadeIn(a_minus_b_brace),
            Write(a_minus_b_label),
        )
        self.play(FadeIn(split_rect))
        self.play(ReplacementTransform(split_rect[0], split_copy))
        self.play(FadeIn(a_minus_b_brace_up), FadeIn(a_minus_b_label_up))
        self.play(Write(b_brace), Write(b_brace_label))
        self.play(Write(b_square_label), FadeIn(b_square))
        self.play(FadeOut(title))
        self.play(VGroup(*self.mobjects).animate.scale(0.7).to_edge(UP))

        resulting_rect = split_rect.copy()
        resulting_rect[0].rotate(90 * DEGREES)
        resulting_rect.arrange(LEFT, buff=0)
        a = VGroup(a_square, a_square_label)
        b = VGroup(b_square, b_square_label)
        binom_3_graphic = (
            VGroup(
                VGroup(
                    resulting_rect,
                    a_minus_b_label.copy().next_to(resulting_rect, direction=LEFT),
                    a_plus_b_label.copy().next_to(resulting_rect, direction=DOWN),
                ),
                MathTex("="),
                a.copy().set_opacity(0.5),
                MathTex("-"),
                b.copy(),
            )
            .arrange(RIGHT)
            .to_edge(DOWN)
        )

        self.play(
            ReplacementTransform(
                VGroup(split_rect, a_minus_b_label, a_plus_b_label).copy(),
                binom_3_graphic[0],
            )
        )
        self.play(FadeIn(binom_3_graphic[1]))
        self.play(ReplacementTransform(a.copy(), binom_3_graphic[2]))
        self.play(FadeIn(binom_3_graphic[3]))
        self.play(ReplacementTransform(b.copy(), binom_3_graphic[4]))

        binom_3 = MathTex("(a+b)", "(a-b)", "=", "a^2", "-", "b^2").move_to(
            binom_3_graphic
        )
        for tex, color in [("(a+b)", RED), ("(a-b)", RED), ("a^2", RED), ("b^2", BLUE)]:
            binom_3.set_color_by_tex(tex, color)

        self.play(TransformMatchingShapes(binom_3_graphic, binom_3))
        self.play(Write(SurroundingRectangle(binom_3, color=GRAY_B, buff=0.3)))

        self.wait(3)
        self.clear_mobjects()


class SummaryScene(FundamentalScene):
    def map_color(self, number):
        return GRAY_B if number else WHITE

    def shift_list(self, lst):
        return lst[-1:] + lst[:-1]

    def construct(self):
        title = (
            Text("Zusammenfassung:", font="Helvetica")
            .to_edge(UP)
            .set_color_by_gradient(WHITE, GRAY_A, GRAY_A)
        )
        self.play(Write(title))

        color_list = [WHITE, GRAY, GRAY]
        for _ in range(10):
            color_list = self.shift_list(color_list)
            self.play(
                title.animate.set_color_by_gradient(*color_list),
                rate_func=linear,
                lag_ratio=0,
            )
        self.play(Unwrite(title))
        self.wait()


class EndScene(FundamentalScene):
    def construct(self):
        mcreature = MCreature(theme="GRAY")
        self.play(FadeIn(mcreature))
        self.wait()
        self.play(mcreature.blink_eyes())
        self.wait()
        self.play(mcreature.speak("Jetzt versteht\nihr die Herleitung!", size=32))
        self.play(mcreature.blink_eyes())
        self.play(mcreature.unspeak())
        self.wait()
        self.play(mcreature.speak("Danke fürs Zuschauen!", size=32))
        self.play(mcreature.write_text(), run_time=2)
        self.play(mcreature.raise_eyebrows(func=there_and_back_with_pause), run_time=2)
        self.play(mcreature.blink_eyes())

        self.wait(3)
        self.clear_mobjects()


class Thumbnail(FundamentalScene):
    def construct(self):
        title = MarkupText(
            "Die <span color='#bbb'>binomischen</span> Formeln",
            font="Helvetica",
            font_size=64,
        ).to_edge(UP)
        a_square = Square(side_length=2, color=BLUE, fill_opacity=0.5).shift(0.5 * DL)
        a_label_down = MathTex("a", color=BLUE).next_to(a_square, direction=DOWN)
        a_label_left = MathTex("a", color=BLUE).next_to(a_square, direction=LEFT)
        a_square_label = MathTex("a^2", color=BLUE).move_to(a_square.get_center())
        ab_right = Rectangle(
            width=1, height=a_square.height, color=ORANGE, fill_opacity=0.5
        ).next_to(a_square, RIGHT, aligned_edge=DOWN, buff=0)
        ab_up = Rectangle(
            width=a_square.width, height=1, color=ORANGE, fill_opacity=0.5
        ).next_to(a_square, direction=UP, aligned_edge=LEFT, buff=0)

        ab_label_up = MathTex("ab", color=ORANGE).move_to(ab_up)
        ab_label_right = ab_label_up.copy().move_to(ab_right)
        b_label_up = MathTex("b", color=ORANGE).next_to(ab_up, direction=LEFT)
        b_label_right = MathTex("b", color=ORANGE).next_to(
            ab_right, direction=DOWN, buff=0.5
        )
        b_label_right.shift(
            ab_right.get_bottom() - b_label_right.get_bottom() + 0.5 * DOWN
        )
        b_square = Square(side_length=1, color=GREEN, fill_opacity=0.5).next_to(
            ab_up, direction=RIGHT, aligned_edge=DOWN, buff=0
        )

        b_square_label = MathTex("b^2", color=GREEN).move_to(b_square)

        square = VGroup(
            a_square,
            a_square_label,
            a_label_down,
            a_label_left,
            ab_right,
            ab_up,
            ab_label_right,
            ab_label_up,
            b_label_right,
            b_label_up,
            b_square,
            b_square_label,
        ).shift(0.5 * UP)

        binom_1 = MathTex(
            "(",
            "a",  # 1
            "+",
            "b",  # 3
            ")",
            "^2",
            "=",
            "a^2",  # 11
            "+",
            "2ab",  # 15
            "+",
            "b^2",  # 17
            font_size=64,
        ).next_to(square, direction=DOWN)

        for tex, color in [
            ("a", BLUE),
            ("b", ORANGE),
            ("ab", ORANGE),
            ("b^2", GREEN),
            ("a^2", BLUE),
        ]:
            binom_1.set_color_by_tex(tex, color)

        mcreature = MCreature(theme="GRAY").scale(0.8).to_corner(DR)
        mcreature.add_speech("Die Herleitung!", size=32, direction="DL")
        self.add(
            square,
            title,
            binom_1,
            mcreature,
        )
