import tkinter
from tkinter import *
root=tkinter.Tk()
root.title("Buttons")
root.geometry("400x500")


bt=Button(root,text="Button 1",width=15,height=2)  
bt.pack()
#grid()
#place() ---pixels

bt2=Button(root,text="Button 2",width=15,height=2)   
bt2.pack()

bt3=Button(root,text="Button 3",width=15,height=2)    
bt3.pack()

bt4=Button(root,text="Link")
bt4.pack(fill=BOTH)
root.mainloop()
