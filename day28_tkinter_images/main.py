
from threading import main_thread
from tkinter import *

from idna import check_initial_combiner
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
fg=GREEN
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/home/rishells/rcdev/100daysOfPython/day28_tkinter_images/tomato.png")
canvas.create_image(100, 112, image = tomato_img)
canvas.create_text(100, 130, text="00:00",fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

#Buttons
def start():
    print("Start button clicked")

def reset():
    print("Reset button clicked")

start_button = Button(text="Start",command=start)
start_button.grid(column=0,row=2)
reset_button = Button(text="Reset",command=reset)
reset_button.grid(column=2,row=2)

#Labels
main_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50 ))
main_label.grid(column=1,row=0)

check_mark_label = Label(text="✓", fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1,row=3)



window.mainloop()









