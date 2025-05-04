from manim import *
import math


class IntroScene(Scene):

    def construct(self):

        # OBJECTS
        introTitle = Text("Gauß'sche Summenformel").shift(3 * UP)
        texSum = MathTex(r"\sum_{i=1}^{n}i")
        texFormula = MathTex(r"= \frac{n(n+1)}{2}").shift(2 * RIGHT)
        texSumExpanded = MathTex(r"1 + 2 + ... + (n-1) + n").next_to(
            texFormula, LEFT, buff=0.5
        )
        jeffrey = ImageMobject("JeffreyCrying").scale(1.25).to_corner(DL, buff=0)
        speech_bubble = (
            SVGMobject("speech_bubble", fill_color=WHITE, fill_opacity=0.8)
            .next_to(jeffrey, RIGHT)
            .shift(0.3 * UP)
        )
        speech = Text("Wieso?").move_to(speech_bubble.get_center())
        # RATE FUNCS
        cubic = lambda t: t**3 if (t <= 1 or t >= 0) else (0 if t < 0 else 1)

        # ANIMATIONS
        self.play(Write(introTitle, run_time=1))
        self.wait()
        self.play(Write(texSum))
        self.wait(2)
        self.play(texSum.animate.next_to(texFormula, LEFT, buff=0.5))
        self.play(Write(texFormula))
        self.wait()
        self.play(ReplacementTransform(texSum, texSumExpanded))
        self.wait()
        self.play(FadeIn(jeffrey))
        self.play(FadeIn(speech, rate_func=cubic), FadeIn(speech_bubble))
        self.wait(1)


class Visualization(Scene):
    def construct(self):

        # OBJECTS
        sq = Square(side_length=0.25, fill_opacity=1)

        groupCubesGreen = (
            VGroup(
                *[
                    VGroup(*[sq.copy() for _ in range(j)]).arrange(LEFT, buff=0.75)
                    for j in range(5)
                ]
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.75)
            .set_z_index(1)
        )

        groupCubesWhite = (
            groupCubesGreen.copy()
            .rotate(PI, about_point=groupCubesGreen.get_center())
            .next_to(groupCubesGreen, RIGHT, buff=-3.25)
        )  # -3.25

        groupCubesGreenDiffOrder = VGroup(
            *[
                VGroup(*[groupCubesGreen[i + 1][i - j] for i in range(j, 4)])
                for j in range(0, 4)
            ]
        )

        for i in range(1, 5):
            groupCubesWhite[i].remove(groupCubesWhite[i][0])

        groupAllCubes = VGroup(groupCubesGreen, groupCubesWhite)

        groupCubesBlue = (
            VGroup(*[sq.copy().set(color=BLUE) for _ in range(4)])
            .arrange(DOWN, buff=0.75)
            .next_to(groupAllCubes, RIGHT, buff=0.75)
        )

        groupNumbers = (
            VGroup(Tex("4"), *[Tex(" + " + str(i + 1)) for i in reversed(range(3))])
            .arrange(RIGHT)
            .next_to(groupAllCubes, DOWN, buff=1.1)
            .set(color=TEAL_E)
        )

        braceUP = Brace(groupAllCubes, sharpness=1, direction=UP)
        braceLEFT = Brace(groupAllCubes, sharpness=1, direction=LEFT)
        groupAllCubes.add(groupCubesBlue)
        braceUPnew = Brace(groupAllCubes, sharpness=1, direction=UP).set(color=BLUE)

        nLEFT = MathTex("n").next_to(braceLEFT, LEFT)
        nUP = nLEFT.copy().next_to(braceUP, UP)
        oneUP = Tex("+ 1").next_to(nUP, RIGHT, aligned_edge=DOWN).set(color=BLUE)
        nOneUP = VGroup(nUP, oneUP)
        roundBraces = MathTex("(\hspace{0.9cm})")
        line = Line(0.95 * LEFT + 2 * RIGHT, 0.95 * RIGHT + 2 * RIGHT, color=RED)
        textTwo = MathTex(2, color=RED)
        equalsSign = MathTex("=")
        cuttingLine = Line(
            groupAllCubes.get_corner(UL) + 0.5 * RIGHT,
            groupAllCubes.get_corner(DR) + 0.5 * LEFT,
            color=RED,
        ).scale(1.1)
        texSumExpanded = MathTex(r"1 + 2 + ... + (n-1) + n", color=TEAL_E).next_to(
            equalsSign, LEFT, buff=-0.3
        )
        texSum = MathTex(r"\sum_{i=1}^{n}i", color=TEAL_E).next_to(
            equalsSign, LEFT, buff=-0.3
        )

        # ANIMATIONS
        i = 0
        for number in groupNumbers:
            self.play(FadeIn(groupCubesGreenDiffOrder[i]), FadeIn(number))

            i += 1

        self.play(
            DrawBorderThenFill(groupCubesWhite),
        )

        self.wait(2)

        self.play(FadeIn(braceUP), FadeIn(braceLEFT), Write(nLEFT), Write(nUP))
        self.wait()
        self.play(groupCubesGreen.animate.set(color=GREEN))

        self.wait(2)

        self.play(
            FadeIn(groupCubesBlue),
            Write(oneUP),
            ReplacementTransform(braceUP, braceUPnew),
            nUP.animate.set(color=BLUE),
            nLEFT.animate.set(color=GREEN),
            braceLEFT.animate.set(color=GREEN),
        )
        self.wait()
        self.play(FadeIn(cuttingLine))
        self.wait()
        groupCubesGreenDiffOrder.add(groupNumbers)
        self.play(
            FadeOut(groupCubesBlue),
            # FadeOut(groupCubesGreen),
            FadeOut(groupCubesWhite),
            FadeOut(braceLEFT),
            FadeOut(braceUPnew),
            ReplacementTransform(cuttingLine, line),
            nOneUP.animate.next_to(line, UP, aligned_edge=RIGHT),
            nLEFT.animate.next_to(line, UP, aligned_edge=LEFT),
            FadeIn(textTwo.next_to(line, DOWN)),
            groupCubesGreenDiffOrder.animate.shift(LEFT),
        )
        self.play(
            nOneUP.animate.shift(0.1 * LEFT),
            FadeIn(
                roundBraces.set(color=BLUE)
                .move_to(nOneUP.get_center())
                .shift(0.1 * LEFT)
            ),
            Write(equalsSign.next_to(line, LEFT)),
        )
        self.wait()
        self.play(
            Wiggle(groupNumbers[0]),
            Flash(groupNumbers[0], flash_radius=0.3, num_lines=5),
        )
        self.play(
            Transform(
                nUP,
                MathTex("4", color=TEAL_E).move_to(nUP.get_center()).shift(0.05 * UP),
            ),
            Transform(
                nLEFT,
                MathTex("4", color=TEAL_E).move_to(nLEFT.get_center()).shift(0.05 * UP),
            ),
            rate_func=there_and_back_with_pause,
            run_time=2,
        )
        self.wait()

        self.play(
            groupNumbers.animate.next_to(line, LEFT, buff=2),
            ReplacementTransform(groupCubesGreenDiffOrder, texSumExpanded),
        )
        self.wait()

        self.play(ReplacementTransform(texSumExpanded, texSum))
        finalFormula = VGroup(
            texSum, nLEFT, nOneUP, line, roundBraces, textTwo, equalsSign
        )
        surroundingBox = SurroundingRectangle(finalFormula, color=RED).shift(
            1.15 * LEFT
        )
        self.play(finalFormula.animate.move_to(ORIGIN))
        self.play(Create(surroundingBox, run_time=1))

        self.wait(2)
        self.play(Unwrite(surroundingBox), Unwrite(finalFormula))
        self.wait(2)


class Visualization2(Scene):
    def construct(self):

        # OBJECTS
        groupNumbers = VGroup()
        groupFives = VGroup()
        for i in range(1, 4 + 1):
            groupNumbers.add(MathTex(str(i)))
            groupNumbers.add(MathTex("+")) if i != 4 else groupNumbers.add(MathTex())
            groupFives.add(MathTex("5"))
            groupFives.add(MathTex("+")) if i != 4 else groupFives.add(MathTex())

        # print([groupNumbers])
        groupNumbers.arrange(LEFT)
        groupFives.arrange(LEFT)

        groupNumbersInverted = (
            groupNumbers.copy().arrange(RIGHT).next_to(groupNumbers, DOWN)
        )
        plusSign = MathTex("+", color=YELLOW).next_to(groupNumbersInverted, LEFT)
        line = Line(groupNumbers.get_left(), groupNumbers.get_right()).next_to(
            groupNumbersInverted, DOWN
        )
        SEquals = MathTex("S =", color=YELLOW).next_to(groupNumbers, LEFT)
        groupFives.next_to(line, DOWN)
        braceFives = BraceText(groupFives, "4")
        # ANIMATIONS
        for i in range(0, len(groupNumbers) - 1, 2):
            self.play(
                FadeIn(groupNumbers[i]), FadeIn(groupNumbers[i + 1]), run_time=0.75
            )
        # print([groupNumbersInverted])
        # print([groupNumbers])
        # self.add(groupNumbers.copy())

        self.play(Write(SEquals))
        self.wait()
        self.play(TransformMatchingTex(groupNumbers.copy(), groupNumbersInverted))
        self.play(FadeIn(plusSign))
        self.wait()
        self.play(Write(line))

        for i in range(0, len(groupNumbers) - 1, 2):
            self.play(
                FadeIn(SurroundingRectangle(groupNumbers[i]), rate_func=there_and_back),
                FadeIn(
                    SurroundingRectangle(
                        groupNumbersInverted[len(groupNumbersInverted) - 2 - i]
                    ),
                    rate_func=there_and_back,
                ),
                Write(groupFives[i]),
                groupFives[i].animate.set(color=YELLOW, rate_func=there_and_back),
            )

        self.play(
            FadeIn(*[groupFives[i - 1] for i in range(0, len(groupNumbers) - 1, 2)])
        )
        self.wait()
        self.play(FadeIn(braceFives, run_time=3))

        groupN = VGroup(
            MathTex("1"),
            MathTex("+"),
            MathTex("2"),
            MathTex("+"),
            MathTex("..."),
            MathTex("+"),
            MathTex("(n-1)"),
            MathTex("+"),
            MathTex("n"),
        ).arrange(LEFT, buff=0.5)
        groupNInverted = (
            groupN.copy()
            .arrange(RIGHT, buff=0.5)
            .move_to(groupNumbersInverted.get_center())
        )
        groupNOne = MathTex()

        variableS1 = MathTex("S").move_to(groupNumbers)
        variableS2 = MathTex("S").move_to(groupNumbersInverted)
        self.play(
            FadeOut(SEquals),
            ReplacementTransform(groupNumbers, variableS1),
            ReplacementTransform(groupNumbersInverted, variableS2),
            plusSign.animate.next_to(variableS2, LEFT),
        )
        # 0  #1  #2  #3  #4  #5  #6
        endFormula = MathTex("S", "+", "S", "=", "4", "*", "5")
        endFormula2 = MathTex("2", "*", "S", "=", "4", "*", "5")
        endFormula3 = MathTex("S", "=", "{4", "*", "5\\over", "2}")
        # 0    #1  #2     #3   #4        #5
        transform_list = [
            variableS1,
            plusSign,
            variableS2,
            line,
            braceFives[1],
            MathTex(""),
            groupFives,
        ]
        self.wait()
        self.play(
            *[
                ReplacementTransform(transforming_items, target)
                for transforming_items, target in zip(transform_list, endFormula)
            ],
            FadeOut(braceFives[0]),
        )

        self.wait()

        transformation_indizes_1_2 = [[0, 2, 1, 3, 4, 5, 6], [2, 2, 1, 3, 4, 5, 6]]

        self.play(
            *[
                ReplacementTransform(endFormula[i], endFormula2[j])
                for i, j in zip(*transformation_indizes_1_2)
            ],
            FadeIn(endFormula2[0]),
        )

        self.wait()

        transformation_indizes_2_3 = [[0, 2, 4, 5, 6, 3], [5, 0, 2, 3, 4, 1]]

        self.play(
            *[
                ReplacementTransform(endFormula2[i], endFormula3[j])
                for i, j in zip(*transformation_indizes_2_3)
            ],
            FadeOut(endFormula2[1]),
            # ReplacementTransform(endFormula3[0],MathTex("1+2+3+4").next_to(endFormula3,LEFT))
        )

        self.wait()

        self.remove(endFormula2[2])
        groupNumbers = MathTex("1+2+3+4").next_to(endFormula3[1], LEFT)
        self.play(ReplacementTransform(endFormula3[0], groupNumbers))

        endFormula = VGroup(groupNumbers, endFormula3[1:])
        endFormulaN = MathTex("1 + 2 + ... + (n-1) + n = \\frac{n(n+1)}{2}")
        self.play(
            endFormula.animate.arrange(RIGHT),
        )
        self.wait()
        self.play(endFormula.animate.shift(UP))
        self.wait()
        self.play(Write(endFormulaN.next_to(endFormula, DOWN)))
        self.play(FadeOut(endFormula))
        surroundingBox = SurroundingRectangle(endFormulaN)
        self.play(DrawBorderThenFill(surroundingBox), run_time=3)
        self.wait(2)
        self.play(Unwrite(surroundingBox, run_time=2), Unwrite(endFormulaN))
        self.wait()
