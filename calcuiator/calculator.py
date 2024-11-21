from tkinter import *
import math as m

window = Tk()
window.geometry('383x600+470+20')
window.title('Cal')
window.config(bg="gray11")
window.resizable(False, False)

def close():
    window.destroy()

def clear():
    entry.delete(0, END)

def back():
    entry.delete(len(entry.get()) - 1)

def press(input):
    length = len(entry.get())
    entry.insert(length, input)

def add(a, b):
    return float(a) + float(b)

def subtract(a, b):
    return float(a) - float(b)

def multiply(a, b):
    return float(a) * float(b)

def divide(a, b):
    return float(a) / float(b)

def expression_break(sign, expression):
    values = expression.split(sign, 1)
    return values

def scientific(expression):
    data = expression_break("(", expression)
    if data[0] == "tan":
        result = m.tan(float(data[1]))
    elif data[0] == "cos":
        result = m.cos(float(data[1]))
    elif data[0] == "sin":
        result = m.sin(float(data[1]))
    elif data[0] == "sqrt":
        result = m.sqrt(float(data[1]))
    elif data[0] == "log":
        result = m.log(float(data[1]))
    elif data[0] == "ln":
        result = m.log(float(data[1]))
    elif data[0] == "deg":
        result = m.degrees(float(data[1]))
    elif data[0] == "rad":
        result = m.radians(float(data[1]))
    elif data[0] == "fac":
        result = m.factorial(int(data[1]))  # factorial требует целое число
    return result

def equal():
    expression = entry.get()
    clear()
    try:
        if "(" in expression:
            result = scientific(expression)
        elif "pow" in expression:
            data = expression_break("pow", expression)
            result = m.pow(float(data[0]), float(data[1]))
        elif "rem" in expression:
            data = expression_break("rem", expression)
            result = m.remainder(float(data[0]), float(data[1]))
        elif "×" in expression:
            data = expression_break("×", expression)
            result = multiply(data[0], data[1])
        elif "*" in expression:
            data = expression_break("*", expression)
            result = multiply(data[0], data[1])
        elif "÷" in expression:
            data = expression_break("÷", expression)
            result = divide(data[0], data[1])
        elif "/" in expression:
            data = expression_break("/", expression)
            result = divide(data[0], data[1])
        elif "+" in expression:
            data = expression_break("+", expression)
            result = add(data[0], data[1])
        elif "-" in expression:
            data = expression_break("-", expression)
            result = subtract(data[0], data[1])
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

entry_string = StringVar()
entry = Entry(window, textvariable=entry_string, foreground="white",
              background="gray20", border=0, font=("Bahnschrift semibold", 26))
entry.grid(columnspan=4, ipady=15)

font_value = ("Calibri", 18)

btn_tan = Button(window, text="tan", background="gray11",
                 foreground="Darkorange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda: press("tan("))
btn_tan.grid(column=0, row=1, sticky=E+W, ipady=5)

btn_cos = Button(window, text="cos", background="gray11",
                 foreground="Darkorange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda: press("cos("))
btn_cos.grid(column=1, row=1, sticky=E+W, ipady=5)

btn_sin = Button(window, text="sin", background="gray11",
                 foreground="Darkorange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda: press("sin("))
btn_sin.grid(column=2, row=1, sticky=E+W, ipady=5)

btn_sqrt = Button(window, text="sqrt", background="gray11",
                  foreground="Darkorange1", font=font_value, borderwidth=1,
                  relief=SOLID, command=lambda: press("sqrt("))
btn_sqrt.grid(column=3, row=1, sticky=E+W, ipady=5)

btn_log = Button(window, text="log", background="gray11",
                 foreground="Darkorange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda: press("log("))
btn_log.grid(column=0, row=2, sticky=E+W, ipady=5)

btn_ln = Button(window, text="ln", background="gray11",
                foreground="Darkorange1", font=font_value, borderwidth=1,
                relief=SOLID, command=lambda: press("ln("))
btn_ln.grid(column=1, row=2, sticky=E+W, ipady=5)

btn_deg = Button(window, text="deg", background="gray11",
                 foreground="Darkorange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda: press("deg("))
btn_deg.grid(column=2, row=2, sticky=E+W, ipady=5)

btn_rad = Button(window, text="rad", background="gray11",
                 foreground="Darkorange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda: press("rad("))
btn_rad.grid(column=3, row=2, sticky=E+W, ipady=5)

btn_fac = Button(window, text="fac", background="gray11",
                 foreground="Darkorange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda: press("fac("))
btn_fac.grid(column=0, row=3, sticky=E+W, ipady=5)

btn_power = Button(window, text="pow", background="gray11",
                   foreground="Darkorange1", font=font_value, borderwidth=1,
                   relief=SOLID, command=lambda: press("pow"))
btn_power.grid(column=1, row=3, sticky=E+W, ipady=5)

btn_remainder = Button(window, text="rem", background="gray11",
                       foreground="Darkorange1", font=font_value, borderwidth=1,
                       relief=SOLID, command=lambda: press("rem"))
btn_remainder.grid(column=2, row=3, sticky=E+W, ipady=5)

btn_pi = Button(window, text="pi", background="gray11",
                foreground="Darkorange1", font=font_value, borderwidth=1,
                relief=SOLID, command=lambda: press(3.141592))
btn_pi.grid(column=3, row=3, sticky=E+W, ipady=5)

btn_clear = Button(window, text="C", background="gray11",
                   foreground="Darkorange1", font=font_value, borderwidth=1,
                   relief=SOLID, command=clear)
btn_clear.grid(column=0, row=4, columnspan=2, sticky=E+W, ipady=5)

btn_backspace = Button(window, text="B", background="gray11",
                       foreground="Darkorange1", font=font_value, borderwidth=1,
                       relief=SOLID, command=back)
btn_backspace.grid(column=2, row=4, columnspan=2, sticky=E+W, ipady=5)

btn_7 = Button(window, text="7", background="gray11",
               foreground="Darkorange1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(7))
btn_7.grid(column=0, row=5, sticky=E+W, ipady=5)

btn_8 = Button(window, text="8", background="gray11",
               foreground="Darkorange1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(8))
btn_8.grid(column=1, row=5, sticky=E+W, ipady=5)

btn_9 = Button(window, text="9", background="gray11",
               foreground="Darkorange1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(9))
btn_9.grid(column=2, row=5, sticky=E+W, ipady=5)

btn_div = Button(window, text="÷", background="gray5",
                 foreground="Darkorange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda: press("÷"))
btn_div.grid(column=3, row=5, sticky=E+W, ipady=5)

btn_4 = Button(window, text="4", background="gray11",
               foreground="Darkorange1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(4))
btn_4.grid(column=0, row=6, sticky=E+W, ipady=5)

btn_5 = Button(window, text="5", background="gray11",
               foreground="Darkorange1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(5))
btn_5.grid(column=1, row=6, sticky=E+W, ipady=5)

btn_6 = Button(window, text="6", background="gray11",
               foreground="Darkorange1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(6))
btn_6.grid(column=2, row=6, sticky=E+W, ipady=5)

btn_mul = Button(window, text="×", background="gray5",
                 foreground="Darkorange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda: press("×"))
btn_mul.grid(column=3, row=6, sticky=E+W, ipady=5)

btn_1 = Button(window, text="1", background="gray11",
               foreground="Darkorange1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(1))
btn_1.grid(column=0, row=7, sticky=E+W, ipady=5)

btn_2 = Button(window, text="2", background="gray11",
               foreground="Darkorange1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(2))
btn_2.grid(column=1, row=7, sticky=E+W, ipady=5)

btn_3 = Button(window, text="3", background="gray11",
               foreground="Darkorange1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(3))
btn_3.grid(column=2, row=7, sticky=E+W, ipady=5)

btn_sub = Button(window, text="-", background="gray5",
                 foreground="Darkorange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda: press("-"))
btn_sub.grid(column=3, row=7, sticky=E+W, ipady=5)

btn_0 = Button(window, text="0", background="gray11",
               foreground="Darkorange1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(0))
btn_0.grid(column=0, row=8, columnspan=2, sticky=E+W, ipady=5)

btn_dot = Button(window, text=".", background="gray5",
                 foreground="Darkorange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda: press("."))
btn_dot.grid(column=2, row=8, sticky=E+W, ipady=5)

btn_add = Button(window, text="+", background="gray5",
                 foreground="Darkorange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda: press("+"))
btn_add.grid(column=3, row=8, sticky=E+W, ipady=5)

btn_equal = Button(window, text="=", background="gray11",
                   foreground="Darkorange1", font=font_value, borderwidth=1,
                   relief=SOLID, command=equal)
btn_equal.grid(column=0, row=9, columnspan=4, sticky=E+W, ipady=5)

btn_close = Button(window, text="close", background="gray5",
                 foreground="Darkorange1", font=font_value, borderwidth=1,
                 relief = SOLID, command=close)
btn_close.grid(column=3, row=9, sticky=E+W, ipady=5)

window.mainloop()
