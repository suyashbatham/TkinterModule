# in check button you can tick more than one option but in radio button only one option is tick.

from tkinter import *

top = Tk()
top.geometry("300x300")
c1 = IntVar()
c2 = IntVar()
cb = Checkbutton(top,text='java',offvalue=0,onvalue=1,height=5,width=10,variable=c1)
cb.pack()
cb1 = Checkbutton(top,text='python',offvalue=0,onvalue=1,height=5,width=10,variable=c2)
cb1.pack()

var = IntVar()
r1 = Radiobutton(top,text='option1',variable=var,value=1)
r1.pack()
r2 = Radiobutton(top,text='option2',variable=var,value=2)
r2.pack()
r3 = Radiobutton(top,text='option3',variable=var,value=3)
r3.pack()
top.mainloop()
