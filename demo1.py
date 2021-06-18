from tkinter import *
import hashlib

s256 = hashlib.sha256()

def login():
    idData = entryID.get()
    pwData = entryPW.get()
    if len(idData) > 0 and len(pwData) > 0:
        s256.update(pwData.encode("utf-8"))
        pwHash = s256.hexdigest()
        #print(pwHash)
        if idData == "csie" and pwHash == "5515f0912ec4ca5c9537a9c29ed62372869e0f2332c58eb312bd7ca7de850456":
            window.deiconify()
            top.destroy()
        else:
            entryID.delete(0, "end")
            entryPW.delete(0, "end")
    else:
        entryID.delete(0, "end")
        entryPW.delete(0, "end")

def exitProgram():
    top.destroy()
    window.destroy()

flag = True

def setBtnText(num):
    global flag
    if num == 0 and btn0.cget("text") == "":
        if flag:
            btn0.config(text="O", font=("Times", 15), bg="black", fg="white")
        else:
            btn0.config(text="X", font=("Times", 15), bg="black", fg="white")
    elif num == 1 and btn1.cget("text") == "":
        if flag:
            btn1.config(text="O", font=("Times", 15), bg="black", fg="white")
        else:
            btn1.config(text="X", font=("Times", 15), bg="black", fg="white")
    elif num == 2 and btn2.cget("text") == "":
        if flag:
            btn2.config(text="O", font=("Times", 15), bg="black", fg="white")
        else:
            btn2.config(text="X", font=("Times", 15), bg="black", fg="white")
    elif num == 3 and btn3.cget("text") == "":
        if flag:
            btn3.config(text="O", font=("Times", 15), bg="black", fg="white")
        else:
            btn3.config(text="X", font=("Times", 15), bg="black", fg="white")
    elif num == 4 and btn4.cget("text") == "":
        if flag:
            btn4.config(text="O", font=("Times", 15), bg="black", fg="white")
        else:
            btn4.config(text="X", font=("Times", 15), bg="black", fg="white")
    elif num == 5 and btn5.cget("text") == "":
        if flag:
            btn5.config(text="O", font=("Times", 15), bg="black", fg="white")
        else:
            btn5.config(text="X", font=("Times", 15), bg="black", fg="white")
    elif num == 6 and btn6.cget("text") == "":
        if flag:
            btn6.config(text="O", font=("Times", 15), bg="black", fg="white")
        else:
            btn6.config(text="X", font=("Times", 15), bg="black", fg="white")
    elif num == 7 and btn7.cget("text") == "":
        if flag:
            btn7.config(text="O", font=("Times", 15), bg="black", fg="white")
        else:
            btn7.config(text="X", font=("Times", 15), bg="black", fg="white")
    elif num == 8 and btn8.cget("text") == "":
        if flag:
            btn8.config(text="O", font=("Times", 15), bg="black", fg="white")
        else:
            btn8.config(text="X", font=("Times", 15), bg="black", fg="white")

    flag = not flag 

    if btn0.cget("text") == btn1.cget("text") and btn0.cget("text") == btn2.cget("text") and btn0.cget("text") != "":
        if btn0.cget("text") == "O":
            print("player 1 win!!")
        elif btn0.cget("text") == "X":
            print("player 2 win!!")
    
    if btn3.cget("text") == btn4.cget("text") and btn3.cget("text") == btn5.cget("text") and btn3.cget("text") != "":
        if btn3.cget("text") == "O":
            print("player 1 win!!")
        elif btn3.cget("text") == "X":
            print("player 2 win!!")

    if btn6.cget("text") == btn7.cget("text") and btn6.cget("text") == btn8.cget("text") and btn6.cget("text") != "":
        if btn6.cget("text") == "O":
            print("player 1 win!!")
        elif btn6.cget("text") == "X":
            print("player 2 win!!")

    if btn0.cget("text") == btn3.cget("text") and btn0.cget("text") == btn6.cget("text") and btn0.cget("text") != "":
        if btn0.cget("text") == "O":
            print("player 1 win!!")
        elif btn0.cget("text") == "X":
            print("player 2 win!!")

    if btn1.cget("text") == btn4.cget("text") and btn1.cget("text") == btn7.cget("text") and btn1.cget("text") != "":
        if btn1.cget("text") == "O":
            print("player 1 win!!")
        elif btn1.cget("text") == "X":
            print("player 2 win!!")

    if btn2.cget("text") == btn5.cget("text") and btn2.cget("text") == btn8.cget("text") and btn2.cget("text") != "":
        if btn2.cget("text") == "O":
            print("player 1 win!!")
        elif btn2.cget("text") == "X":
            print("player 2 win!!")
    
    if btn0.cget("text") == btn4.cget("text") and btn0.cget("text") == btn8.cget("text") and btn0.cget("text") != "":
        if btn0.cget("text") == "O":
            print("player 1 win!!")
        elif btn0.cget("text") == "X":
            print("player 2 win!!")

    if btn2.cget("text") == btn4.cget("text") and btn2.cget("text") == btn6.cget("text") and btn2.cget("text") != "":
        if btn2.cget("text") == "O":
            print("player 1 win!!")
        elif btn2.cget("text") == "X":
            print("player 2 win!!")

###################################################################################################

window = Tk()
window.geometry("400x400+200+100")
window.withdraw() #先抽起
top = Toplevel(window) #登入介面
labID = Label(top,  text="ID", anchor=E, justify=RIGHT, font=("Times", 20), bg="black", fg="white")
labPW = Label(top,  text="Password", anchor=E, justify=RIGHT, font=("Times", 20), bg="black", fg="white")
entryID = Entry(top, bg="black", fg="white")
entryPW = Entry(top, show="*", bg="black", fg="white")
btnLogin = Button(top, text="Login", command=login, bg="black", fg="white")
btnExit = Button(top, text="Exit", command=exitProgram, bg="black", fg="white")
labID.grid(row=0, column=0, sticky=NSEW)
entryID.grid(row=0, column=1, sticky=NSEW)
labPW.grid(row=1, column=0, sticky=NSEW)
entryPW.grid(row=1, column=1, sticky=NSEW)
btnLogin.grid(row=2, column=0, sticky=NSEW)
btnExit.grid(row=2, column=1, sticky=NSEW)

window.title="Button Test"
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

btn0 =Button(window, text="", command=lambda:setBtnText(0))
btn0.grid(row=0, column=0, sticky=NSEW)
btn1 =Button(window, text="", command=lambda:setBtnText(1))
btn1.grid(row=0, column=1, sticky=NSEW)
btn2 =Button(window, text="", command=lambda:setBtnText(2))
btn2.grid(row=0, column=2, sticky=NSEW)

btn3 =Button(window, text="", command=lambda:setBtnText(3))
btn3.grid(row=1, column=0, sticky=NSEW)
btn4 =Button(window, text="", command=lambda:setBtnText(4))
btn4.grid(row=1, column=1, sticky=NSEW)
btn5 =Button(window, text="", command=lambda:setBtnText(5))
btn5.grid(row=1, column=2, sticky=NSEW)

btn6 =Button(window, text="", command=lambda:setBtnText(6))
btn6.grid(row=2, column=0, sticky=NSEW)
btn7 =Button(window, text="", command=lambda:setBtnText(7))
btn7.grid(row=2, column=1, sticky=NSEW)
btn8 =Button(window, text="", command=lambda:setBtnText(8))
btn8.grid(row=2, column=2, sticky=NSEW)

window.mainloop()
window.withdraw()