# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('red')
# timmy.forward(100)

# print(timmy)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Torterra", "Ground"],
        ["Metagross","Steel"]
    ]
)

table.align = "l"
print(table)
