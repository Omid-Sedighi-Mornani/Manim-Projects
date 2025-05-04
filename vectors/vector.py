import sys

sys.path.append("/Users/omidsedighi-mornani/Desktop/mathe/PROJECTS")
from Library.m_creature import MCreature

from manim import *
from reactive_manim import *

# config.quality = "low_quality"


class AbstractScene(Scene):

    def get_vector(self, x: float | str, y: float | str):
        return [r"\begin{pmatrix}", r"1", r"//", r"2" r"\end{pmatrix}"]

    def get_rectangle(
        self, mobject: Mobject, color: ManimColor = YELLOW, opacity: float = 0.6
    ) -> Mobject:
        return VGroup(
            SurroundingRectangle(mobject, color=color),
            BackgroundRectangle(
                mobject, color=color, fill_opacity=opacity, buff=SMALL_BUFF
            ),
        )

    def create_components(self, x: float, y: float, color: ManimColor = YELLOW) -> None:
        vector_x_component = Vector([x, 0, 0], tip_length=0.3, color=WHITE)
        vector_y_component = Vector([0, y, 0], tip_length=0.3, color=WHITE)

        vector_x_component_group = VGroup(
            vector_x_component,
            MathTex(
                x,
            ).next_to(vector_x_component, DOWN),
        )
        vector_y_component_group = VGroup(
            vector_y_component, MathTex(y).next_to(vector_y_component, LEFT)
        )

        self.play(Write(vector_x_component_group))
        self.play(Write(vector_y_component_group))

        self.play(
            vector_x_component_group.animate.set_color(color=color),
            vector_y_component_group.animate.set_color(color=color),
        )
        self.wait(1)
        self.play(Unwrite(vector_x_component_group), Unwrite(vector_y_component_group))


class IntroScene(AbstractScene):
    def construct(self):
        # adding vector
        vector1_text = MathTex(
            r"\vec{v_1}=", r"\begin{pmatrix} 1 \\ 1 \end{pmatrix}", z_index=1
        )
        self.play(Write(vector1_text))
        self.wait()

        # adding asking MCreature animation
        mcreature = MCreature().shift(0.1 * UP)
        self.play(DrawBorderThenFill(mcreature))
        self.play(mcreature.move_iris(direction=UR))
        self.play(mcreature.raise_eyebrows())
        self.play(mcreature.speak("Was ist das??", direction="DR"))
        self.wait()
        self.play(mcreature.lower_eyebrows())
        self.play(mcreature.move_iris(DOWN))
        self.wait()
        self.play(mcreature.blink_eyes())
        self.wait(2.5)
        self.play(mcreature.blink_eyes())
        self.wait(3)
        self.play(mcreature.blink_eyes())
        self.wait()
        self.play(mcreature.move_iris(UP))

        self.play(mcreature.unspeak(), FadeOut(mcreature))

        # showing NumberPlane and moving vector

        self.play(vector1_text.animate.scale(1.3).to_corner(UL))
        surrRect_1 = VGroup(
            SurroundingRectangle(vector1_text, color=BLUE),
            BackgroundRectangle(
                vector1_text, color=BLUE_E, fill_opacity=0.99, buff=0.1
            ),
        )
        self.play(
            DrawBorderThenFill(surrRect_1),
        )
        plane = NumberPlane(
            x_range=(-7, 7, 1),
            y_range=(-4, 4, 1),
            axis_config={
                "include_numbers": True,
                "font_size": 35,
                "include_ticks": True,
                "include_tip": True,
                "stroke_color": "WHITE",
            },
        )

        self.play(Write(plane))
        self.wait(2)

        vector1 = Vector([1, 1, 0], color=BLUE)

        self.play(Write(vector1))
        self.create_components(1, 1)
        self.wait(1)

        self.play(vector1.animate.shift(UR))
        self.play(vector1.animate.shift(UP))
        self.play(vector1.animate.shift(LEFT))
        self.play(vector1.animate.shift(2 * DOWN))

        self.wait(1)
        vector2 = Vector([2, 1, 0], color=ORANGE)

        vector2_text = MathTex(
            r"\vec{v_2}=", r"\begin{pmatrix} 2 \\ 1 \end{pmatrix}", z_index=1
        ).scale(1.3)

        vector2_text.next_to(surrRect_1, direction=DOWN)

        surrRect_2 = VGroup(
            SurroundingRectangle(vector2_text, color=ORANGE),
            BackgroundRectangle(vector2_text, color=ORANGE, buff=0.1),
        )

        self.play(
            ReplacementTransform(vector1_text.copy(), vector2_text),
            FadeIn(surrRect_2),
            ReplacementTransform(vector1.copy(), vector2),
        )
        self.wait(1)
        self.create_components(2, 1)
        self.play(vector2.animate.shift([1, 1, 0]))
        self.wait(1)

        vector3 = Vector([3, 2, 0], color=YELLOW)
        self.play(Write(vector3))

        self.wait(2)

        vector3_text = MathTex(
            r"\vec{v_3}=",
            r"\begin{pmatrix} 1 \\ 1 \end{pmatrix}",
            r"+",
            r"\begin{pmatrix} 2 \\ 1 \end{pmatrix}",
            r"=",
            r"\begin{pmatrix} 3 \\ 2 \end{pmatrix}",
            z_index=1,
        ).scale(1.3)

        vector3_text.to_corner(DL)

        self.play(
            ReplacementTransform(vector1_text[1].copy(), vector3_text[1]),
            ReplacementTransform(vector2_text[1].copy(), vector3_text[3]),
        )

        surrRect_3 = VGroup(
            SurroundingRectangle(vector3_text, color=YELLOW),
            BackgroundRectangle(
                vector3_text, color=YELLOW_E, fill_opacity=0.7, buff=0.1
            ),
        )

        self.wait(0.5)
        self.play(
            Write(vector3_text[0]),
            Write(vector3_text[2]),
            Write(vector3_text[4]),
            Write(vector3_text[5]),
            DrawBorderThenFill(surrRect_3),
        )

        self.wait(1)

        self.play(
            FadeOut(vector1),
            FadeOut(vector2),
            FadeOut(vector1_text),
            FadeOut(vector2_text),
            FadeOut(surrRect_1),
            FadeOut(surrRect_2),
            VGroup(surrRect_3, vector3_text).animate.to_corner(UL),
        )

        vector3_text_transformed = (
            MathTex(
                r"\vec{v_3}=",
                r"\begin{pmatrix} 3 \\ 2 \end{pmatrix}",
                z_index=1,
            )
            .scale(1.3)
            .to_corner(UL)
        )

        surrRect_3_transformed = VGroup(
            SurroundingRectangle(vector3_text_transformed, color=YELLOW),
            BackgroundRectangle(
                vector3_text_transformed, color=YELLOW_E, fill_opacity=0.7, buff=0.1
            ),
        )

        self.play(Wiggle(vector3_text[1]))
        self.play(Wiggle(vector3_text[3]))
        self.play(Wiggle(vector3_text[5]))

        self.play(
            TransformMatchingTex(vector3_text, vector3_text_transformed),
            ReplacementTransform(surrRect_3, surrRect_3_transformed),
        )

        self.wait(1)
        self.create_components(3, 2, color=ORANGE)

        self.play(
            Unwrite(vector3),
            FadeOut(VGroup(surrRect_3_transformed, vector3_text_transformed)),
        )

        #####
        self.wait(5)


class AdditionScene(AbstractScene):
    def construct(self):
        plane = NumberPlane(
            x_range=(-7, 7, 1),
            y_range=(-4, 4, 1),
            axis_config={
                "include_numbers": True,
                "font_size": 35,
                "include_ticks": True,
                "include_tip": True,
                "stroke_color": "WHITE",
            },
        )
        self.add(plane)

        vector1 = Vector([2, 1], color=BLUE)
        vector1_text = (
            MathTex(
                r"\vec{v_1}=",
                MathMatrix([[2], [1]]),
                z_index=1,
            )
            .scale(1.3)
            .to_corner(UL, buff=1)
        )

        surrRect_1 = self.get_rectangle(vector1_text, color=BLUE)

        self.play(Write(vector1_text), DrawBorderThenFill(surrRect_1))
        self.play(Write(vector1))

        self.create_components(2, 1, color=ORANGE)

        vector1_text[1] = MathTex("2*", vector1_text[1])

        self.play(
            Transform(surrRect_1, self.get_rectangle(vector1_text, color=ORANGE)),
            TransformInStages.progress(vector1_text),
        )

        vector1_text[1] = MathMatrix([["2*2"], ["2*1"]])

        self.play(
            TransformInStages.progress(vector1_text),
            Transform(vector1, Vector([4, 2], color=ORANGE)),
        )

        vector1_text[1] = MathMatrix([[4], [2]])

        self.play(TransformInStages.progress(vector1_text))
        self.play(
            Transform(surrRect_1, self.get_rectangle(vector1_text, color=ORANGE)),
        )

        self.create_components(4, 2, color=YELLOW)

        vector1_text[1] = MathMatrix([[2], [1]])
        self.play(
            Transform(surrRect_1, self.get_rectangle(vector1_text, color=BLUE)),
            TransformInStages.progress(vector1_text),
            Transform(vector1, Vector([2, 1], color=BLUE)),
        )

        vector1_text[1] = MathTex("-1*", vector1_text[1])

        self.play(
            Transform(surrRect_1, self.get_rectangle(vector1_text, color=RED)),
            TransformInStages.progress(vector1_text),
            Transform(vector1, Vector([-2, -1], color=RED)),
        )

        self.wait(1)
        vector1_text[1] = MathMatrix([[-2], [-1]])

        self.play(
            Transform(surrRect_1, self.get_rectangle(vector1_text, color=RED)),
            TransformInStages.progress(vector1_text),
        )

        self.wait(2)

        factors = [1.5, -2, 3, 1]
        vector1_text[1] = MathTex(f"{factors[0]}*", MathMatrix([[2], [1]]))
        for factor in factors:
            vector1_text[1][0] = f"{factor}*"
            self.play(
                Transform(surrRect_1, self.get_rectangle(vector1_text, color=BLUE)),
                TransformInStages.progress(vector1_text),
                Transform(vector1, Vector([factor * 2, factor * 1], color=BLUE)),
            )

        vector1_text[1] = MathMatrix([[2], [1]])
        self.play(TransformInStages.progress(vector1_text))

        components = [
            [1, 2],
            [2, -2],
            [0, -3],
            [-8, 4],
        ]
        vector = vector1
        new_component = [2, 1]
        for moving_component in components:
            x, y = moving_component
            new_component = [new_component[0] + x, new_component[1] + y]
            vector1_text[1] = MathTex(vector1_text[1], "+", MathMatrix([[x], [y]]))
            vector1_text.move_to(3 * DOWN)
            vector_added = Vector(moving_component, color=ORANGE).shift(
                vector.get_end()
            )
            self.play(
                Transform(
                    surrRect_1,
                    self.get_rectangle(vector1_text, color=GREEN, opacity=0.9),
                ),
                TransformInStages.progress(vector1_text),
                Write(vector_added),
            )

            new_vector = Vector(new_component, color=GREEN)
            self.play(Write(new_vector))
            self.play(FadeOut(vector), FadeOut(vector_added))
            vector = new_vector

            x_new, y_new = new_component
            vector1_text[1] = MathMatrix([[x_new], [y_new]])

            self.play(TransformInStages.progress(vector1_text))

        self.play(
            Transform(
                surrRect_1, self.get_rectangle(vector1_text, color=GREEN, opacity=0.9)
            )
        )

        ####
        self.wait(5)


class SummaryScene(Scene):
    def construct(self):
        title = Text("Zusammenfassung:").to_edge(UP)
        self.play(Write(title))


class EndScene(Scene):
    def construct(self):
        mcreature = MCreature()
        self.play(FadeIn(mcreature))
        self.wait()
        self.play(mcreature.move_iris(RIGHT))
        self.wait()
        self.play(mcreature.write_text())
        self.play(mcreature.move_iris(LEFT))
        self.wait()
        self.play(mcreature.speak("Bis zum nächsten Mal! ;)"))
        self.play(mcreature.blink_eyes())
        self.wait()
        self.play(mcreature.blink_eyes())
        self.wait()
        self.play(mcreature.blink_eyes())
        self.wait()


import numpy as np


class Thumbnail(Scene):

    def construct(self):

        plane = NumberPlane()
        vectors = VGroup(
            *[
                Vector([i, j], stroke_width=3, tip_length=0.25).set_color(
                    "#69fff1" if j > 0 else "#63d471" if j < 0 else GREEN_B
                )
                for i in np.arange(-7, 8, 1)
                for j in np.arange(-4, 5, 1)
            ]
        )
        self.add(plane)
        self.add(vectors)


if __name__ == "__main__":
    scene = IntroScene()
    scene.render()
