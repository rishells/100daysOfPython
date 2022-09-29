from tkinter import *
from tkinter.tix import ButtonBox
from turtle import width

from matplotlib.pyplot import text

# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI program")
window.minsize(500,300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
#my_label.pack()
#my_label.place(x=100, y = 0)
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")


#Button
button = Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1,row=1)

button2 = Button(text="New Button")
button2.grid(column=3,row=0)


# Entry
input = Entry(width=10)
#input.pack()
input.grid(column=4, row=3)










window.mainloop()
