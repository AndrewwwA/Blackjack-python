import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Getting and setting')
window.geometry('600x500')

text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text='Click me')
btn.pack()

text.bind('<Shift-MouseWheel>', lambda event: print('mousewheel'))

window.mainloop()