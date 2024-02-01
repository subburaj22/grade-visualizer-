import tkinter as tk


root=tk.Tk()
root.geometry('800x500')

number1=tk.StringVar()
number2=tk.StringVar()
number3=tk.StringVar()

def copy():

    a=number1.get()
    b=number2.get()
    c=int(a)+int(b)
    number3.set(c)
def copy2():

    a=number1.get()
    b=number2.get()
    c=int(a)-int(b)
    number3.set(c)

def copy3():

    a=number1.get()
    b=number2.get()
    c=int(a)*int(b)
    number3.set(c)
def copy4():

    a=number1.get()
    b=number2.get()
    c=int(a)/int(b)
    number3.set(c)

labelNum1=tk.Label(root,text="First Number").place(x=100,y=100)
entryNum1=tk.Entry(root,textvariable=number1).place(x=250,y=100)
labelNum2=tk.Label(root,text="Second Mumber").place(x=100,y=150)
entryNum2=tk.Entry(root,textvariable=number2).place(x=250,y=150)
button=tk.Button(root,text="Add",command=copy).place(x=100,y=250)
button=tk.Button(root,text="sub",command=copy2).place(x=200,y=250)
button=tk.Button(root,text="multi",command=copy3).place(x=300,y=250)
button=tk.Button(root,text="divi",command=copy4).place(x=400,y=250)


entryNum3=tk.Entry(root,textvariable=number3).place(x=250,y=300)



root.mainloop()