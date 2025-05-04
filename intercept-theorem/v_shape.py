from manim import *
import sys

sys.path.append("/Users/omidsedighi-mornani/Desktop/mathe/PROJECTS")
from intercept_shape import InterceptShape


class VShape(InterceptShape):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ray1 = Line(LEFT * 0.5, 3 * RIGHT, color=self.ray_color)
        self.ray2 = Line(DL * 0.5, 2.5 * UR, color=self.ray_color)
        self.line1 = Line(1.5 * UP + 0.5 * UR, DR, color=self.ray_color)
        self.line2 = self.line1.copy().shift(RIGHT)
        self.label_line1 = MathTex("g", color=self.ray_color).next_to(
            self.line1, direction=DOWN, buff=0.1
        )
        self.label_line2 = MathTex("h", color=self.ray_color).next_to(
            self.line2, direction=DOWN, buff=0.0
        )

        DEFAULT_RADIUS = 0.07

        self.Z = Dot(ORIGIN, color=self.dot_color, radius=DEFAULT_RADIUS)
        self.label_Z = MathTex("Z", color=self.dot_color).next_to(
            self.Z, direction=UP, buff=0.15
        )

        self.A = Dot(
            self.ray1.point_from_proportion(0.38),
            color=self.dot_color,
            radius=DEFAULT_RADIUS,
        )
        self.label_A = MathTex("A", color=self.dot_color).next_to(
            self.A, direction=DL, buff=0.15
        )

        self.A_dash = Dot(
            self.ray1.point_from_proportion(0.67),
            color=self.dot_color,
            radius=DEFAULT_RADIUS,
        )
        self.label_A_dash = MathTex("A'", color=self.dot_color).next_to(
            self.A_dash, direction=DL, buff=0.1
        )

        self.B = Dot(
            self.ray2.point_from_proportion(0.4),
            color=self.dot_color,
            radius=DEFAULT_RADIUS,
        )
        self.label_B = MathTex("B", color=self.dot_color).next_to(
            self.B, direction=UL, buff=0.15
        )

        self.B_dash = Dot(
            self.ray2.point_from_proportion(0.69),
            color=self.dot_color,
            radius=DEFAULT_RADIUS,
        )
        self.label_B_dash = MathTex("B'", color=self.dot_color).next_to(
            self.B_dash, direction=UL, buff=0.1
        )

        self.ZB = Line(self.Z, self.B, color=self.short_line_color)
        self.ZB_dash = Line(
            self.Z.get_edge_center(UP),
            self.B_dash.get_edge_center(UP),
            color=self.long_line_color,
        )

        self.ZA = Line(self.Z, self.A, color=self.short_line_color)
        self.ZA_dash = Line(
            self.Z.get_edge_center(DOWN),
            self.A_dash.get_edge_center(DOWN),
            color=self.long_line_color,
        )

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
        )

        self.add(
            self.ray1,
            self.ray2,
            self.line1,
            self.line2,
            self.label_line1,
            self.label_line2,
            self.Z,
            self.label_Z,
            self.A,
            self.label_A,
            self.A_dash,
            self.label_A_dash,
            self.B,
            self.label_B,
            self.B_dash,
            self.label_B_dash,
            self.ZB,
            self.ZB_dash,
            self.ZA,
            self.ZA_dash,
            self.AB,
            self.AB_dash,
            self.points,
        )
