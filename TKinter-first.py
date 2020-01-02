import tkinter
root=tkinter.Tk()
root.title("login")

 
w=500
h=400
 
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=int(ws/2-w/2)
y=int(hs/2-h/2)
data=str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)

root.configure(background="#000000")
root.geometry(data)

root.mainloop()