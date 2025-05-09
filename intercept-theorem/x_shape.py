from manim import *
import sys

sys.path.append("/Users/omidsedighi-mornani/Desktop/mathe/PROJECTS")
from intercept_shape import InterceptShape


class XShape(InterceptShape):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ray1 = Line(LEFT * 0.5, 3 * RIGHT, color=self.ray_color)
        self.ray2 = Line(DL * 0.5, 2.5 * UR, color=self.ray_color).move_to(self.ray1)
        self.line1 = (
            Line(1.5 * UP + 0.5 * UR, DR, color=self.ray_color)
            .move_to(self.ray1)
            .shift(LEFT)
        )
        self.line2 = self.line1.copy().move_to(self.ray1).shift(1.3 * RIGHT)
        self.label_line1 = MathTex("g", color=self.ray_color).next_to(
            self.line1, direction=DOWN
        )
        self.label_line2 = MathTex("h", color=self.ray_color).next_to(
            self.line2, direction=DOWN
        )

        self.Z = Dot(self.ray1.point_from_proportion(0.5), color=self.dot_color)
        self.label_Z = MathTex("Z", color=self.dot_color).next_to(self.Z, direction=UP)
        self.A = Dot(self.ray1.point_from_proportion(0.21), color=self.dot_color)
        self.label_A = MathTex("A", color=self.dot_color).next_to(
            self.A, direction=UL, buff=0.15
        )

        self.A_dash = Dot(self.ray1.point_from_proportion(0.87), color=self.dot_color)
        self.label_A_dash = MathTex("A'", color=self.dot_color).next_to(
            self.A_dash, direction=DL, buff=0.1
        )

        self.B = Dot(self.ray2.point_from_proportion(0.21), color=self.dot_color)
        self.label_B = MathTex("B", color=self.dot_color).next_to(
            self.B, direction=UL, buff=0.15
        )

        self.B_dash = Dot(self.ray2.point_from_proportion(0.87), color=self.dot_color)
        self.label_B_dash = MathTex("B'", color=self.dot_color).next_to(
            self.B_dash, direction=UL, buff=0.1
        )

        self.ZA = Line(self.Z, self.A, color=self.short_line_color)
        self.ZA_dash = Line(self.Z, self.A_dash, color=self.long_line_color)
        self.ZB = Line(self.Z, self.B, color=self.short_line_color)
        self.ZB_dash = Line(self.Z, self.B_dash, color=self.long_line_color)

        self.AB = Line(self.A, self.B, color=self.short_line_color)
        self.AB_dash = Line(self.A_dash, self.B_dash, color=self.long_line_color)

        self.dots = VGroup(
            self.Z,
            self.A,
            self.B,
            self.A_dash,
            self.B_dash,
            self.label_Z,
            self.label_A,
            self.label_B,
            self.label_A_dash,
            self.label_B_dash,
        ).set_z_index(1)

        self.add(
            self.ray1,
            self.ray2,
            self.line1,
            self.line2,
            self.label_line1,
            self.label_line2,
            self.A,
            self.label_A,
            self.A_dash,
            self.label_A_dash,
            self.B,
            self.label_B,
            self.B_dash,
            self.label_B_dash,
            self.Z,
            self.label_Z,
            self.ZA,
            self.ZA_dash,
            self.ZB,
            self.ZB_dash,
            self.AB,
            self.AB_dash,
            self.dots,
        )
