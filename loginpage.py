import tkinter.messagebox

from databaseoperations import *
from tkinter import *


# Functions

def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)


#def check():
    # Here lies the Check function
    # Check function check the login  ID and passsword and validates it with  the sql database attached


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

submit = Button(frame, text="Submit", command=lambda: check())
submit.grid(row=3, column=5, padx=5, pady=5)

cancel = Button(frame, text="Cancel", command=lambda: frame.quit())
cancel.grid(row=3, column=7, padx=5, pady=5)

label4 = Label(frame)
label4.grid(row=4, column=5,columnspan=3)
root.mainloop()
