from tkinter import *

root=Tk()
root.geometry("470x500")
root.title("Calculator")
expression = StringVar()
expression.set("")

entry = Entry(width=38, font=("ARIAL", 20), textvariable=expression)
entry.grid(row=0, column=0, columnspan=4)

op = ["+", "-", "/", "*", "."]

def handleClick(event):
    value = event.widget.cget("text")
    if value == "Clear":
        expression.set("")
        return
    exp = expression.get()
    if value != "=":
        if len(exp) >= 1:
            if expression.get()[-1] in op and value in op:
                return
        expression.set(expression.get()+value)
    else:
        expression.set(eval(expression.get()))


btn7 = Button(text="7", height=3, width=6, font=("ARIAL", 20), bg= "grey")
btn7.grid(row=1, column=0)
btn7.bind("<Button-1>", handleClick)
btn8 = Button(text="8", height=3, width=6, font=("ARIAL", 20), bg= "grey")
btn8.grid(row=1, column=1)
btn8.bind("<Button-1>", handleClick)
btn9 = Button(text="9", height=3, width=6, font=("ARIAL", 20), bg= "grey")
btn9.grid(row=1, column=2)
btn9.bind("<Button-1>", handleClick)
btnPlus = Button(text="+", height=3, width=6, font=("ARIAL", 20), bg= "yellow")
btnPlus.grid(row=1, column=3)
btnPlus.bind("<Button-1>", handleClick)

btn4 = Button(text="4", height=3, width=6, font=("ARIAL", 20), bg= "grey")
btn4.grid(row=2, column=0)
btn4.bind("<Button-1>", handleClick)
btn5 = Button(text="5", height=3, width=6, font=("ARIAL", 20), bg= "grey")
btn5.grid(row=2, column=1)
btn5.bind("<Button-1>", handleClick)
btn6 = Button(text="6", height=3, width=6, font=("ARIAL", 20), bg= "grey")
btn6.grid(row=2, column=2)
btn6.bind("<Button-1>", handleClick)
btnSub = Button(text="-", height=3, width=6, font=("ARIAL", 20), bg= "yellow")
btnSub.grid(row=2, column=3)
btnSub.bind("<Button-1>", handleClick)

btn1 = Button(text="1", height=3, width=6, font=("ARIAL", 20), bg= "grey")
btn1.grid(row=3, column=0)
btn1.bind("<Button-1>", handleClick)
btn2 = Button(text="2", height=3, width=6, font=("ARIAL", 20), bg= "grey")
btn2.grid(row=3, column=1)
btn2.bind("<Button-1>", handleClick)
btn3 = Button(text="3", height=3, width=6, font=("ARIAL", 20), bg= "grey")
btn3.grid(row=3, column=2)
btn3.bind("<Button-1>", handleClick)
btnMult = Button(text="*", height=3, width=6, font=("ARIAL", 20), bg= "yellow")
btnMult.grid(row=3, column=3)
btnMult.bind("<Button-1>", handleClick)

btnDec = Button(text=".", height=3, width=6, font=("ARIAL", 20), bg= "grey")
btnDec.grid(row=4, column=2)
btnDec.bind("<Button-1>", handleClick)
btn0 = Button(text="0", height=3, width=16, font=("ARIAL", 20), bg= "grey")
btn0.grid(row=4, column=0, columnspan=2)
btn0.bind("<Button-1>", handleClick)
btnDiv = Button(text="/", height=3, width=6, font=("ARIAL", 20), bg= "yellow")
btnDiv.grid(row=4, column=3)
btnDiv.bind("<Button-1>", handleClick)
btnEql = Button(text="=", height=3, width=6, font=("ARIAL", 20), bg= "yellow")
btnEql.grid(row=5, column=3)
btnEql.bind("<Button-1>", handleClick)

btnClear = Button(text="Clear", height=3, width=6, font=("ARIAL", 20))
btnClear.grid(row=5, column=2)
btnClear.bind("<Button-1>", handleClick)
btnBrack1 = Button(text="(", height=3, width=6, font=("ARIAL", 20))
btnBrack1.grid(row=5, column=0)
btnBrack1.bind("<Button-1>", handleClick)
btnBrack1 = Button(text=")", height=3, width=6, font=("ARIAL", 20))
btnBrack1.grid(row=5, column=1)
btnBrack1.bind("<Button-1>", handleClick)


root.mainloop()