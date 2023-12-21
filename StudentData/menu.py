from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root=Tk()
root.geometry("800x500")
menu=Menu(root)
root.config(menu=menu)

def cmd():
    file_path=filedialog.askopenfilename(initialdir="D:\\PyCharm\\StudentData",title="Open File",
                                         filetypes=(("text files","*.txt"),("all files","*.*")))
    file=open(file_path,'r')
    print(file.read())
    file.close()

def save():
    file=filedialog.asksaveasfile(initialdir="D:\\PyCharm\\StudentData",defaultextension=".txt", filetypes=[
        ("Text Files",".txt"),
        ("HTML Files", ".html"),
        ("All Files", ".*")
                                            ])
    filetext=text.get(1.0,END)
    file.write(filetext)
    file.close()



file_menu=Menu(menu)
menu.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="Open",command=cmd)
file_menu.add_command(label="Save",command=save)


text=Text(root)
text.pack()





root.mainloop()
