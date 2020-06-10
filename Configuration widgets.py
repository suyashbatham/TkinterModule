from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("400x400")

frame = Frame(top)
frame.pack()
frame1 = Frame(top)
frame1.pack(side=BOTTOM)

rb = Button(frame,text='Red',fg='red')
rb.pack(side=LEFT)
rb1 = Button(frame1,text='Yellow',fg='green')
rb1.pack(side=RIGHT)


lb = Listbox(top)
lb.insert(1,'python')
lb.insert(2,'C')
lb.insert(3,'C++')
lb.insert(4,'Java')
lb.pack()

# multiple windows
top.title('Suyash Batham')
top1 = Toplevel()
top1.title("Suyash")

# message box
def hello():
    messagebox.showinfo('from computer','hey there')
b = Button(top,text="popup",command=hello)
b.pack()


top.mainloop()