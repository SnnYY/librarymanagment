from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pyodbc
from main import *

def logIn():
    
    credential = bookInfo1.get()
    credential_pass = bookInfo2.get()


    cnxn = pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-PS9QIBH\SQLEXPRESS;Database=db;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    
    checkSql = "SELECT * FROM auth WHERE id = \'"+credential+"\'"

    print(checkSql)
    cursor.execute(checkSql)

    row = cursor.fetchone()
    try:
        if row[1] == credential_pass:
            messagebox.showinfo("success","Welcome to system")
            if row[2] == "admin":
                root.destroy()
                Toplevel(adminSystem())
            else:
                root.destroy()
                Toplevel(userSystem(credential))
        else:
            messagebox.showinfo("Error","Wrong password and id")
    except:
        root.destroy()
    
    
def logInPage(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library System")
    root.minsize(width=500,height=400)
    root.geometry("1080x720")

    background_image = Image.open("libraryfoto.jpg")

    img = ImageTk.PhotoImage(background_image)

    bookTable = "books" 

    Canvas1 = Canvas(root)
    
    Canvas1.create_image(400,240,image = img)   
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Welcome to Library System", bg='black', fg='white', font=('Courier',22))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Student Number
    lb1 = Label(labelFrame,text="Login ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Password
    lb2 = Label(labelFrame,text="Password : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    
        

        
    #Submit Button
    SubmitBtn = Button(root,text="Log In",bg='#d1ccc0', fg='black',command=logIn)
    SubmitBtn.place(relx=0.28,rely=0.7, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.7, relwidth=0.18,relheight=0.08)
    root.mainloop()
    

logInPage()