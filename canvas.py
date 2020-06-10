from tkinter import *

top = Tk()
top.geometry("200x200")
c = Canvas(top,height=250,width=300,bg='blue')
coordinate = 10,50,240,210
arc = c.create_arc(coordinate,start=90,extent=180,fill='yellow')   # start and extent in angle
line = c.create_line(10,10,200,200,fill='yellow')
c.pack()
top.mainloop()