from tkinter import *

top = Tk()
top.geometry("400x400")
# Make a button
def pr():
    print('hi')
button = Button(top,text='Hello',command=pr,padx=20,pady=50,activeforeground='red')  # command = print('hi')  # padx = adding the boundry outside the text
button.place(x=100,y=100)
# button.grid(row=1,column=1)
# button.pack()
# button1 = Button(top,text='Hi')
# button1.place(x=300,y=302)
# button1.grid(row=2,column=1)
# button1.pack()
top.mainloop()