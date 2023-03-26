from turtle import Turtle
import pandas

data = pandas.read_csv("38_states_and_UTs.csv")
df = data.set_index("state", drop=False)

class Annotater(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("red")

    def annotate(self, answer_state):
        """To annotate the states on the map"""
        x_cor = df.loc[answer_state.title(), "x"]
        y_cor = df.loc[answer_state.title(), "y"]
        self.goto(x_cor, y_cor)
        self.write(arg=answer_state.title(), move=False, align="center", font=('Arial', 8, 'normal'))
