from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import pyclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    #password_list = []
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]


    '''
    List comprehension examples
    #Using list comprehension

    new_list2 = [n + 1 for n in numbers]

    name = "Ricardo"
    new_name_list = [letter for letter in name]

    # LC using range function
    number_list = [num * 2 for num in range(1,5)]

    #LC using validation and modification to the return object
    names = ['Ricardo','Axel','Yadira','Rac','Toto']
    long_names = [name.upper() for name in names if len(name)> 4]
    '''

    # Next 3 for loops were replace by list comprehension above
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # password_list =[random.choice(letters) for char in letters]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)
    #print(f"Your password is: {password}")
    password_entry.insert(0,string=password)
    #pyperclip.copy(password)
    #pyclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #





def save():

    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email)==0 or len (password)==0:
        messagebox.showwarning(title="Oops",message="Please don't leave any fields empty!")
    else:  
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it ok to save? ")
        
        #messagebox.showinfo(title="Title", message="Message")
        if is_ok:
            data_file = open("/home/rishells/rcdev/100daysOfPython/day29_tkinter_pass_manager/data.txt", "a")
            data_file.write(f"{website_entry.get()} | {email_user_entry.get()} | {password_entry.get()}\n")
            data_file.close()
            clear_entries()
            print("Add button clicked")
# ---------------------------- UI SETUP ------------------------------- #


def clear_entries():
    website_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="/home/rishells/rcdev/100daysOfPython/day29_tkinter_pass_manager/logo.png")
canvas.create_image(100,100,image = lock_image)
canvas.grid(column=1,row=0)

#Buttons




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