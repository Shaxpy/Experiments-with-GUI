import tkinter
from tkinter import *
from tkinter import messagebox

root=tkinter.Tk()
root.geometry('400x500')
root.configure(background='#000000')

a1=Entry(
    root,
    font=('Times New Roman',16)
).pack(ipadx=10,pady=50)
#padding


root.mainloop()