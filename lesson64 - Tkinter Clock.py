# Clock HH:MM:SS AM/PM
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("UCA Time Display")

def time():
    string = strftime("%H:%M:%S: %p")
    label.config(text=string)
    label.after(1000, time)

label = Label(root , font=("ds-digital", 200), background="black", foreground=("green"))
label.pack(anchor="center")

time()
mainloop()


