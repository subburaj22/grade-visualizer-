from tkinter import *

# Create an instance of tkinter frame or widget
win = Tk()
win.geometry("500x550")

def update_text():
   # Configuring the text in Label widget
   global a
   label.configure(text="subburaj")


# Create a label widget
label=Label(win, text="")
label.pack()

# Create a button to update the text of label widget
button=Button(win, text= "click here", command=update_text)
button.pack()

win.mainloop()