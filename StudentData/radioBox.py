from tkinter import *
from tkinter import messagebox
import mysql.connector


root=Tk()
root.geometry("600x300")

def submit():
    pass

def reset():
    pass



c=IntVar()



bt1=Radiobutton(text="Right Hand Batsman",variable=c)
bt2=Radiobutton(text="left Hand Batsman",variable=c)


submit=Button(text="Submit",bg="green",fg="white",pady=10,padx=5,command=submit)
submit.configure(height=10,width=20)
submit.pack()

reset=Button(text="Submit",bg="green",fg="white",pady=10,padx=5,command=reset)
reset.configure(height=10,width=20)
reset.pack()


bt1.pack()
bt2.pack()




root.mainloop()