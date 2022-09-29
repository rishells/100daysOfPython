from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300,100)
window.config(padx=20, pady=20)


# Button
def converter():
    miles_input__text = input.get()
    km_value = float(miles_input__text) * 1.609
    km_value_label.config(text=round(km_value,2))

#Button
button = Button(text="Calculate", command=converter)
#button.pack()
button.grid(column=1,row=2)

#Labels
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0,row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

km_value_label = Label(text="0")
km_value_label.grid(column=1,row=1)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)




window.mainloop()