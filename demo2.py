from tkinter import *

def login():
    idData = entryID.get()
    pwData = entryPW.get()
    if len(idData) > 0 and len(pwData) > 0:
        if idData == "1234" and pwData == "1234":
            root.deiconify()
            top.destroy()
        else:
            entryID.delete(0, "end")
            entryPW.delete(0, "end")
    else:
        entryID.delete(0, "end")
        entryPW.delete(0, "end")


def exitProgram():
    top.destroy()
    root.destroy()

root = Tk()
root.geometry("400x300+200+100")
top = Toplevel(root)
labID = Label(top,  text="ID", anchor=E, justify=RIGHT, font=("Times", 20))
labPW = Label(top,  text="Password", anchor=E, justify=RIGHT, font=("Times", 20))
entryID = Entry(top)
entryPW = Entry(top, show="*")
btnLogin = Button(top, text="Login", command=login)
btnExit = Button(top, text="Exit", command=exitProgram)
labID.grid(row=0, column=0, sticky=NSEW)
entryID.grid(row=0, column=1, sticky=NSEW)
labPW.grid(row=1, column=0, sticky=NSEW)
entryPW.grid(row=1, column=1, sticky=NSEW)
btnLogin.grid(row=2, column=0, sticky=NSEW)
btnExit.grid(row=2, column=1, sticky=NSEW)

root.withdraw()
root.mainloop()