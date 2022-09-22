from turtle import Turtle, Screen
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


graphics = Graphics()

graphics.text_at_xy(100, 100, "Static Text")  # just print text at location

graphics.text_onkey(-100, -100, "On Key Text", "j")  # print text at location when you type "j"

graphics.text_onmouseclick("On Mouse Click Text")  # print text whereever mouse is clicked

graphics.screen.mainloop()



screen = Turtle.Screen()
screen.title("U.S. States Game")
image = "/home/rishells/rcdev/100daysOfPython/day25_pandas/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#screen.exitonclick()

data = pd.read_csv("/home/rishells/rcdev/100daysOfPython/day25_pandas/us-states-game-start/50_states.csv")

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

found = data[data['state'].str.contains(answer_state)]
print(found.to_numpy)


#states_list = answer_state.tolist()

#print(answer_state.isin(states))

