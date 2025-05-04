from manim import *
import random

class MCreature(Scene):

    def construct(self):
        # Draw the 'M' shape
        m_shape = Tex("M", color=WHITE, stroke_width=0).scale(6)
        # Draw eyes
        self.left_eye = Circle(radius=0.3, color=BLACK, fill_color=WHITE, fill_opacity=1).shift(LEFT*0.8 + UP*0.5)
        self.right_eye = Circle(radius=0.3, color=BLACK, fill_color=WHITE, fill_opacity=1).shift(RIGHT*0.8 + UP*0.5)
        
        

        # Draw iris
        self.left_iris = Circle(radius=0.1, color=BLACK, fill_color=BLACK, fill_opacity=1).shift(LEFT*0.8 + UP*0.5)
        self.right_iris = Circle(radius=0.1, color=BLACK, fill_color=BLACK, fill_opacity=1).shift(RIGHT*0.8 + UP*0.5)
        
        #Draw reflection
        self.reflection_left = Circle(radius=0.05, color=WHITE, fill_color=WHITE, fill_opacity=1).move_to(self.left_iris.get_left()).shift(0.02*UP)
        self.reflection_right = Circle(radius=0.05, color=WHITE, fill_color=WHITE, fill_opacity=1).move_to(self.right_iris.get_left()).shift(0.02*UP)

        self.left_pupil = VGroup(self.left_iris,self.reflection_left)
        self.right_pupil = VGroup(self.right_iris,self.reflection_right)


        # Draw eyelids
        self.left_eyelid = Arc(radius=0.3, angle=PI, color=BLUE, fill_color=BLUE, fill_opacity=1).move_to(self.left_eye).shift(UP*0.3)
        self.right_eyelid = Arc(radius=0.3, angle=PI, color=BLUE, fill_color=BLUE, fill_opacity=1).move_to(self.right_eye).shift(UP*0.3)

        self.creatureM = VGroup(m_shape,self.left_eye,self.right_eye,self.left_pupil,self.right_pupil,self.left_eyelid,self.right_eyelid)
        self.creatureM.move_to(2.5*DL + 1.5*LEFT)
        name = Tex("athe für Dullies").scale(2).next_to(m_shape,RIGHT,aligned_edge=DOWN)
        self.speech_bubble = SVGMobject("speech_bubble", fill_color=WHITE,fill_opacity=0.8).scale(2).next_to(self.creatureM, RIGHT).shift(2*UP).stretch_to_fit_height(6).stretch_to_fit_height(4)
        self.text = Text("Danke fürs \nZuschauen!",font="Chalkboard").move_to(self.speech_bubble).shift(0.1*UR)
        self.play(DrawBorderThenFill(self.creatureM),run_time=1)
        #self.play(
         #   FadeIn(self.speech_bubble),
          #  Write (self.text)
           # )
        self.raise_eyebrows()
        self.move_iris(UR)
        self.wait()
        self.move_iris(DOWN)
        self.blink_eyes()
        self.wait()
        self.play(Write(name))
        self.blink_eyes()
        self.wait()

    def raise_eyebrows(self):
        self.play(
            self.left_eyelid.animate.shift(DOWN*0.1),
            self.right_eyelid.animate.shift(DOWN*0.1),
            run_time=0.5
        )
        self.wait(0.3)
        self.play(
            self.left_eyelid.animate.shift(UP*0.1),
            self.right_eyelid.animate.shift(UP*0.1),
            run_time=0.5
        )

    def blink_eyes(self):
        self.play(
            self.left_eye.animate.stretch_to_fit_height(0.1*self.left_eye.get_height()),
            self.right_eye.animate.stretch_to_fit_height(0.1*self.right_eye.get_height()),
            self.left_pupil.animate.stretch_to_fit_height(0.1*self.left_iris.get_height()),
            self.right_pupil.animate.stretch_to_fit_height(0.1*self.right_iris.get_height()),
            run_time=0.3
        )
        self.play(
            self.left_eye.animate.stretch_to_fit_height(10*self.left_eye.get_height()),
            self.right_eye.animate.stretch_to_fit_height(10*self.right_eye.get_height()),
            self.left_pupil.animate.stretch_to_fit_height(10*self.left_iris.get_height()),
            self.right_pupil.animate.stretch_to_fit_height(10*self.right_iris.get_height()),
            run_time=0.3
        )

    def move_iris(self, direction):
        self.play(
            self.left_pupil.animate.shift(direction*0.1),
            self.right_pupil.animate.shift(direction*0.1),
            run_time=1
        )



