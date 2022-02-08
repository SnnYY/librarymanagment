from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pyodbc

# Add your own database name and password here to reflect in the code

con = pyodbc.connect(r'Driver=SQL Server;Server=.\SQLEXPRESS;Database=db;Trusted_Connection=yes;')
cursor = con.cursor()
bookTable = "books"   

def View(): 
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-10s%-40s%-30s%-20s"%('Book ID','Title','Author','Status'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = "select * from books"
    try:
        cursor.execute("SELECT * FROM books")
        row = cursor.fetchone()
        while row:
            Label(labelFrame, text="%-10s%-30s%-30s%-20s"%(row[0],row[1],row[2],row[3]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
            row = cursor.fetchone()
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()