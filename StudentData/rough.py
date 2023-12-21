import tkinter.ttk
from tkinter import *
import mysql.connector
from PIL import Image
from tkinter import messagebox

con=mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="student")
cursor=con.cursor()
root=Tk()
root.geometry("420x400+100+50")
root.title("Sign-In")
root.resizable(False,False)

img=PhotoImage(file='Images/logo.png')
Label(image=img).place(x=70,y=0)

l=Label(text="Enter Your Mail Id:")
lb=Entry()
l.place(x=30,y=210)
lb.place(x=180,y=210)

p=Label(text="Enter Your Password:")
pb=Entry()
p.place(x=30,y=250)
pb.place(x=180,y=250)



def register():

    messagebox.showinfo(title="Log-in",message="Success to Login !")
    reg = Toplevel(root)
    reg.geometry("400x300+100+80")
    reg.resizable(False, False)
    reg.configure(bg="#D3D3D3")


    def addRec():

        addPage=Toplevel(reg)
        addPage.title("Add Record")
        addPage.geometry("1000x600+30+10")

        menuBar = Menu(addPage)
        addPage.config(menu=menuBar)
        file_menu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_separator()
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=quit)

        edit_menu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Paste")
        edit_menu.add_separator()
        edit_menu.add_command(label="Delete")



        l1 = Label(addPage,text="Enter The Student Name:", )
        lb1 = Entry(addPage,width=30)
        l1.place(x=50, y=90)
        lb1.place(x=240, y=90)

        l2 = Label(addPage,text="Enter The Student Department:")
        lb2 = Entry(addPage,width=30)
        l2.place(x=50, y=130)
        lb2.place(x=240, y=130)

        l3 = Label(addPage,text="Enter The Student Mob.No:")
        lb3 = Entry(addPage,width=30)
        l3.place(x=50, y=170)
        lb3.place(x=240, y=170)

        ins = Button(addPage,text="Add Record")
        ins.configure(bg="#D3D3D3")
        res = Button(addPage,text="Reset")
        res.configure(width=9, bg="#D3D3D3")
        exi = Button(addPage,text="Exit")
        exi.configure(width=9, bg="#D3D3D3")


        addPage.mainloop()






    b1 = Button(reg,text="Add New Record",command=addRec)
    b2 = Button(reg, text="Remove Record")
    b3 = Button(reg, text="Update Record")
    b4 = Button(reg, text="Fetch All Records")
    b5 = Button(reg, text="Back")

    b1.configure(bg="#D3D3D3",border=1,cursor="hand2")
    b2.configure(bg="#D3D3D3",border=1,cursor="hand2")
    b3.configure(bg="#D3D3D3",border=1,cursor="hand2")
    b4.configure(bg="#D3D3D3",border=1,cursor="hand2")
    b5.configure(bg="white",border=0,cursor="hand2")

    b1.place(x=150,y=50)
    b2.place(x=150,y=100)
    b3.place(x=150,y=150)
    b4.place(x=150,y=200)
    b5.place(x=340,y=250)



    reg.mainloop()


bt=Button(text="Log-In",command=register)
bt.configure(width=10)
bt.place(x=280,y=290)

def signup():
    signup=Toplevel(root)
    signup.title("Sign-Up")
    signup.geometry("500x600+100+50")
    signup.configure(bg="white")
    signup.resizable(False, False)
    l1 = Label(signup,text="Enter First Your Name : ",bg="white",font=("Nunito",12))
    l2 = Label(signup,text="Enter Last Your Name : ",bg="white",font=("Nunito",12))
    l3 = Label(signup,text="Enter Your Mobile Number : ",bg="white",font=("Nunito",12))
    l4 = Label(signup,text="Enter Your E-Mail Id : ",bg="white",font=("Nunito",12))
    l5 = Label(signup,text="Create Your Password : ",bg="white",font=("Nunito",12))
    l6 = Label(signup,text="Confirm Your Password : ",bg="white",font=("Nunito",12))


    lb1 = Entry(signup,width=25,bg="#D6D6D6",fg="black",font=(15))
    lb2 = Entry(signup,width=25,bg="#D6D6D6",fg="black",font=(15))
    lb3 = Entry(signup,width=25,bg="#D6D6D6",fg="black",font=(15))
    lb4 = Entry(signup,width=25,bg="#D6D6D6",fg="black",font=(15))
    lb5 = Entry(signup,width=25,bg="#D6D6D6",fg="black",font=(15))
    lb6 = Entry(signup,width=25,bg="#D6D6D6",fg="black",font=(15))

    bt1=Button(signup,text="Create",bg="#ADD8E6")
    bt1.configure(width=10,font=(10,))
    bt1.place(x=365,y=410)

    pic=PhotoImage(file='Images/logo2.png')
    Label(signup,image=pic,bg="white").place(x=145,y=460)

    l1.place(x=30,y=50)
    lb1.place(x=240,y=50)

    l2.place(x=30,y=110)
    lb2.place(x=240,y=110)

    l3.place(x=30,y=170)
    lb3.place(x=240,y=170)

    l4.place(x=30,y=230)
    lb4.place(x=240,y=230)

    l5.place(x=30,y=290)
    lb5.place(x=240,y=290)

    l6.place(x=30,y=350)
    lb6.place(x=240,y=350)


    signup.mainloop()



l1=Label(text="Don't Have register ?")
bt5=Button(text="Click Here",command=signup)
bt5.configure(border=0,cursor="hand2",fg="red")
l1.place(x=200,y=340)
bt5.place(x=315,y=340)


root.mainloop()