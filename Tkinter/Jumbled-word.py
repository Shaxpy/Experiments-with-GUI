#Project based on solving the Jumbled words in tkinter
import tkinter
from tkinter import *
root=tkinter.Tk()
import random
from tkinter import messagebox


answers = [
"python",
"java",
"swift",
"canada",
"india",
"america",
"london",
"asia",
"antarctica",
"scramble",
"astronaut",
"astronaut",
"cricket",
"portuguese",
"america",
"europe",
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
    "siaa",
    "ataractic",
    "clambers",
    "saturanto ",
    "aurnattos ",
    "cretick",
    "superego ",
    "cameria ",
    "purreo",

]
def default():
    global words,answers,num
    lbl.config(text=words[num])

def reset():
    num=random.randrange(0,16,1)
    lbl.config(text=words[num])
    a1.delete(0,END)
num=random.randrange(0,16,1)


def ans_check():
    var=a1.get()
    if var==answers[num]:
        messagebox.showinfo("Success", "You win")
        reset()
    else:
        messagebox.showerror("Failure","Try again")
        a1.delete(0,END)

ans=StringVar()
root.geometry('500x600')
root.config(background='#000000')
root.title('Jumbled')
lbl= Label(
root,
text='This is easy',
font=('Yerdana',25),
bg='#000000',
fg='#ffffff'
)
lbl.pack(ipady=30,pady=50)

a1=Entry(
root,
font=('Verdana',24),textvariable=ans,
)
a1.pack(ipady=30,pady=30)
btn=Button(
    root,text='Check',font=('Times New Roman',16),
    fg='#ffffff',
    bg='#192A56',
    relief=GROOVE,command=ans_check
)
btn.pack()

btn1=Button(
    root,text='Reset',font=('Times New Roman',16),
    fg='#ffffff',
    bg='#019031',
    relief=GROOVE,
    command=reset,
)
btn1.pack(pady=30)
default()
root.mainloop()