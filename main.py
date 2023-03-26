from turtle import Turtle, Screen
import pandas
from annotater import Annotater

screen = Screen()
screen.title("Indian States Game")
screen.screensize(canvwidth=500, canvheight=500)
image1 = "india_map.gif"
image2 = "congrats.gif"
screen.bgpic(image1)
screen.tracer(0)

# olie = turtle.Turtle()
# def get_mouse_click_cor(x,y):
#     print(x, y)
# screen.onscreenclick(get_mouse_click_cor)

data = pandas.read_csv("38_states_and_UTs.csv")
annotater = Annotater()

score = 0
correct_guesses = []

is_game_on = True
while is_game_on:
    screen.update()
    answer_state = screen.textinput(title=f"{score}/36 Guesses Correct", prompt="What's another state's/UT's name?")
    ans_is_in_state = answer_state.title() in data["state"].unique()
    if ans_is_in_state:
        if answer_state in correct_guesses:
            print("Already answered")
        else:
            correct_guesses.append(answer_state.title())
            score = len(correct_guesses)
            annotater.annotate(answer_state)
        print(correct_guesses)
        if score == 36:
            is_game_on = False
            annotater.clear()
            screen.bgpic(image2)

screen.mainloop()
