import tkinter.ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector


con=mysql.connector.connect(host="localhost",user="root",password="",port="3306",database="student")
cursor = con.cursor()


root=Tk()
root.geometry("500x450")
root.title("Student Record")
root.resizable(False,False)
root.configure(bg="#D3D3D3")
id=Label(text="Student ID:")
idb=Entry(width=30)
id.place(x=50,y=50)
idb.place(x=240,y=50)
id.configure(bg="#D3D3D3")



l1=Label(text="Enter The Student Name:",)
lb1=Entry(width=30)
l1.place(x=50,y=90)
lb1.place(x=240,y=90)
l1.configure(bg="#D3D3D3")

l2=Label(text="Enter The Student Department:")
lb2=Entry(width=30)
l2.place(x=50,y=130)
lb2.place(x=240,y=130)
l2.configure(bg="#D3D3D3")


l3=Label(text="Enter The Student Mob.No:")
lb3=Entry(width=30)
l3.place(x=50,y=170)
lb3.place(x=240,y=170)
l3.configure(bg="#D3D3D3")


def add():
    q="insert into std1(id,name,dept,mno)values(%s,%s,%s,%s)"
    data=(idb.get(),lb1.get(),lb2.get(),lb3.get())
    cursor.execute(q,data)
    con.commit()
    messagebox.showinfo(title="Record",message="Record Insert Successful")

def reset():
    idb.delete(0,END)
    lb1.delete(0,END)
    lb2.delete(0,END)
    lb3.delete(0,END)

def close():
    exit(0)

def fetch():

    fet=Toplevel(root)
    fet.resizable(False,False)
    fet.geometry("800x400")
    fet.configure(bg="#D3D3D3")
    q="select * from std1"
    cursor.execute(q)
    rec=cursor.fetchall()
    #for row in rec:
        #print(row[0],"",row[1],"",row[2],"",row[3])

    tree=tkinter.ttk.Treeview(fet)
    tree['columns']=["name","dept","mno","idcode",]
    tree.column("name", width=130,anchor=CENTER)
    tree.column("dept", width=150,anchor=CENTER)
    tree.column("mno", width=100,anchor=CENTER)
    tree.column("idcode", width=50, anchor=CENTER)

    tree['show']='headings'

    tree.heading("name",text="S-NAME", anchor=tkinter.CENTER)
    tree.heading("dept", text="S-DEPT", anchor=tkinter.CENTER)
    tree.heading("mno", text="S-Mob NO", anchor=tkinter.CENTER)
    tree.heading("idcode", text="S-ID", anchor=tkinter.CENTER)


    i=0
    for row in rec:
        tree.insert('',i,text="",values=(row[0],row[1],row[2],row[3]))
        i=i+1
    tree.place(x=10,y=10)


ins=Button(text="Add Record",command=add)
ins.configure(bg="#D3D3D3")
res=Button(text="Reset",command=reset)
res.configure(width=9,bg="#D3D3D3")
exi=Button(text="Exit",command=close)
exi.configure(width=9,bg="#D3D3D3")
fetc=Button(text="Fetch Existing Data",command=fetch)
fetc.configure(bg="#D3D3D3")

ins.place(x=340,y=240)
res.place(x=340,y=280)
exi.place(x=340,y=320)
fetc.place(x=20,y=360)




root.mainloop()