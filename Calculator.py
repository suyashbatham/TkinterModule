# the area in which we write something is called text and introdunction and other option are called label.

from tkinter import *
from functools import partial
top = Tk()
def sum(label,x1,x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum = int(n1) + int(n2)
    label.config(text='sum is : %d',%sum)
    return

top.geometry("400x400")
l1 = Label(top,text="First Number")
l1.grid(row=1,column=0)
l2 = Label(top,text="Second number")
l2.grid(row=2,column=0)
label = Label(top,text="sum")
label.grid(row=6,column=2)

x1 = StringVar()
x2 = StringVar()
e1 = Entry(top,textvariable=x1)
e1.grid(row=1,column=2)
e2 = Entry(top,textvariable=x2)
e2.grid(row=2,column=2)

sum = partial(sum,label,x1,x2)

button = Button(top,text="Calculater",command=sum)
button.grid(row=3,column=0)
# l = Label(top,text="user name")
# l.pack(side=LEFT)
# e = Entry(top)
# e.pack(side=RIGHT)
# t = Text(top)
# t.insert(INSERT,"HELLO")
# t.pack()
top.mainloop()