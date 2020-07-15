import tkinter as tk
from tkinter import *
import math
root = tk.Tk()

root.title('Simple Calculator')

e = tk.Entry(root, width=30, borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    global math
    global f_num
    global sqart
    if math == 'addition':
        e.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        e.insert(0, f_num * int(second_number))
    if math == 'division':
        e.insert(0, f_num / int(second_number))

    if math == 'power':
        e.insert(0, pow(f_num, int(second_number)))

    if math == 'square':
        e.insert(0, pow(f_num, 0.5))

    if math == 'fact':
        num = 1
        for i in range(1, f_num+1):
            num = num*i
        return e.insert(0, num)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)


def button_power():
    first_number = e.get()
    global f_num
    global math
    math = 'power'
    f_num = int(first_number)
    e.delete(0, END)


def button_square():
    first_number = e.get()
    global f_num
    global math
    math = 'square'
    f_num = int(first_number)
    e.delete(0, END)


def button_fact():
    first_number = e.get()
    global f_num
    global math
    math = 'fact'
    f_num = int(first_number)
    e.delete(0, END)


Button_1 = tk.Button(root, padx=40, pady=20, text="1",
                     command=lambda: button_click(1))
Button_2 = tk.Button(root, padx=40, pady=20, text="2",
                     command=lambda: button_click(2))
Button_3 = tk.Button(root, padx=40, pady=20, text="3",
                     command=lambda: button_click(3))
Button_4 = tk.Button(root, padx=40, pady=20, text="4",
                     command=lambda: button_click(4))
Button_5 = tk.Button(root, padx=40, pady=20, text="5",
                     command=lambda: button_click(5))
Button_6 = tk.Button(root, padx=40, pady=20, text="6",
                     command=lambda: button_click(6))
Button_7 = tk.Button(root, padx=40, pady=20, text="7",
                     command=lambda: button_click(7))
Button_8 = tk.Button(root, padx=40, pady=20, text="8",
                     command=lambda: button_click(8))
Button_9 = tk.Button(root, padx=40, pady=20, text="9",
                     command=lambda: button_click(9))
Button_0 = tk.Button(root, padx=40, pady=20, text="0",
                     command=lambda: button_click(0))

Button_clear = tk.Button(root, padx=81, pady=20,
                         text="clear", command=button_clear)
Button_equal = tk.Button(root, padx=91, pady=20,
                         text="=", command=button_equal)

Button_power = tk.Button(root, padx=37, pady=20,
                         text="^", command=button_power)

Button_square = tk.Button(root, padx=39, pady=20,
                          text="√", command=button_square)

Button_fact = tk.Button(root, padx=36, pady=20,
                        text="x!", command=button_fact)

Button_add = tk.Button(root, padx=40, pady=20, text="+", command=button_add)
Button_sub = tk.Button(root, padx=40, pady=20, text="-", command=button_sub)
Button_mul = tk.Button(root, padx=40, pady=20, text="*", command=button_mul)
Button_div = tk.Button(root, padx=40, pady=20, text="/", command=button_div)


Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

Button_0.grid(row=4, column=0)
Button_add.grid(row=5, column=0)
Button_clear.grid(row=4, column=1, columnspan=2)
Button_equal.grid(row=5, column=1, columnspan=2)

Button_sub.grid(row=6, column=0)
Button_mul.grid(row=6, column=1)
Button_div.grid(row=6, column=2)

Button_power.grid(row=7, column=0)
Button_square.grid(row=7, column=1)
Button_fact.grid(row=7, column=2)


root.mainloop()
