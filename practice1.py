import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("No of projects Done")
root.geometry("300x150")


def show():
    number = int(entry.get())
    number = number + 2
    messagebox.showinfo("entered no is",f"your no :{number}")            

label = tk.Label(root,text="Enter no:")
label.pack(anchor="center")

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Display no",command=show)
button.pack(pady=10)


root.mainloop()