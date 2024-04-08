import tkinter as tk

def button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("My Tkinter App")

button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

root.mainloop()