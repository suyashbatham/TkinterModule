from tkinter import *

top = Tk()
top.geometry("300x400")
s = Scale(top)
s.pack()

#spinbobxx
sb = Spinbox(top,from_ = 0,to=10)
sb.pack()

#scrollbar
scrollbar = Scrollbar(top)
scrollbar.pack(side=RIGHT,fill=Y)
list = Listbox(top,yscrollcommand=scrollbar.set)
for line in range(100):
    list.insert(END,'This is a line no is'+str(line))
list.pack(side=LEFT,fill=BOTH)

top.mainloop()