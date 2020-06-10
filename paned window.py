from tkinter import *

import button

top = Tk()
top.geometry("100x100")

pw = PanedWindow()
pw.pack(fill=BOTH,expand=1)

left = Entry(top,bd=5)
pw.add(left)

pw2 = PanedWindow(pw,orient=VERTICAL)
pw.add(pw2)

top = Scale(pw2,orient=HORIZONTAL)
pw2.add(top)

botton = Button(pw2,text="ok")
pw2.add(button)

top.mainloop()