from manim import *


class Test(Scene):
    def construct(self):
        speechbubble = SpeechBubble("Test!")

        self.add(speechbubble)


class SpeechBubble(VMobject):

    def __init__(
        self,
        text,
        alignment="DL",
        text_font="Chalkboard",
        font_size=DEFAULT_FONT_SIZE,
        buff=1,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.text = text
        self.textBox = MarkupText(self.text, font=text_font, font_size=font_size)
        self.bubble = RoundedRectangle(
            corner_radius=0.5,
            height=self.textBox.height + buff,
            width=max(self.textBox.width + buff, 1.5),
        )

        line3 = Line(ORIGIN, [1, -0.45, 0]).shift(UP)
        line1 = Line(ORIGIN, line3.get_anchors()[0])
        line2 = Line(ORIGIN, line3.get_anchors()[1])

        self.lines = (
            VGroup(line1, line2)
            .next_to(self.bubble.get_corner(DL))
            .shift(0.2 * DL + 0.05 * UL + 0.1 * UP)
        )

        match alignment:
            case "UR":
                VGroup(self.bubble, self.lines).flip([1, 0, 0]).flip([0, 1, 0])
            case "UL":
                VGroup(self.bubble, self.lines).flip([1, 0, 0])
            case "DR":
                VGroup(self.bubble, self.lines).flip([0, 1, 0])

        self.textBox.move_to(self.bubble.get_center_of_mass())

        self.speech_bubble = VGroup(self.bubble, self.textBox, self.lines)
        self.add(self.speech_bubble)

    def speak(self, duration=1) -> Animation:
        return AnimationGroup(
            DrawBorderThenFill(self.bubble, run_time=duration),
            DrawBorderThenFill(self.lines, run_time=duration),
            Write(self.textBox, run_time=duration),
        )

    def unspeak(self, duration=1) -> Animation:
        return AnimationGroup(
            Unwrite(self.bubble, run_time=duration),
            Unwrite(self.lines, run_time=duration),
            Unwrite(self.textBox, run_time=duration),
        )
