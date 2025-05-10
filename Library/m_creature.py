from manim import *
import sys

sys.path.append("/Users/omidsedighi-mornani/Desktop/mathe/PROJECTS/Library")
from speech_bubble import *
from extended_colors import *


class Test(Scene):
    def construct(self):
        mcreature = MCreature(theme="GRAY")
        self.play(FadeIn(mcreature))
        self.play(mcreature.write_text(text="athe ist leicht", duration=2))
        # self.play(mcreature.speak("Hello!",direction="UL"))
        # self.play(mcreature.speak("Test!",direction="DL"))
        # self.play(mcreature.speak("Test2!",direction="DR"))
        self.play(mcreature.speak("Test3!", direction="UR"))
        self.play(mcreature.move_iris(UP))
        # self.play(mcreature.roll_eyes())
        self.wait()
        self.play(mcreature.move_iris(DOWN))
        self.wait(1)


class MCreature(VMobject):

    THEMES = {
        "DEFAULT": {
            "fillcolor_eyes": WHITE,
            "color_eyes": BLACK,
            "fillcolor_iris": BLACK,
            "color_iris": BLACK,
            "fillcolor_eyebrows": BLUE,
            "color_eyebrows": BLUE,
            "color_mshape": WHITE,
            "color_text": WHITE,
            "color_speechbubble": WHITE,
            "color_speechtext": WHITE,
        },
        "PINK": {
            "fillcolor_eyes": LIGHT_PINK,
            "color_eyes": PINK,
            "fillcolor_iris": BLACK,
            "color_iris": BLACK,
            "fillcolor_eyebrows": PURPLE_E,
            "color_eyebrows": PURPLE_E,
            "color_mshape": PURPLE_A,
            "color_text": PURPLE_A,
            "color_speechbubble": PINK,
            "color_speechtext": PURPLE_A,
        },
        "GRAY": {
            "fillcolor_eyes": WHITE,
            "color_eyes": GRAY_E,
            "fillcolor_iris": GRAY,
            "color_iris": GRAY_D,
            "fillcolor_eyebrows": GRAY,
            "color_eyebrows": GRAY,
            "color_mshape": GRAY_A,
            "color_text": GRAY_A,
            "color_speechbubble": WHITE,
            "color_speechtext": WHITE,
        },
        "BROWN": {
            "fillcolor_eyes": CREAM,
            "color_eyes": BROWN,
            "fillcolor_iris": BROWN,
            "color_iris": BROWN,
            "fillcolor_eyebrows": BROWN,
            "color_eyebrows": BROWN,
            "color_mshape": DARK_BROWN,
            "color_text": DARK_BROWN,
            "color_speechbubble": BROWN,
            "color_speechtext": BROWN,
        },
    }

    def __init__(self, theme="DEFAULT", **kwargs):

        self.theme = theme

        super().__init__(**kwargs)

        self.m_shape = Tex(
            "M", color=MCreature.THEMES[theme]["color_mshape"], stroke_width=0
        ).scale(6)

        # Draw eyes
        self.left_eye = Circle(
            radius=0.3,
            color=MCreature.THEMES[theme]["color_eyes"],
            fill_color=MCreature.THEMES[theme]["fillcolor_eyes"],
            fill_opacity=1,
        ).shift(LEFT * 0.8 + UP * 0.5)
        self.right_eye = Circle(
            radius=0.3,
            color=MCreature.THEMES[theme]["color_eyes"],
            fill_color=MCreature.THEMES[theme]["fillcolor_eyes"],
            fill_opacity=1,
        ).shift(RIGHT * 0.8 + UP * 0.5)

        # Draw iris
        self.left_iris = Circle(
            radius=0.1,
            color=MCreature.THEMES[theme]["color_iris"],
            fill_color=MCreature.THEMES[theme]["fillcolor_iris"],
            fill_opacity=1,
        ).shift(LEFT * 0.8 + UP * 0.5)
        self.right_iris = Circle(
            radius=0.1,
            color=MCreature.THEMES[theme]["color_iris"],
            fill_color=MCreature.THEMES[theme]["fillcolor_iris"],
            fill_opacity=1,
        ).shift(RIGHT * 0.8 + UP * 0.5)

        # Draw reflection
        self.reflection_left = (
            Circle(radius=0.05, color=WHITE, fill_color=WHITE, fill_opacity=1)
            .move_to(self.left_iris.get_left())
            .shift(0.02 * UP)
        )
        self.reflection_right = (
            Circle(radius=0.05, color=WHITE, fill_color=WHITE, fill_opacity=1)
            .move_to(self.right_iris.get_left())
            .shift(0.02 * UP)
        )

        self.left_pupil = VGroup(self.left_iris, self.reflection_left)
        self.right_pupil = VGroup(self.right_iris, self.reflection_right)

        # Draw eyebrows
        self.left_eyebrow = (
            Arc(
                radius=0.3,
                angle=PI,
                color=MCreature.THEMES[theme]["color_eyebrows"],
                fill_color=MCreature.THEMES[theme]["fillcolor_eyebrows"],
                fill_opacity=1,
            )
            .move_to(self.left_eye)
            .shift(UP * 0.3)
        )
        self.right_eyebrow = (
            Arc(
                radius=0.3,
                angle=PI,
                color=MCreature.THEMES[theme]["color_eyebrows"],
                fill_color=MCreature.THEMES[theme]["fillcolor_eyebrows"],
                fill_opacity=1,
            )
            .move_to(self.right_eye)
            .shift(UP * 0.3)
        )

        self.creatureM = VGroup(
            self.m_shape,
            self.left_eye,
            self.right_eye,
            self.left_pupil,
            self.right_pupil,
            self.left_eyebrow,
            self.right_eyebrow,
        )
        self.creatureM.move_to(2.5 * DL + 1.5 * LEFT)
        # self.text = Tex("athe für Dullies",color=MCreature.THEMES[theme]['color_text']).scale(2).next_to(self.m_shape,RIGHT,aligned_edge=DOWN)
        # self.speech_bubble = SVGMobject("speech_bubble", fill_color=MCreature.THEMES[theme]['color_speechbubble'],fill_opacity=0.8).scale(2).next_to(self.creatureM, RIGHT).shift(2*UP).stretch_to_fit_height(6).stretch_to_fit_height(4)
        # self.speech_text = Text("Danke fürs \nZuschauen!",color=MCreature.THEMES[theme]['color_speechtext'],font="Chalkboard").move_to(self.speech_bubble).shift(0.1*UR)
        self.m_shape.set(z_index=0)

        self.left_eye.set(z_index=1)
        self.right_eye.set(z_index=1)

        self.left_iris.set(z_index=2)
        self.right_iris.set(z_index=2)

        self.reflection_left.set(z_index=3)
        self.reflection_right.set(z_index=3)

        self.left_eyebrow.set(z_index=4)
        self.right_eyebrow.set(z_index=4)

        self.speech_bubbles = []

        self.add(self.creatureM)

    # smooth_there_and_back = lambda t: -2*t*(t-1) if t > 0 and t < 1 else 0

    # CREATED BY MYSELF!

    # def smooth_there_and_back(self,t: float) -> float:
    # return -2*t*(t-1) #if t > 0 and t < 1 else 0

    def raise_eyebrows(self, duration=0.5, func=smooth) -> Animation:
        return AnimationGroup(
            self.left_eyebrow.animate(rate_func=func, run_time=duration).shift(
                UP * 0.1
            ),
            self.right_eyebrow.animate(rate_func=func, run_time=duration).shift(
                UP * 0.1
            ),
        )

    def lower_eyebrows(self, duration=0.5, func=smooth) -> Animation:
        return AnimationGroup(
            self.left_eyebrow.animate(rate_func=func, run_time=duration).shift(
                DOWN * 0.1
            ),
            self.right_eyebrow.animate(rate_func=func, run_time=duration).shift(
                DOWN * 0.1
            ),
        )

    def waiting(self, duration=1):
        return AnimationGroup(run_time=duration)

    def blink_eyes(self, duration=0.5, func=there_and_back) -> Animation:
        return AnimationGroup(
            self.left_eye.animate(
                rate_func=func, run_time=2 * duration
            ).stretch_to_fit_height(0.1 * self.left_eye.get_height()),
            self.right_eye.animate(
                rate_func=func, run_time=2 * duration
            ).stretch_to_fit_height(0.1 * self.right_eye.get_height()),
            self.left_pupil.animate(
                rate_func=func, run_time=2 * duration
            ).stretch_to_fit_height(0.1 * self.left_iris.get_height()),
            self.right_pupil.animate(
                rate_func=func, run_time=2 * duration
            ).stretch_to_fit_height(0.1 * self.right_iris.get_height()),
        )

    def move_iris(self, direction, duration=1, func=smooth) -> Animation:
        return AnimationGroup(
            self.left_pupil.animate(rate_func=func, run_time=duration).shift(
                direction * 0.1
            ),
            self.right_pupil.animate(rate_func=func, run_time=duration).shift(
                direction * 0.1
            ),
        )

    def write_text(self, text="athe für Dullies", duration=1, func=smooth) -> Animation:

        self.text = (
            Tex(text, color=MCreature.THEMES[self.theme]["color_text"])
            .scale(2)
            .next_to(self.m_shape, RIGHT, aligned_edge=DOWN)
        )
        self.text.next_to(self.m_shape, RIGHT, aligned_edge=DOWN)
        return AnimationGroup(Write(self.text, rate_func=func, run_time=duration))

    def unwrite_text(self, duration=1):
        try:
            return AnimationGroup(Unwrite(self.text, run_time=duration))

        except:
            raise Exception("MCreature does not have a text to unwrite!")

    def speak(
        self,
        text="",
        duration=1,
        func=smooth,
        size=DEFAULT_FONT_SIZE,
        font="Chalkboard",
        direction="UR",
    ) -> Animation:

        bubbleSide = RIGHT
        shiftingFactor = 2 * UP
        lineAlignment = "DL"

        match direction:
            case "DL":
                shiftingFactor = 0.5 * DOWN
                lineAlignment = "UR"
                bubbleSide = LEFT

            case "UL":
                bubbleSide = LEFT
                lineAlignment = "DR"

            case "DR":
                shiftingFactor = 0.5 * DOWN
                lineAlignment = "UL"

        speech_bubble = (
            SpeechBubble(text, font_size=size, text_font=font, alignment=lineAlignment)
            .next_to(self.creatureM, bubbleSide)
            .shift(shiftingFactor)
            .set(color=MCreature.THEMES[self.theme]["color_speechbubble"])
        )
        self.speech_bubbles.append(speech_bubble)

        return AnimationGroup(speech_bubble.speak(duration))

    def roll_eyes(self):
        moving_circle_right = self.right_eye.copy().scale(0.35)
        moving_circle_left = self.left_eye.copy().scale(0.35)

        angle = ValueTracker(PI / 2)

        right_eye = always_redraw(
            lambda: self.right_pupil.move_to(
                moving_circle_right.point_at_angle(angle.get_value())
            )
        )
        left_eye = always_redraw(
            lambda: self.left_pupil.move_to(
                moving_circle_left.point_at_angle(angle.get_value())
            )
        )
        return AnimationGroup(
            angle.animate.set_value(2 * PI + PI / 2), run_time=3, rate_func=linear
        )

    def unspeak(self, duration=1, element=-1) -> Animation:
        try:
            return AnimationGroup(self.speech_bubbles.pop(element).unspeak())
        except:
            raise Exception("MCreature does not have any speech bubbles to unspeak!")

    def add_speech(
        self,
        text="",
        duration=1,
        func=smooth,
        size=DEFAULT_FONT_SIZE,
        font="Chalkboard",
        direction="UR",
    ):
        self.speak(text, duration, func, size, font, direction)
        self.add(self.speech_bubbles[-1])
