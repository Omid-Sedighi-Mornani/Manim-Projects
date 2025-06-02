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
        self.camera.background_color = RED
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

        self.wait()

        self.wait(3)


class Thumbnail(AbstractScene):
    def construct(self):
        pass
