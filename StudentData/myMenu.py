from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
root = Tk()
root.title("Menu Bar")
root.geometry("800x500")

def new():
    messagebox.showinfo(title="New Window",message="Go to the Next New Page")
    new=Toplevel(root)
    new.geometry("800x500")
    menuBar = Menu(new)
    new.config(menu=menuBar)
    file_menu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Open folder")
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Exit")
    text = Text(new)
    text.configure(width=1000, height=700, padx=10, pady=10)
    text.pack()
    new.mainloop()


def open():
    file=filedialog.askopenfilename(initialdir="D:\\Menu Purposes",filetypes=(("Text Files","*.txt"),("All Files","*.*")))

def save():
    file=filedialog.asksaveasfile(initialdir="D:\\Menu Purposes",filetypes=(("Text Files","*.txt"),("All Files","*.*")))


menuBar=Menu(root)
root.config(menu=menuBar)
file_menu=Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new)
file_menu.add_command(label="Open",command=open)
file_menu.add_separator()
file_menu.add_command(label="Save",command=save)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)


edit_menu=Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_separator()
edit_menu.add_command(label="Delete")


text=Text(root)
text.configure(width=1000,height=700,padx=10,pady=10)
text.pack()


root.mainloop()