from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry = Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click_button(value):
    entry.insert(END, value)

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        b = Button(root, text=button, width=5, height=2, font=('Arial', 18), command=calculate)
    else:
        b = Button(root, text=button, width=5, height=2, font=('Arial', 18), command=lambda b=button: click_button(b))
    b.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

clear_btn = Button(root, text='C', width=21, height=2, font=('Arial', 18), command=clear)
clear_btn.grid(row=row_val, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
