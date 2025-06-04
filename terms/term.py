from manim import *
import sys
import random
from MF_Tools import *

sys.path.append("/Users/omidsedighi-mornani/Desktop/mathe/PROJECTS")
from Library.m_creature import MCreature
from Library.list_utils import ExtendedMathTex, ExtendedVGroup, ExtendedText
from Library.extended_colors import *

# set random seed
random.seed(69)


class AbstractScene(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        frame = SVGMobject("assets/whiteboard.svg")

        frame.stretch_to_fit_height(config.frame_height)
        frame.stretch_to_fit_width(config.frame_width)
        frame.set_z_index(-99)

        self.add(frame)


class IntroScene(AbstractScene):
    def construct(self):
        title = (
            Text(
                "Grundlagen von Termen",
                font="Patrick Hand",
                color=PENN_BLUE,
                stroke_color=BLACK,
                weight=MEDIUM,
            )
            .scale(1.5)
            .to_edge(UP)
        )

        terms = (
            ExtendedVGroup(
                ExtendedMathTex("3", "+", "5", color=PENN_BLUE),
                ExtendedMathTex("3", "\cdot", "(", "x", "+", "5", ")", color=PENN_BLUE),
                ExtendedMathTex(
                    "3", "\cdot", "x", "-", "5", "\cdot", "x", color=PENN_BLUE
                ),
            )
            .scale(1.3)
            .arrange(DOWN)
            .shift(0.5 * UP)
        )

        terms_simplified = (
            ExtendedVGroup(
                ExtendedMathTex("8", color=PENN_BLUE),
                ExtendedMathTex("3", "\cdot", "x", "+", "15", color=PENN_BLUE),
                ExtendedMathTex("-2", "x", color=PENN_BLUE),
            )
            .scale(1.3)
            .arrange(DOWN)
            .shift(0.5 * UP)
        )

        self.play(Write(title))
        self.wait()
        self.play(Write(terms[0]))
        # Transform each term to the next using a for loop
        for i in range(len(terms) - 1):
            self.play(TransformMatchingTex(terms[i].copy(), terms[i + 1]))
            self.wait()

        self.wait()

        mcreature = MCreature(theme="BLUE").scale(0.8)

        self.play(DrawBorderThenFill(mcreature))
        self.play(mcreature.blink_eyes())
        self.play(mcreature.move_iris(UR))
        self.play(
            mcreature.speak(
                "Buchstaben??", font="Patrick Hand", direction="DR", scale_factor=0.7
            )
        )
        self.play(mcreature.move_iris(DL))

        transform_indices = [[0, 1, 3, 4], [0, 1, 2, 3]]
        self.play(
            ReplacementTransform(terms[0], terms_simplified[0]),
            *[
                ReplacementTransform(terms[1][i], terms_simplified[1][j])
                for i, j in zip(transform_indices[0], transform_indices[1])
            ],
            FadeIn(terms_simplified[1][4:]),
            FadeOut(terms[1][2, 5, 6]),
            TransformMatchingTex(terms[2], terms_simplified[2]),
        )
        surr_rect = SurroundingRectangle(terms_simplified, color=BLUE_E, buff=0.3)
        self.play(Create(surr_rect))

        self.play(
            mcreature.speak(
                "Zusammenfassen??",
                font="Patrick Hand",
                direction="UR",
                scale_factor=0.7,
            ),
            mcreature.speech_bubbles.animate.arrange(UP).next_to(mcreature),
        )
        self.play(mcreature.blink_eyes())
        self.wait(2)

        for _ in range(3):
            self.play(mcreature.blink_eyes())
            random_time = 1 + (2 - 1) * random.random()
            self.wait(random_time)

        self.play(
            Unwrite(VGroup(title, terms_simplified, surr_rect)),
            FadeOut(mcreature),
            *[mcreature.unspeak() for _ in range(2)],
        )

        self.wait(3)


class FirstScene(AbstractScene):
    def construct(self):
        title = Text(
            "Einfaches Beispiel",
            font="Patrick Hand",
            color=PENN_BLUE,
            stroke_color=BLACK,
        ).to_edge(UP)
        natural_term = ExtendedMathTex("2", "\cdot", "3", color=PENN_BLUE).scale(1.5)
        variable_term = ExtendedMathTex(
            "5", "\cdot", "x", "+", "2", color=PENN_BLUE
        ).scale(1.5)
        VGroup(natural_term, variable_term).arrange(UP)
        self.play(Write(title))
        self.wait()
        self.play(Write(natural_term), Write(variable_term))
        self.wait()
        self.play(
            natural_term.animate.arrange(RIGHT, buff=2.5),
            FadeOut(variable_term),
        )
        self.play(
            *[
                natural_term[i].animate.set_color(c)
                for i, c in enumerate([RED_E, GREEN_E, RED_E])
            ],
        )

        braces = VGroup(
            *[
                BraceLabel(natural_term[i], text=text)
                for i, text in enumerate(["1.Operand", "Operation", "2.Operand"])
            ]
        )

        [braces[i].set_color(c) for i, c in enumerate([RED_E, GREEN_E, RED_E])]

        self.play(FadeIn(braces))

        self.play(braces[0].animate.set(brace_text="Test!"))

        natural_term.save_state()
        for operation in ["+", "-", "\div"]:
            self.wait(0.5)
            self.play(
                Transform(natural_term[1], ExtendedMathTex(operation, color=GREEN_E))
            )
        self.wait(1)
        self.play(Restore(natural_term))
        self.wait(1)

        complex_term = ExtendedMathTex(
            "7", "+", "2", "\cdot", "4", color=PENN_BLUE
        ).scale(1.5)

        self.play(
            FadeOut(natural_term, braces),
            Write(complex_term),
            TransformMatchingShapes(
                title,
                Text("Komplexerer Term", font="Patrick Hand", color=PENN_BLUE).to_edge(
                    UP
                ),
            ),
        )
        self.play(complex_term.animate.arrange(RIGHT, buff=1))

        braces = ExtendedVGroup(
            BraceLabel(complex_term, "Summe", buff=1.2).set_color(PENN_BLUE),
            BraceLabel(complex_term[2:], "Produkt").set_color(PENN_BLUE),
        )

        self.play(Indicate(complex_term[3], scale_factor=1.5, color=RED_E))
        self.play(complex_term[2:].animate.set_color(RED_E), FadeIn(braces[1]))
        self.wait()
        self.play(Indicate(complex_term[1], scale_factor=1.5, color=GREEN_E))
        self.play(complex_term[:2].animate.set_color(GREEN_E))
        self.play(FadeIn(braces[0]))

        complex_term2 = (
            ExtendedMathTex("7", "+", "8", color=GREEN_E)
            .scale(1.5)
            .arrange(RIGHT, buff=1)
        )

        self.play(
            ReplacementTransform(complex_term[2:], complex_term2[2]),
            ReplacementTransform(complex_term[:2], complex_term2[:2]),
            FadeOut(braces[1]),
            Transform(
                braces[0], BraceLabel(complex_term2, text="Summe").set_color(PENN_BLUE)
            ),
        )
        self.wait()
        self.play(
            ReplacementTransform(
                complex_term2, ExtendedMathTex("15", color=PENN_BLUE).scale(1.5)
            ),
            FadeOut(braces[0]),
        )
        self.wait(1)
        self.play(FadeOut(complex_term2))

        self.wait(3)


class SecondScene(AbstractScene):
    def construct(self):
        title = Text("Komplexerer Term", font="Patrick Hand", color=PENN_BLUE).to_edge(
            UP
        )

        variable_term = ExtendedMathTex(
            "5", "\cdot", "x", "+", "2", color=PENN_BLUE
        ).scale(1.5)

        self.add(title)

        self.play(
            Transform(
                title,
                Text(
                    "Term mit Variablen", font="Patrick Hand", color=PENN_BLUE
                ).to_edge(UP),
            )
        )
        variable_term.save_state()
        self.play(Write(variable_term))
        self.play(variable_term.animate.arrange(RIGHT, buff=1))

        braces = ExtendedVGroup(
            *[
                BraceLabel(
                    variable_term[i], text, brace_direction=DOWN if i % 2 == 0 else UP
                ).set_color(PENN_BLUE)
                for i, text in enumerate(
                    ["Zahl", "1.Operand", "Variable", "2.Operand", "Zahl"]
                )
            ]
        )

        self.play(FadeIn(braces[[0, 1, 3, 4]]))
        self.wait()
        self.play(
            variable_term[2].animate.set_color(RED_E),
            Wiggle(variable_term[2]),
            Flash(variable_term[2], color=RED_E, flash_radius=0.3),
        )
        self.play(FadeIn(braces[2].set_color(RED_E)))

        for num in [2, 5, 7, "x"]:
            math_tex = (
                ExtendedMathTex(num, color=RED_E).scale(1.5).move_to(variable_term[2])
            )

            self.play(Transform(variable_term[2], math_tex))
            self.wait(0.5)

        self.wait(1)
        self.play(FadeOut(braces), Restore(variable_term))

        self.play(Indicate(variable_term[1], scale_factor=1.5, color=RED_E))

        variable_term_simplified = MathTex("5", "x", "+", "2", color=PENN_BLUE).scale(
            1.5
        )

        self.play(
            FadeOut(variable_term[1]),
            ReplacementTransform(variable_term[0, 2], variable_term_simplified[:2]),
            ReplacementTransform(variable_term[3:], variable_term_simplified[2:]),
        )

        brace = BraceLabel(variable_term_simplified, "Summe").set_color(PENN_BLUE)
        braces = ExtendedVGroup(
            BraceLabel(variable_term_simplified[:2], "x", brace_direction=UP).set_color(
                RED_E
            ),
            BraceLabel(
                variable_term_simplified[3], "Zahl", brace_direction=UP
            ).set_color(GREEN_E),
        )
        self.play(FadeIn(brace))

        self.play(
            variable_term_simplified[:2].animate.set_color(RED_E),
            variable_term_simplified[3].animate.set_color(GREEN_E),
        )

        for br in braces:
            self.play(FadeIn(br))

        mcreature = MCreature(theme="BLUE").to_corner(DL)

        self.play(FadeIn(mcreature))
        self.play(
            mcreature.speak(
                "Kann man nicht \n vereinfachen!", scale_factor=0.6, direction="DR"
            )
        )

        self.play(mcreature.blink_eyes())
        self.play(mcreature.unspeak(duration=2))

        self.play(
            Transform(
                variable_term_simplified[2],
                ExtendedMathTex("-", color=PENN_BLUE)
                .scale(1.5)
                .move_to(variable_term_simplified[2]),
            ),
            Transform(
                brace,
                BraceLabel(variable_term_simplified, "Differenz").set_color(PENN_BLUE),
            ),
        )

        self.play(
            mcreature.speak(
                "Summen und Differenzen kann man\n<b>nur mit gleichen Familien</b> zusammenfassen!",
                direction="DR",
                scale_factor=0.6,
                duration=2,
            ),
        )

        self.wait()
        self.play(mcreature.blink_eyes(), mcreature.unspeak(duration=2))

        self.play(
            Transform(
                variable_term_simplified[2],
                ExtendedMathTex("\cdot", color=PENN_BLUE)
                .scale(1.5)
                .move_to(variable_term_simplified[2]),
            ),
            Transform(
                brace,
                BraceLabel(variable_term_simplified, "Produkt").set_color(PENN_BLUE),
            ),
            mcreature.speak(
                "Anders sieht das bei\n<b>Produkten und Quotienten</b> aus!",
                scale_factor=0.6,
                direction="DR",
                duration=2,
            ),
        )

        variable_term2 = ExtendedMathTex(
            "5", "\cdot", "x", "\cdot", "2", color=PENN_BLUE
        ).scale(1.5)

        variable_term2_simplified = ExtendedMathTex(
            "10", "\cdot", "x", color=PENN_BLUE
        ).scale(1.5)

        variable_term2_finished = ExtendedMathTex("10", "x", color=PENN_BLUE).scale(1.5)

        self.play(
            FadeOut(braces, brace),
            TransformMatchingTex(variable_term_simplified, variable_term2),
        )

        self.wait()
        self.play(
            TransformMatchingTex(
                variable_term2, variable_term2_simplified, transform_mismatches=True
            )
        )
        self.wait()
        self.play(
            TransformMatchingTex(variable_term2_simplified, variable_term2_finished)
        )

        self.play(
            ReplacementTransform(
                title,
                Text(
                    "Jetzt bist du dran!", font="Patrick Hand", color=PENN_BLUE
                ).to_edge(UP),
            ),
            mcreature.unspeak(duration=2),
            Unwrite(variable_term2_finished),
        )

        self.wait(3)


class ThirdScene(AbstractScene):
    def construct(self):
        title = Text(
            "Jetzt bist du dran!",
            font="Patrick Hand",
            color=PENN_BLUE,
            stroke_color=PENN_BLUE,
        ).to_edge(UP)
        mcreature = MCreature(theme="BLUE").to_edge(DL)
        self.add(title, mcreature)
        self.play(
            mcreature.speak(
                "Kannst du diese beiden Terme zusammenfassen?",
                scale_factor=0.6,
                duration=2,
                direction="DR",
            )
        )

        terms = ExtendedVGroup(
            ExtendedMathTex("2", "x", "+", "1", "-", "x", "+", "3"),
            ExtendedMathTex("4", "y", "\cdot", "3", "x", "+", "4", "x", "y"),
        )

        terms_simplified = ExtendedVGroup(
            ExtendedMathTex("x", "+", "1", "+", "3"),
            ExtendedMathTex("12", "x", "y", "+", "4", "x", "y"),
        )

        terms_finished = ExtendedVGroup(
            ExtendedMathTex("x", "+", "4"),
            ExtendedMathTex("16", "x", "y"),
        )

        for t in [terms, terms_simplified, terms_finished]:
            t.scale(1.5).arrange(DOWN, buff=0.5).shift(UP).set_color(PENN_BLUE)

        self.play(Write(terms), run_time=2)
        self.wait()

        self.play(
            mcreature.speak(
                "<b>Tipp:</b> Alle Teilterme mit <b>x</b> und <b>y</b>\nsind auch zwei verschiedene Familien!",
                duration=2,
                scale_factor=0.6,
            ),
            mcreature.speech_bubbles.animate.arrange(
                UP, buff=0.1, aligned_edge=LEFT
            ).next_to(mcreature),
        )

        D_BLUE = "#5D6B75"
        pause = SVGMobject("assets/pause.svg", fill_opacity=0.6).scale(2)
        pause[0].set_fill(D_BLUE)

        self.play(FadeIn(pause))
        self.wait(5)

        self.play(FadeOut(pause))

        self.play(
            mcreature.unspeak(),
            mcreature.unspeak(),
            FadeOut(mcreature, terms[1]),
            terms[0].animate.move_to(ORIGIN),
        )

        coloring = [([0, 1, 4, 5], RED_E), ([2, 3, 6, 7], GREEN_E)]

        self.play(*[terms[0][idx].animate.set_color(clr) for idx, clr in coloring])

        braces_indices = [
            ([0, 1], "x"),
            ([2, 3], "Zahl"),
            ([4, 5], "x"),
            ([6, 7], "Zahl"),
        ]
        braces = ExtendedVGroup(
            *[
                BraceLabel(terms[0][idx], txt).set_color(
                    RED_E if txt == "x" else GREEN_E
                )
                for idx, txt in braces_indices
            ]
        )

        self.play(FadeIn(braces))
        self.play(Indicate(terms[0][0, 1, 4, 5], color=RED))
        self.play(FadeOut(braces))

        for t in terms_simplified, terms_finished:
            t[0].move_to(terms[0]).set_color(GREEN_E)
            t[0][0].set_color(RED_E)

        self.play(TransformMatchingTex(terms[0], terms_simplified[0]))
        brace = BraceLabel(terms_simplified[0][1:], "Zahl").set_color(GREEN_E)

        self.play(FadeIn(brace), Indicate(terms_simplified[0][1:], color=GREEN))
        self.wait()
        self.play(
            TransformMatchingTex(terms_simplified[0], terms_finished[0]), FadeOut(brace)
        )

        surr_Rect = SurroundingRectangle(
            terms_finished[0], color=GREY_A, fill_opacity=0.1
        )

        self.play(DrawBorderThenFill(surr_Rect))

        self.wait()
        self.play(Unwrite(terms_finished[0]), Uncreate(surr_Rect))

        for t in terms[1], terms_simplified[1], terms_finished[1]:
            t.move_to(ORIGIN)

        self.play(Write(terms[1]))

        coloring = [([0, 1, 8], RED_E), ([3, 4, 7], "GREEN_E")]

        self.play(*[terms[1][idx].animate.set_color(clr) for idx, clr in coloring])

        braces_indices = [([0, 1], "y"), ([3, 4], "x"), ([7, 8], "xy")]
        braces = ExtendedVGroup(
            *[
                BraceLabel(
                    terms[1][idx], txt, buff=0.2 if txt == "x" else 0.1
                ).set_color(
                    RED_E if txt == "y" else GREEN_E if txt == "x" else PENN_BLUE
                )
                for idx, txt in braces_indices
            ]
        )

        mcreature = MCreature(theme="BLUE").to_corner(DL)

        self.play(FadeIn(braces))
        self.wait()
        self.play(FadeIn(mcreature))
        self.wait(0.5)
        self.play(
            mcreature.speak(
                "<b>Erinnerung:</b> Mit dem &#183; Zeichen\nkann man Familien verschmelzen!",
                direction="DR",
                scale_factor=0.6,
                duration=2,
            ),
            mcreature.blink_eyes(),
        )

        self.play(
            Indicate(terms[1][0, 1], color=RED), Indicate(terms[1][3, 4], color=GREEN)
        )

        brace = braces[2].copy().next_to(terms_simplified[1][:4], direction=DOWN)

        for t in terms_simplified[1], terms_finished[1]:
            t.set_color_by_tex("x", GREEN_E)
            t.set_color_by_tex("y", RED_E)

        self.play(
            FadeOut(braces[0, 1]),
            braces[2].animate.next_to(terms_simplified[1][5:], direction=DOWN),
            ReplacementTransform(braces[2].copy(), brace),
            ReplacementTransform(terms[1][0, 3], terms_simplified[1][0]),
            ReplacementTransform(terms[1][4, 1], terms_simplified[1][1, 2]),
            ReplacementTransform(terms[1][5:], terms_simplified[1][3:]),
            FadeOut(terms[1][2]),
        )
        self.play(mcreature.unspeak())
        self.play(mcreature.blink_eyes())
        self.play(
            mcreature.speak(
                "<b>xy</b> ist wieder eine Familie!",
                scale_factor=0.6,
                duration=2,
                direction="DR",
            ),
        )

        self.wait()
        self.play(
            TransformMatchingTex(
                terms_simplified[1], terms_finished[1], transform_mismatches=True
            ),
            FadeOut(braces[2], brace),
        )

        surr_Rect = SurroundingRectangle(
            terms_finished[1], color=GREY_A, fill_opacity=0.1
        )

        self.play(DrawBorderThenFill(surr_Rect))

        self.play(mcreature.blink_eyes())

        self.play(
            Uncreate(surr_Rect),
            Unwrite(terms_finished[1]),
            Unwrite(title),
            mcreature.unspeak(),
            FadeOut(mcreature),
        )

        self.wait(3)


class FourthScene(AbstractScene):
    def construct(self):
        title = Text(
            "Term aufstellen",
            font="Patrick Hand",
            color=PENN_BLUE,
            stroke_color=PENN_BLUE,
        ).to_edge(UP)
        mcreature = MCreature(theme="BLUE").to_corner(DL)

        speech_texts = [
            "Ein Kino verlangt 8€ Eintritt pro Kind\nund 12€ pro Erwachsenen.",
            "Stelle einen Term für die Gesamtkosten für\n<b>k</b> Kinder und <b>e</b> Erwachsene auf!",
        ]

        task_formulation = (
            MarkupText(
                "\n".join(speech_texts).replace("\n", " ", 1),
                color=DARK_BLUE,
                stroke_color=DARK_BLUE,
                font="Chalkboard",
            )
            .scale(0.6)
            .next_to(title, direction=DOWN)
        )

        term_basic = (
            ExtendedMathTex(
                "8",
                "\cdot",
                "4",
                "+",
                "12",
                "\cdot",
                "2",
                "=",
                "50",
                color=PENN_BLUE,
            )
            .scale(1.5)
            .arrange(RIGHT, buff=0.5)
        )

        term_variable = ExtendedMathTex(
            "8", "k", "+", "12", "e", color=PENN_BLUE
        ).scale(1.5)

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(mcreature))
        self.play(mcreature.speak(speech_texts[0], scale_factor=0.6, duration=3))
        self.play(
            mcreature.speak(
                speech_texts[1], scale_factor=0.6, direction="DR", duration=3
            )
        )

        self.play(
            *[
                TransformMatchingShapes(bubble.textBox.copy(), task_formulation)
                for bubble in mcreature.speech_bubbles
            ],
            mcreature.unspeak(),
            mcreature.unspeak(),
        )

        self.play(mcreature.blink_eyes())

        self.play(
            mcreature.speak(
                "Beispiel für\n<b>4 Kinder</b> und <b>2 Erwachsene</b>!",
                direction="DR",
                scale_factor=0.6,
                duration=2,
            )
        )

        self.play(mcreature.blink_eyes())

        self.play(Write(term_basic[:3]))

        label_constructor = lambda text, **kwargs: Text(
            text, font="Patrick Hand", **kwargs
        )

        label_texts = [
            "Preis pro Kind",
            "Anzahl Kinder",
            "Preis pro Erwachsener",
            "Anzahl Erwachsene",
        ]

        braces = ExtendedVGroup(
            *[
                BraceLabel(
                    term_basic[2 * i],
                    label_text,
                    brace_direction=DOWN if i % 2 == 0 else UP,
                    label_constructor=label_constructor,
                    font_size=24,
                )
                for i, label_text in enumerate(label_texts)
            ]
        ).set_color(PENN_BLUE)

        self.play(FadeIn(braces[0, 1]))
        self.play(mcreature.blink_eyes())
        self.play(FadeIn(term_basic[3]))
        self.play(Write(term_basic[4:7]))
        self.play(FadeIn(braces[2, 3]))
        self.play(mcreature.blink_eyes())
        self.play(
            FadeIn(term_basic[7]), FadeTransform(term_basic[:7].copy(), term_basic[8])
        )
        self.play(mcreature.unspeak())
        self.play(mcreature.blink_eyes())
        self.wait(0.5)
        self.play(
            mcreature.speak(
                "Es sind insgesamt 50 Euro!", scale_factor=0.6, direction="DR"
            )
        )
        self.play(mcreature.blink_eyes())

        self.wait()

        self.play(mcreature.unspeak())
        self.play(mcreature.blink_eyes())
        self.play(
            mcreature.speak(
                "Jetzt stellen wir den Term\nfür allgemein <b>e</b> Erwachsene und <b>k</b> Kinder auf!",
                scale_factor=0.6,
                direction="DR",
            )
        )
        self.play(FadeOut(term_basic[7:]))
        self.play(Indicate(term_basic[2, 6], color=BLUE))
        self.play(mcreature.blink_eyes())

        tuple_k_e = [(2, 3), (1, 1), (5, 4), ("k", "e")]

        for k, e in tuple_k_e:
            self.play(
                Transform(
                    term_basic[2],
                    ExtendedMathTex(k, color=PENN_BLUE)
                    .scale(1.5)
                    .move_to(term_basic[2]),
                ),
                Transform(
                    term_basic[6],
                    ExtendedMathTex(e, color=PENN_BLUE)
                    .scale(1.5)
                    .move_to(term_basic[6]),
                ),
            )
            self.wait()

        self.play(mcreature.blink_eyes())
        self.play(
            ReplacementTransform(term_basic[0, 2], term_variable[0, 1]),
            ReplacementTransform(term_basic[3], term_variable[2]),
            ReplacementTransform(term_basic[4, 6], term_variable[3, 4]),
            FadeOut(term_basic[1, 5]),
            FadeOut(braces),
        )

        surr_Rect = SurroundingRectangle(term_variable, color=GRAY_D, fill_opacity=0.2)

        self.play(DrawBorderThenFill(surr_Rect))
        self.play(mcreature.blink_eyes())
        self.play(
            Unwrite(task_formulation),
            Unwrite(title),
            Unwrite(term_variable),
            FadeOut(mcreature),
            mcreature.unspeak(),
            Uncreate(surr_Rect),
        )

        self.wait(3)


class EndScene(AbstractScene):
    def construct(self):
        mcreature = MCreature(theme="BLUE")
        self.play(FadeIn(mcreature))

        self.play(
            mcreature.speak(
                "Jetzt weißt du was Terme sind!",
                scale_factor=0.6,
                direction="DR",
                duration=2,
            )
        )
        self.play(mcreature.blink_eyes())
        self.play(
            mcreature.speak("Und wie man sie aufstellt!", scale_factor=0.6, duration=2)
        )
        self.play(mcreature.blink_eyes())
        self.wait()
        self.play(mcreature.unspeak(), mcreature.unspeak())
        self.play(mcreature.blink_eyes())
        self.play(
            mcreature.speak("Bis zum nächsten Mal! ;)", scale_factor=0.6, duration=2)
        )
        self.wait()
        self.play(mcreature.write_text(duration=2))

        self.play(FadeOut(mcreature, mcreature.speech_bubbles, mcreature.text))
        self.play(FadeOut(*self.mobjects))
        self.wait(3)


class Thumbnail(AbstractScene):
    def construct(self):
        pass
