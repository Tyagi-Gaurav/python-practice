from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(width=300, height=300, padx=20, pady=20)

canvas_background = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=canvas_background)
canvas.grid(column=1, row=1)

window.mainloop()