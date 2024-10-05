#A Simple gui clock written in less than 15 lines of code
import os 
from tkinter import *
from time import strftime
main_window =Tk()
label = Label(main_window ,font="arial 40 bold",background="grey",foreground="black")
def time():
    string = strftime("%h: %H: %M: %S")
    label.config(text=string)
    label.after(1000,time)
time()
label.pack(anchor='center')
main_window.mainloop()
