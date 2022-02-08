from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox
from bookAdd import *
from bookDelete import *
from displayBook import *
from bookIssue import *
from bookReturn import * 
from displayIssues import *
from overDateIssues import * 
from displayStudentIssue import *
from issueStudentBook import * 
from registerStudent import * 
import pyodbc



def adminSystem():
    cnxn = pyodbc.connect(r'Driver=SQL Server;Server=.\SQLEXPRESS;Database=db;Trusted_Connection=yes;')
    cursor = cnxn.cursor()


    root = Tk()
    root.title("Library Management System")
    root.minsize(width=300,height=200)
    root.geometry("1080x720")




    background_image = Image.open("libraryfoto.jpg")
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)

    Canvas1.create_image(400,240,image = img)      
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=1)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.2)

    headingLabel = Label(headingFrame1, text="Welcome to \n Library Management System", bg='black', fg='white', font=('Courier',22))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command= addBook)
    btn1.place(relx=0.16,rely=0.39, relwidth=0.35,relheight=0.1)

    btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
    btn2.place(relx=0.16,rely=0.59, relwidth=0.35,relheight=0.1)
        
    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
    btn3.place(relx=0.50,rely=0.39, relwidth=0.35,relheight=0.1)

    btn3 = Button(root,text="View All Issues ",bg='black', fg='white', command=ViewIssues)
    btn3.place(relx=0.16,rely=0.49, relwidth=0.35,relheight=0.1)

    btn3 = Button(root,text="View Overdate Issues ",bg='black', fg='white', command= ViewOverDateIssues)
    btn3.place(relx=0.50,rely=0.49, relwidth=0.35,relheight=0.1)
        
    btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
    btn4.place(relx=0.16,rely=0.69, relwidth=0.35,relheight=0.1)
        
    btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
    btn5.place(relx=0.50,rely=0.59, relwidth=0.35,relheight=0.1)

    btn6 = Button(root,text="Register new Student",bg='black', fg='white', command = registerStudent)
    btn6.place(relx=0.50,rely=0.69, relwidth=0.35,relheight=0.1)



    root.mainloop()
    root.destroy()

def userSystem(student_number):
    



    root = Tk()
    root.title("Library Management System")
    root.minsize(width=300,height=200)
    root.geometry("1080x720")




    background_image = Image.open("libraryfoto.jpg")

    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)

    Canvas1.create_image(400,240,image = img)      
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=1)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.2)

    headingLabel = Label(headingFrame1, text="Welcome to \n Library Student System", bg='black', fg='white', font=('Courier',22))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        
   
        
    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
    btn3.place(relx=0.28,rely=0.34, relwidth=0.45,relheight=0.1)

    btn3 = Button(root,text="View My Book Issues ",bg='black', fg='white', command=lambda: viewStudentIssues(student_number))
    btn3.place(relx=0.28,rely=0.44, relwidth=0.45,relheight=0.1)

    btn3 = Button(root,text="Issue a Book ",bg='black', fg='white', command= lambda: issueStudentBook(student_number))
    btn3.place(relx=0.28,rely=0.54, relwidth=0.45,relheight=0.1)
        
    btn4 = Button(root,text="Return My Book",bg='black', fg='white', command = returnBook)
    btn4.place(relx=0.28,rely=0.64, relwidth=0.45,relheight=0.1)



    root.mainloop()
    root.destroy()
