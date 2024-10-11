from tkinter import *

def button_press(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try: 
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Error: Can't Divide By Zero")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Error: Invalid Syntax")
        equation_text = ""
    except:
        equation_label.set("Error: Unknown Issue")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()

window.title("Calculator")
window.geometry("225x290")

equation_text=""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("Roboto", 16), bg="white", width=24, height=2)
label.pack(pady=5)

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=2, width=2, font=40, command=lambda: button_press(1))
button1.grid(row=1, column=0)
button2 = Button(frame, text=2, height=2, width=2, font=40, command=lambda: button_press(2))
button2.grid(row=1, column=1)
button3 = Button(frame, text=3, height=2, width=2, font=40, command=lambda: button_press(3))
button3.grid(row=1, column=2)
button4 = Button(frame, text=4, height=2, width=2, font=40, command=lambda: button_press(4))
button4.grid(row=2, column=0)
button5 = Button(frame, text=5, height=2, width=2, font=40, command=lambda: button_press(5))
button5.grid(row=2, column=1)
button6 = Button(frame, text=6, height=2, width=2, font=40, command=lambda: button_press(6))
button6.grid(row=2, column=2)
button7 = Button(frame, text=7, height=2, width=2, font=40, command=lambda: button_press(7))
button7.grid(row=3, column=0)
button8 = Button(frame, text=8, height=2, width=2, font=40, command=lambda: button_press(8))
button8.grid(row=3, column=1)
button9 = Button(frame, text=9, height=2, width=2, font=40, command=lambda: button_press(9))
button9.grid(row=3, column=2)
button0 = Button(frame, text=0, height=2, width=2, font=40, command=lambda: button_press(0))
button0.grid(row=4, column=0)
button_plus = Button(frame, text="+", height=2, width=2, font=40, command=lambda: button_press("+"))
button_plus.grid(row=1, column=3)
button_minus = Button(frame, text="-", height=2, width=2, font=40, command=lambda: button_press("-"))
button_minus.grid(row=2, column=3)
button_multiply = Button(frame, text="*", height=2, width=2, font=40, command=lambda: button_press("*"))
button_multiply.grid(row=3, column=3)
button_divide = Button(frame, text="/", height=2, width=2, font=40, command=lambda: button_press("/"))
button_divide.grid(row=4, column=3)
button_decimal = Button(frame, text=".", height=2, width=2, font=40, command=lambda: button_press("."))
button_decimal.grid(row=4, column=1)
button_equals = Button(frame, text="=", height=2, width=2, font=40, command=equals)
button_equals.grid(row=4, column=2)
button_clear = Button(frame, text="AC", height=2, width=20, font=40, command=clear)
button_clear.grid(row=0, column=0, columnspan=4)

window.mainloop()
