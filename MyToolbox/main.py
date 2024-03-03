from tkinter import *
from tkinter import messagebox
import password_gen
import pyperclip


def add():
    website_name = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website_name.strip() == "" or email.strip() == "" or password.strip() == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                       message=f"Details entered: \nEmail: {email}. \nPassword: {password}. Ok to save?")

        if is_ok:
            with open("password.txt", mode="a") as file:
                file.write(f"{website_name} | {email} | {password}\n")

        clear_fields()


def clear_fields():
    website_input.delete(0, END)
    email_input.delete(0, END)
    email_input.insert(0, "test@email.com")
    password_input.delete(0, END)


def gen_password():
    password = password_gen.generate(4, 4, 4)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


window = Tk()

window.title("Password Manager")
window.config(width=300, height=300, padx=50, pady=50)

canvas_background = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=canvas_background)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=("Arial", 18, "bold"))
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username: ", font=("Arial", 18, "bold"))
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.insert(0, "test@email.com")
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password: ", font=("Arial", 18, "bold"))
password_label.grid(column=0, row=3)

password_input = Entry(width=18)
password_input.grid(column=1, row=3)

generate_pwd_button = Button(text="Generate Password", width=13, command=gen_password)
generate_pwd_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
