from tkinter import *
from turtle import width

window = Tk()
window.title("My First GUI program")
window.minsize(500,300)


# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()


# Entry
input = Entry(width=10)
input.pack()










window.mainloop()
