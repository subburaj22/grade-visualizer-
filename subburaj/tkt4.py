import tkinter as tk


root=tk.Tk()
root.geometry('400x200+100+200')

number1=tk.StringVar()
number2=tk.StringVar()



def copy():

    a=number1.get()
    number2.set(a)



labelNum1=tk.Label(root,text="First").grid(row=1,column=1)

entryNum1=tk.Entry(root,textvariable=number1).grid(row=1,column=2)

button=tk.Button(root,text="Copy",command=copy).grid(row=3,column=2)

labelNum2=tk.Label(root,text="Second").grid(row=5,column=0)

entryNum2=tk.Entry(root,textvariable=number2).grid(row=5,column=2)

root.mainloop()