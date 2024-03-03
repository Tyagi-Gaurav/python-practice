from tkinter import *

window = Tk() # Just like screen in turtle

window.title("My first GUI program")
window.minsize(width=500, height=400)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left",expand=True) #Label wouldn't show up until pack() is called.


def button_clicked():
    print ("I got clicked")
    new_label = input.get() #Get value in entry
    print(new_label)
    my_label["text"] = new_label

button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry/Input
input = Entry(width=10)
input.pack()

# textarea
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of a multi-line text entry")
print (text.get("1.0", END)) # Line1, character 0
text.pack()

# Spinbox (Drop down)
# Scale
# checkbox
# listbox
# radio button
radioState = IntVar()
radioButton1 = Radiobutton(text="option1")
radioButton2 = Radiobutton(text="option2")
radioButton1.place(x=10, y= 10)
radioButton2.place(x=10, y= 30) #Place layout

# grid(column, row)
#window.config(padx=, pady) Add Padding

# Layout - Pack, Place, Grid

# Place - Precise position


window.mainloop()
