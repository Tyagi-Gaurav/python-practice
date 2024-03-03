from tkinter import *


def calculate():
    miles = input.get()
    if miles != "":
        result_label.config(text=f"{float(miles) * 1.609}")


window = Tk()
window.title("Mile ot Km converter")
window.minsize(width=400, height=200)

input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 24))
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=("Arial", 24))
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=10, pady=10)

result_label = Label(text="0", font=("Arial", 24))
result_label.grid(column=1, row=1)
result_label.config(padx=10, pady=10)

km_label = Label(text="km", font=("Arial", 24))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=3)

window.mainloop()
