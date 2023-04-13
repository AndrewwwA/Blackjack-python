import tkinter as tk
import math

root = tk.Tk()
root.title("Flexbox-like container in Tkinter")

def create_flex_container(parent, widget_count):
    parent.grid_rowconfigure(0, weight=1)
    for column in range(widget_count):
        parent.grid_columnconfigure(column, weight=1)

    return widget_count


widget_count = 8  # Adjust this value to change the number of cards
container = tk.Frame(root)
columns = create_flex_container(container, widget_count)
container.pack(fill=tk.BOTH, expand=True)

for i in range(widget_count):
    button = tk.Button(container, text=f"Button {i + 1}")
    button.grid(row=0, column=i, sticky=tk.NSEW)




root.mainloop()
