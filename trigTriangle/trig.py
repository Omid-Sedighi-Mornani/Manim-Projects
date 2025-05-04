from manim import *
import sys
sys.path.append('/Users/omidsedighi-mornani/Desktop/mathe/PROJECTS/')
#print(sys.path)
from Library.m_creature import *      

#config.disable_caching = True

class IntroScene(Scene):   
     def construct(self):
        A, B, C = 2 * UR, 2 * DR, 2 * DL

        triangle = VGroup(
            Line(2*DL,2*DR),
            Line(2*DR,2*UR),
            Line(2*UR,2*DL)
        )           
        angle = Angle.from_three_points(B, C, A)
        right_angle = Angle.from_three_points(A, B, C, elbow=True)
        alpha = MathTex(r"\alpha").move_to([-1, -1.5, 0])
        sideLengths = VGroup(
            Text('a').next_to(triangle[0],DOWN),
            Text('b').next_to(triangle[1],RIGHT),
            Text('c').next_to(triangle[2],LEFT,buff=-1.5)
        )

        lines = VGroup(
            VGroup(triangle[0],sideLengths[0]),
            VGroup(triangle[1],sideLengths[1]),
            VGroup(triangle[2],sideLengths[2])
        )

        formulas = VGroup(
                    #10          #1      #2   #3   #4     #5
            MathTex("\\sin","(","\\alpha",")","=","{b","\over","c}"),
            MathTex("\\cos","(","\\alpha",")","=","{a","\over","c}"),
            MathTex("\\tan","(","\\alpha",")","=","{a","\over","b}"),

        ).scale(1.25)

        surroundingRectagle = SurroundingRectangle(formulas[0],buff=0.2).to_edge(RIGHT,buff=4)
        for formula in formulas:
            formula.move_to(surroundingRectagle.get_center_of_mass())

        formulas[0][5].set(color=BLUE_E)
        formulas[0][7].set(color=GREEN_E)
        formulas[1][5].set(color=RED_E)
        formulas[1][7].set(color=GREEN_E)
        formulas[2][7].set(color=RED_E)
        formulas[2][5].set(color=BLUE_E)

        for i in range(3):
            formulas[i][0].set(color=GREY)

        #formulas[1].shift(0.04*UL)
        #formulas[2].shift(0.06*LEFT)
        self.play(FadeIn(triangle, shift=UP)) 
        self.play(FadeIn(alpha, angle))
        self.play(GrowFromCenter(right_angle))  
        for s in sideLengths:
            self.play(FadeIn(s))

        self.wait()
        self.play(
            VGroup(triangle,angle,right_angle,alpha,sideLengths).animate.scale(0.9).to_edge(LEFT)
        )
        self.wait()

        transforming_formulas = formulas.copy()

        self.play(
            FadeIn(transforming_formulas[0]),
            lines[1].animate().set(color=BLUE_E),
            lines[2].animate().set(color=GREEN_E),
            DrawBorderThenFill(surroundingRectagle)
            )

        self.play(
            ReplacementTransform(transforming_formulas[0],transforming_formulas[1]),
            lines[1].animate.set(color=WHITE),
            lines[0].animate.set(color=RED_E)
        )
        self.play(
            ReplacementTransform(transforming_formulas[1],transforming_formulas[2]),
            lines[2].animate.set(color=WHITE),
            lines[1].animate.set(color=BLUE_E),
        )

        self.wait()

        self.play(
            formulas.animate.arrange(DOWN),
            lines[2].animate.set(color=GREEN_E),
            FadeOut(surroundingRectagle),
            FadeOut(transforming_formulas[2])
        )

        mcreature = MCreature().to_corner(DR)

        self.play(DrawBorderThenFill(mcreature))
        self.play(mcreature.blink_eyes())
        self.play(mcreature.speak("Woher??",direction="DL"))
        self.play(mcreature.move_iris(LEFT))
        self.wait()
        self.play(mcreature.blink_eyes())
        self.play(mcreature.speak("...", direction="UL",font="Helvetica"))
        self.wait()
        self.play(mcreature.blink_eyes())
        self.play(mcreature.move_iris(RIGHT))
        #self.play(mcreature.roll_eyes())
        self.play(
            FadeOut(formulas),
            mcreature.unspeak(),
            mcreature.unspeak(),
            FadeOut(mcreature),
            VGroup(triangle,angle,right_angle,alpha,sideLengths).animate.scale(1.11).move_to(ORIGIN)
        )

        self.wait(2)
        self.play(Wiggle(VGroup(alpha,angle),scale_value=1.2))
        self.play(lines[1].animate.set(color=BLUE),rate_func=there_and_back,run_time=1)
        self.play(Transform(sideLengths[1],MathTex("Gegenkathete",color=BLUE_E,font_size=60).next_to(sideLengths[1],RIGHT,buff=0)))
        self.wait()
        self.play(lines[0].animate.set(color=RED_A),rate_func=there_and_back,run_time=1)
        self.play(Transform(sideLengths[0],MathTex("Ankathete",color=RED_E,font_size=60).next_to(sideLengths[0],DOWN,buff=0)))
        self.wait()
        self.play(Wiggle(right_angle),scale_value=1.2)
        self.play(lines[2].animate.set(color=GREEN_A),rate_func=there_and_back,run_time=1)
        self.play(Transform(sideLengths[2],MathTex("Hypothenuse",color=GREEN_E,font_size=60).next_to(sideLengths[2],LEFT,buff=0)))
        self.wait()

        formulaNames = VGroup(
                    #0       #1     #2    #3    #4    #5            #6      #7
            MathTex("\\sin","(","\\alpha",")","=","{Gegenkathete","\over","Hypothenuse}"),
            MathTex("\\cos","(","\\alpha",")","=","{Ankathete","\over","Hypothenuse}"),
            MathTex("\\tan","(","\\alpha",")","=","{Gegenkathete","\over","Ankathete}"),

        ).to_corner(UL)

        for i in range(3):
            formulaNames[i][0].set(color=GREY)

        formulaNames[1].next_to(formulaNames[0],DOWN)
        formulaNames[2].next_to(formulaNames[1],DOWN)

        formulaNames[0][5].set(color=BLUE_E)
        formulaNames[0][7].set(color=GREEN_E)
        formulaNames[1][5].set(color=RED_E)
        formulaNames[1][7].set(color=GREEN_E)
        formulaNames[2][7].set(color=RED_E)
        formulaNames[2][5].set(color=BLUE_E)


        #self.play(Create(formulaNames))
        self.wait()
        self.play(VGroup(triangle,angle,right_angle,alpha,sideLengths).animate.scale(0.7).to_corner(RIGHT))
        self.play(
            *[ReplacementTransform(alpha.copy(),formulaNames[i][2]) for i in range(3)],
            *[FadeIn(formulaNames[i][0]) for i in range(3)],
            *[FadeIn(formulaNames[i][1]) for i in range(3)],
            *[FadeIn(formulaNames[i][3]) for i in range(3)],
            run_time=2
        )
        self.play(
            *[FadeIn(formulaNames[i][4]) for i in range(3)]
        )

        self.wait()
        self.play(
            FadeTransform(sideLengths[1].copy(),formulaNames[0][5]),
            FadeTransform(sideLengths[2].copy(),formulaNames[0][7]),
            Write(formulaNames[0][6]),
            run_time=2
        )
        self.wait()
        self.play(
            FadeTransform(sideLengths[0].copy(),formulaNames[1][5]),
            FadeTransform(sideLengths[2].copy(),formulaNames[1][7]),
            Write(formulaNames[1][6]),
            run_time=2
        )
        self.wait()
        self.play(
            FadeTransform(sideLengths[1].copy(),formulaNames[2][5]),
            FadeTransform(sideLengths[0].copy(),formulaNames[2][7]),
            Write(formulaNames[2][6]),
            run_time=2
        )

        self.wait(2)
        
        angle2 = Angle.from_three_points(triangle[2].get_center(),triangle[1].get_top(),triangle[1].get_center())
        beta = MathTex(r"\beta").scale(0.7).next_to(angle2,DOWN,buff=0.2).shift(0.2*LEFT)

        betas = VGroup(
            MathTex(r"\beta"),
            MathTex(r"\beta"),
            MathTex(r"\beta")
        )


        self.play(
           *[ReplacementTransform(formulaNames[i][2],betas[i].move_to(formulaNames[i][2])) for i in range(3)],
            FadeTransform(angle,angle2),
            FadeTransform(alpha,beta),
            lines[0].animate.set(color=BLUE_E),
            lines[1].animate.set(color=RED_E),
            Transform(sideLengths[1],MathTex("Ankathete",color=RED_E,font_size=60).scale(0.7).next_to(triangle[1],RIGHT)),
            Transform(sideLengths[0],MathTex("Gegenkathete",color=BLUE_E,font_size=60).scale(0.7).move_to(sideLengths[0])),
        )

        self.wait()

        self.play(
            Wiggle(VGroup(beta,angle2),scale_value=1.3)
        )

        colors = [BLUE_B, RED_B, GREEN_B]

        for idx, line in enumerate(lines):
            if line == lines[2]:
                self.play(Wiggle(right_angle),scale_value=1.3)

            self.play(
                line.animate.set(color=colors[idx]),
                rate_func=there_and_back
            )
        
            self.wait()

        transformationList = [
            ['a','b','c'],
            ['x','y','z'],
            ['e','f','g'],
            ['a','b','c']
        ]

        directions = [DOWN,RIGHT,LEFT]

        for transformation in transformationList:
            self.play(
                *[Transform(sideLengths[i],MathTex(transformation[i]).set(color=triangle[i].get_color()).next_to(triangle[i],directions[i],buff=0.5)) if i < 2 else Transform(sideLengths[i],MathTex(transformation[i]).set(color=triangle[i].get_color()).next_to(triangle[i],directions[i],buff=-0.7))  for i in range(3)]
            )

            self.wait()

        
        formulasOtherSide = VGroup(
                    #0       #1     #2    #3    #4    #5            #6      #7
            MathTex("\\sin","(","\\beta",")","=","{a","\over","c}"),
            MathTex("\\cos","(","\\beta",")","=","{b","\over","c}"),
            MathTex("\\tan","(","\\beta",")","=","{a","\over","b}"),

        ).arrange(DOWN).move_to(formulaNames.get_left() + RIGHT)

        for i in range(3):
            formulasOtherSide[i][0].set(color=GREY)

        formulasOtherSide[0][5].set(color=RED_E)
        formulasOtherSide[0][7].set(color=GREEN_E)
        formulasOtherSide[1][5].set(color=BLUE_E)
        formulasOtherSide[1][7].set(color=GREEN_E)
        formulasOtherSide[2][7].set(color=BLUE_E)
        formulasOtherSide[2][5].set(color=RED_E)

        self.play(
            ReplacementTransform(formulaNames,formulasOtherSide),
             *[ReplacementTransform(betas[i],formulasOtherSide[i][2]) for i in range(3)],
        )

        self.wait(2)

        formulas.scale(0.8).move_to(formulasOtherSide)

        self.play(
            FadeTransform(angle2,angle),
            FadeTransform(beta,alpha),
            lines[0].animate.set(color=RED_E),
            lines[1].animate.set(color=BLUE_E),
            ReplacementTransform(formulasOtherSide,formulas),
        )

        self.wait()

        self.play(
             VGroup(triangle,angle,right_angle,alpha,sideLengths).animate.scale(1.4).move_to(ORIGIN),
             VGroup(formulas,*[formulasOtherSide[i][2] for i in range(3)]).animate.scale(1.25).to_corner(LEFT)
        )

        self.wait(2)    

        self.play(
            FadeOut(VGroup(lines,alpha,angle,right_angle)),
            Unwrite(VGroup(formulas,*[formulasOtherSide[i][2] for i in range(3)]))
        )

        self.wait(2)


class Thumbnail(Scene):
    def construct(self):
        A, B, C = 2 * UR, 2 * DR, 2 * DL

        triangle = VGroup(
            Line(2*DL,2*DR),
            Line(2*DR,2*UR),
            Line(2*UR,2*DL)
        )           
        angle = Angle.from_three_points(B, C, A)
        right_angle = Angle.from_three_points(A, B, C, elbow=True)
        alpha = MathTex(r"\alpha").move_to([-1, -1.5, 0])
        sideLengths = VGroup(
            Text('a').next_to(triangle[0],DOWN),
            Text('b').next_to(triangle[1],RIGHT),
            Text('c').next_to(triangle[2],LEFT,buff=-1.5)
        )

        lines = VGroup(
            VGroup(triangle[0],sideLengths[0]),
            VGroup(triangle[1],sideLengths[1]),
            VGroup(triangle[2],sideLengths[2])
        )

        formulas = VGroup(
                    #10          #1      #2   #3   #4     #5
            MathTex("\\sin","(","\\alpha",")","=","{b","\over","c}"),
            MathTex("\\cos","(","\\alpha",")","=","{a","\over","c}"),
            MathTex("\\tan","(","\\alpha",")","=","{a","\over","b}"),

        ).scale(1.25)

    
        
        formulas.arrange(DOWN).to_corner(LEFT)
        line_colors = [BLUE_E,RED_E,GREEN_E]
        lines.shift(0.2*LEFT)
        mcreature = MCreature().to_corner(RIGHT).shift(2*UP+0.2*RIGHT)
        title = Tex("Sin", ",",  "Cos", ",", "Tan",font_size=3*DEFAULT_FONT_SIZE).to_corner(UP).shift(0.1*UP)
        subtitle = Tex("im " ,"Dreieck",font_size=3*DEFAULT_FONT_SIZE).to_corner(DOWN).shift(0.1*DOWN)
        subtitle[1].set(color= YELLOW)
        [title[i].set(color=LIGHT_GRAY) if i % 2 == 0 else print() for i in range(5)]

        for idx, line_color in enumerate(line_colors):
            lines[idx].set(color=line_color)

        formulas[0][5].set(color=BLUE_E)
        formulas[0][7].set(color=GREEN_E)
        formulas[1][5].set(color=RED_E)
        formulas[1][7].set(color=GREEN_E)
        formulas[2][7].set(color=RED_E)
        formulas[2][5].set(color=BLUE_E)

        for i in range(3):
            formulas[i][0].set(color=GREY)

        surroundingRectagle = SurroundingRectangle(formulas,buff=0.2)

        self.add(lines,formulas,mcreature,title,subtitle,surroundingRectagle)
        mcreature.add_speech("???",direction="DL")


class Trig(Scene):
    def construct(self):
        quotes = VGroup(
            Tex("\"Die ", "Mathematiker " , "sind eine Art ","Franzosen:"),
            Tex("Redet ", "man zu ihnen, so übersetzen sie es in ihre ", "Sprache", ","),
            Tex("und dann ist es alsobald etwas ", "ganz anderes","\""),
            Tex("-J.W.", " Goethe",font_size=DEFAULT_FONT_SIZE-5)

        ).arrange(DOWN,buff=0.15,aligned_edge=LEFT) 

        color_changes = [

            [1,3],
            [0,2],
            [1],
            [1]
        ]

        for idx, quote in enumerate(quotes):
            for color_change in color_changes[idx]:
                quote[color_change].set(color=YELLOW)

        self.play(Write(quotes[:3],run_time=5))
        self.wait()
        self.play(Write(quotes[3],run_time=2))
        self.wait(2)
        self.play(Unwrite(quotes))
        self.wait()





class EndScene(Scene): 
    def construct(self):
        mcreature = MCreature()
        self.play(DrawBorderThenFill(mcreature))        
        self.play(mcreature.blink_eyes())
        self.play(mcreature.move_iris(UR))
        self.play(mcreature.speak("Danke fürs Zuschauen!",duration=2))
        self.wait()
        self.play(mcreature.move_iris(DOWN))
        self.play(mcreature.unspeak())
        self.play(mcreature.blink_eyes())
        self.wait()
        self.play(mcreature.speak("Lasst gerne ein\nLike & Abo da!",duration=2))
        self.play(mcreature.lower_eyebrows(func=there_and_back,duration=2))
        self.wait()
        self.play(
            mcreature.blink_eyes()
            )
        self.play(mcreature.move_iris(LEFT))
        self.play(
            mcreature.blink_eyes()
        )
        self.play(
            mcreature.write_text(duration=2)
        )
        self.play(mcreature.blink_eyes())

        self.wait()

        self.play(
            mcreature.unspeak()
        )

        self.wait()
        self.play(mcreature.blink_eyes())
        self.play(mcreature.lower_eyebrows())
        self.play(
            mcreature.unwrite_text(duration=1),
            FadeOut(mcreature)
        )
        self.wait(2)
