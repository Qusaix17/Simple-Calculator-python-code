from tkinter import *

# main tkinter
root = Tk()
root.title("Calculator")
root.geometry("350x400")

# display for the calculator
display = Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4)

# classes and methods
class Calculator:
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def times(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error"
        return a / b

#instance of cal
calc = Calculator()

# Global variables
first_num = None
operation = None

# button functions
def button_click(value):
    current = display.get()
    display.delete(0, END)
    display.insert(END, current + str(value))

def clear_display():
    display.delete(0, END)

def set_operation(op):
    global first_num, operation
    try:
        first_num = float(display.get())
        operation = op
        display.delete(0, END)
    except ValueError:
        display.delete(0, END)
        display.insert(END, "Error")

def calculate():
    global first_num, operation
    try:
        second_num = float(display.get())
        display.delete(0, END)
        if operation == 'add':
            display.insert(END, calc.add(first_num, second_num))
        elif operation == 'minus':
            display.insert(END, calc.minus(first_num, second_num))
        elif operation == 'times':
            display.insert(END, calc.times(first_num, second_num))
        elif operation == 'divide':
            display.insert(END, calc.divide(first_num, second_num))
    except ValueError:
        display.delete(0, END)
        display.insert(END, "Error")

# Define buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('/', 4, 3)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == 'C':
        tk_button = Button(root, text=text, width=5, height=2, command=clear_display)
    elif text == '+':
        tk_button = Button(root, text=text, width=5, height=2, command=lambda: set_operation('add'))
    elif text == '-':
        tk_button = Button(root, text=text, width=5, height=2, command=lambda: set_operation('minus'))
    elif text == '*':
        tk_button = Button(root, text=text, width=5, height=2, command=lambda: set_operation('times'))
    elif text == '/':
        tk_button = Button(root, text=text, width=5, height=2, command=lambda: set_operation('divide'))
    else:
        tk_button = Button(root, text=text, width=5, height=2, command=lambda t=text: button_click(t))
    tk_button.grid(row=row, column=col)

# Equals button to trigger the calculation
equals_button = Button(root, text='=', width=22, height=2, command=calculate)
equals_button.grid(row=5, column=0, columnspan=4)

# Start the Tkinter event loop
root.mainloop()
