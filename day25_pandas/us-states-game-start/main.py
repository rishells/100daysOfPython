from turtle import Turtle, Screen
import turtle
import turtle
# from turtle import  Screen
import pandas as pd


FONT = ("Arial", 14, "bold")
class Graphics:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=1280, height=800)
        self.screen.listen()

        self.turtle = Turtle(visible=False)
        self.turtle.speed('fastest')

    def text_at_xy(self, x, y, text):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.write(text, font=FONT)

    def text_onkey(self, x, y, text, key):
        self.screen.onkey(lambda x=x, y=y, text=text: self.text_at_xy(x, y, text), key)

    def text_onmouseclick(self, text):
        self.screen.onclick(lambda x, y, text=text: self.text_at_xy(x, y, text))


# graphics = Graphics()

# graphics.text_at_xy(100, 100, "Static Text")  # just print text at location

# graphics.text_onkey(-100, -100, "On Key Text", "j")  # print text at location when you type "j"

# graphics.text_onmouseclick("On Mouse Click Text")  # print text whereever mouse is clicked

# graphics.screen.mainloop()




screen = Screen()
screen.title("U.S. States Game")
image = "/home/rishells/rcdev/100daysOfPython/day25_pandas/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# 
#screen.exitonclick()

data = pd.read_csv("/home/rishells/rcdev/100daysOfPython/day25_pandas/us-states-game-start/50_states.csv")

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:


    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("/home/rishells/rcdev/100daysOfPython/day25_pandas/us-states-game-start/states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())



