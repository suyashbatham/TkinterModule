from tkinter import *

top = Tk()
top.geometry("200x250")
# menubutton = Menubutton(top, text="Language")
# menubutton.grid()
# menubutton.menu = Menu(menubutton)
# menubutton["menu"] = menubutton.menu
# menubutton.menu.add_checkbutton(label="Hindi", variable=IntVar())
# menubutton.menu.add_checkbutton(label="English", variable=IntVar())
# menubutton.pack()
# top.mainloop()


def nothing():
    file = Toplevel(top)
    button = Button(file,text="Do Nothing")
    button.pack()

menubar = Menu(top)
filemenu = Menu(menubar)
filemenu.add_command(label="New Window",command=nothing())
filemenu.add_command(label="New file",command=nothing())
filemenu.add_command(label="Open",command=nothing())
filemenu.add_separator()
filemenu.add_command(label="Close",command=nothing())
filemenu.add_command(label="Save",command=nothing())
filemenu.add_command(label="Save as",command=nothing())
filemenu.add_separator()
filemenu.add_command(label="Close Tab",command=nothing())
filemenu.add_separator()
filemenu.add_command(label="Exit",command=top.quit())
filemenu.add_separator()

menubar.add_cascade(label="File",menu=filemenu)

editmenu = Menu(menubar)
filemenu.add_command(label="Undo",command=nothing())
filemenu.add_command(label="Redo",command=nothing())
filemenu.add_command(label="Cut",command=nothing())
filemenu.add_separator()
filemenu.add_command(label="Copy",command=nothing())
filemenu.add_command(label="paste",command=nothing())
editmenu.add_command(label="Select all",command=nothing())
editmenu.add_separator()
editmenu.add_command(label="Close all",command=nothing())
editmenu.add_separator()
editmenu.add_command(label="Exit",command=top.quit())
editmenu.add_separator()

menubar.add_cascade(label="File",menu=editmenu)
top.config(menu=menubar)
top.mainloop()