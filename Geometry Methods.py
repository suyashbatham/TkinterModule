from tkinter import *
import tkinter

top = Tk()
top.geometry("200x200")

# making 36 buttons
# b = 0
# for i in range(6):
#     for j in range(6):
#         b = b + 1
#         Button(top,text=str(b),borderwidth=1).grid(row=i,column=j)

l1 = Label(top,text="maths")
l1.place(x=10,y=10)
e1 = Entry(top,bd=5)
e1.place(x=60,y=10)

l2 = Label(top,text="english")
l2.place(x=10,y=60)
e2 = Entry(top,bd=5)
e2.place(x=60,y=60)

b = Button(top,text="Submit")
b.place(x=100,y=100)
top.mainloop()