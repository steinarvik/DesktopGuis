import tkinter as tk
from tkinter import ttk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

style = ttk.Style()
style.theme_use('clam')  # You can change 'clam' to other themes like 'vista', 'xpnative', etc.

entry = tk.Entry(root, font=('Helvetica', 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, column) in buttons:
    if text == '=':
        button = ttk.Button(root, text=text, command=calculate)
    else:
        button = ttk.Button(root, text=text, command=lambda t=text: button_click(t))
    button.grid(row=row, column=column, padx=5, pady=5, sticky="ew")

clear_button = ttk.Button(root, text="C", command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

root.mainloop()