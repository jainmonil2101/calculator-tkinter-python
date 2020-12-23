from tkinter import *

calc = Tk()
calc.title("Calculator")
calc.resizable(False, False)

textInput = StringVar()
operator = ""

def clear_button():
    global operator
    operator =""
    textInput.set(operator)

def showText(numbers):
    global operator
    operator = operator + str(numbers)
    textInput.set(operator)

def calculate():
    global operator
    answer = eval(operator)
    textInput.set(answer)
    operator = ''
    


textDisplay = Entry(calc, font=("Arial", 20, "bold"), textvariable=textInput, bg="#45b6fe", bd=26,justify="right")
textDisplay.grid(columnspan=4)

btn7 = Button(calc, pady=12, padx=16, font=("Arial", 20, "bold"), text=7, bg="#45b6fe", bd=8, command=lambda:showText(7))
btn7.grid(row=1, column=0)

btn8 = Button(calc, pady=12, padx=16, font=("Arial", 20, "bold"), text=8, bg="#45b6fe", bd=8, command=lambda:showText(8))
btn8.grid(row=1, column=1)

btn9 = Button(calc, pady=12, padx=16, font=("Arial", 20, "bold"), text=9, bg="#45b6fe", bd=8, command=lambda:showText(9))
btn9.grid(row=1, column=2)

addBtn = Button(calc, pady=12, padx=16, font=("Arial", 20, "bold"), text="+", bg="#45b6fe", bd=8, command=lambda:showText("+"))
addBtn.grid(row=1, column=3)


btn4 = Button(calc, pady=12, padx=16, font=("Arial", 20, "bold"), text=4, bg="#45b6fe", bd=8, command=lambda:showText(4))
btn4.grid(row=2, column=0)

btn5 = Button(calc, pady=12, padx=16, font=("Arial", 20, "bold"), text=5, bg="#45b6fe", bd=8, command=lambda:showText(5))
btn5.grid(row=2, column=1)

btn6 = Button(calc, pady=12, padx=16, font=("Arial", 20, "bold"), text=6, bg="#45b6fe", bd=8, command=lambda:showText(6))
btn6.grid(row=2, column=2)

subtractBtn = Button(calc, pady=12, padx=19, font=("Arial", 20, "bold"), text="-", bg="#45b6fe", bd=8, command=lambda:showText("-"))
subtractBtn.grid(row=2, column=3)

btn1 = Button(calc, pady=12, padx=16, font=("Arial", 20, "bold"), text=1, bg="#45b6fe", bd=8, command=lambda:showText(1))
btn1.grid(row=3, column=0)

btn2 = Button(calc, pady=12, padx=16, font=("Arial", 20, "bold"), text=2, bg="#45b6fe", bd=8, command=lambda:showText(2))
btn2.grid(row=3, column=1)

btn3 = Button(calc, pady=12, padx=16, font=("Arial", 20, "bold"), text=3, bg="#45b6fe", bd=8, command=lambda:showText(3))
btn3.grid(row=3, column=2)

multiplyBtn = Button(calc, pady=12, padx=16, font=("Arial", 20, "bold"), text="x", bg="#45b6fe", bd=8, command=lambda:showText("*"))
multiplyBtn.grid(row=3, column=3)


btn0 = Button(calc, pady=12, padx=16, font=("Arial", 20, "bold"), text=0, bg="#45b6fe", bd=8, command=lambda:showText(0))
btn0.grid(row=4, column=0)

btnClear = Button(calc, pady=12, padx=14, font=("Arial", 20, "bold"), text="C", bg="#45b6fe", bd=8, command=clear_button)
btnClear.grid(row=4, column=1)

btnEquals = Button(calc, pady=12, padx=16, font=("Arial", 20, "bold"), text="=", bg="#45b6fe", bd=8, command=calculate)
btnEquals.grid(row=4, column=2)

divideBtn = Button(calc, pady=12, padx=19, font=("Arial", 20, "bold"), text="/", bg="#45b6fe", bd=8, command=lambda:showText("/"))
divideBtn.grid(row=4, column=3)

calc.mainloop()