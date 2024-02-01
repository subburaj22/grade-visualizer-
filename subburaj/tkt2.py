from tkinter import *

top = Tk()

top.geometry("500x500")

# creating a simple canvas
c = Canvas(top, bg="yellow", height="200", width=200)

arc = c.create_arc((5, 10, 150, 200), start=0, extent=150, fill="blue")

c.pack()

top.mainloop()