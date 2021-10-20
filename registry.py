from databaseoperations import *
from tkinter import *
import tkinter.messagebox


# Functions
def clear():
    entry1.delete(0,END)
    entry2.delete(0,END)


def register():
    response = tkinter.messagebox.askokcancel("Confirm","Are You sure about submitting details??")
    if response:
        insert_data(entry1.get(), entry2.get())
    else:
        clear()
    # register
    # Register function creates the login  ID and passsword and adds it to the sql database attached


# GUI

root = Tk()
canvas = Canvas(root, height=480, width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.6)

label1 = Label(frame, text="Login")
label1.grid(row=0, column=5, columnspan=3, pady=2)

label2 = Label(frame, text="User ID")
label2.grid(row=1, column=5, padx=5, pady=5)

entry1 = Entry(frame)
entry1.grid(row=1, column=7, padx=5, pady=5)

label3 = Label(frame, text="Password")
label3.grid(row=2, column=5, padx=5, pady=5)

entry2 = Entry(frame,show="*")
entry2.grid(row=2, column=7, padx=5, pady=5)

clean = Button(frame, text="Clear", command=lambda: clear())
clean.grid(row=3, column=6, padx=5, pady=5)

submit = Button(frame, text="Register", command=lambda: register())
submit.grid(row=3, column=5, padx=5, pady=5)

cancel = Button(frame, text="Cancel", command=lambda: frame.quit())
cancel.grid(row=3, column=7, padx=5, pady=5)

root.mainloop()
