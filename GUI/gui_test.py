import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter", foreground = "white", background = "black", width = 10, height = 10)
# inclues "red, orange, yellow, green, blue, purple"
# background = "34AANFE"
# foreground can be fg, background can be bg
greeting.pack()

button = tk.Button(text = "Click me!", width = 25, height = 5, bg = "blue", fg = "yellow")
button.pack()

entry = tk.Entry(fg="yellow", bg = "blue", width = 50)
# retrive with .get()
# delte with .delete() # index of number can be added (0,4) = first 4
# insert with .insert()
entry.pack()

window.mainloop()