from tkinter import *

top = Tk()

top.geometry("200x100")

from tkinter import messagebox
def fun():
    messagebox.showinfo("Hello", "subburaj")


b1 = Button(top, text="click me", command=fun, activeforeground="red", activebackground="pink", pady=10)


b1.pack()
top.mainloop()
