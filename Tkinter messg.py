import tkinter
from tkinter import *
from tkinter import messagebox
root=tkinter.Tk()

def btn_is_clicked():
    messagebox.showwarning("Warning", "This is info window")
root.geometry('400x500')
Button(
    root,
    text='Click here',bg='#000000',
    fg='#ffffff',width=20,height=2, command=btn_is_clicked).pack()
root.mainloop()