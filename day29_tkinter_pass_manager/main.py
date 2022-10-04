from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #



def save():
    data_file = open("/home/rishells/rcdev/100daysOfPython/day29_tkinter_pass_manager/data.txt", "a")
    data_file.write("test")
    data_file.close()
    print("Add button clicked")
# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="/home/rishells/rcdev/100daysOfPython/day29_tkinter_pass_manager/logo.png")
canvas.create_image(100,100,image = lock_image)
canvas.grid(column=1,row=0)

#Buttons


def generate_password():
    print("Generate Password button clicked")

add_button = Button(text="Add",command=save,width=32)
add_button.grid(column=1,row=4, columnspan=2)

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)


#Labels

website_label = Label(text="Website")
website_label.grid(column=0,row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1,columnspan=2)
website_entry.focus()

email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2,columnspan=2)
email_user_entry.insert(0,"ricardoconchas@gmail.com")

password_entry = Entry(width=16)
password_entry.grid(column=1, row=3)





window.mainloop()