from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import mysql.connector
import helper

conn = mysql.connector.connect(**helper.db_config)
print("DATABASE CONNECTION SUCCESSFUL")



#Class for DOCTOR REGISTRATION 
class Doctors:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg=helper.bg)
        self.frame = Frame(self.master,bg=helper.bg)
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.doc_ID=StringVar()
        self.doc_name=StringVar()
        self.doc_gender=StringVar()
        self.doc_age=IntVar()
        self.doc_type=StringVar()
        self.doc_salary=IntVar()
        self.doc_exp=StringVar()
        self.doc_email=StringVar()
        self.doc_phno=StringVar()


        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "DOCTOR REGISTRATION FORM", font="Helvetica 20 bold",bg=helper.bg)
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,bg=helper.bg,bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,bg=helper.bg,bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblempid = Label(self.LoginFrame,text="DOCTOR ID",font="Helvetica 14 bold",bg=helper.bg,bd=22)
        self.lblempid.grid(row=0,column=0)
        self.lblempid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_ID)
        self.lblempid.grid(row=0,column=1)
        
        self.lblempname = Label(self.LoginFrame,text="DOCTOR NAME",font="Helvetica 14 bold",bg=helper.bg,bd=22)
        self.lblempname.grid(row=1,column=0)
        self.lblempname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_name)
        self.lblempname.grid(row=1,column=1)

        self.lblgender = Label(self.LoginFrame,text="GENDER",font="Helvetica 14 bold",bg=helper.bg,bd=22)
        self.lblgender.grid(row=2,column=0)
        self.etype1 =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_gender)
        self.etype1.grid(row=2,column=1)
        

        self.lblage = Label(self.LoginFrame,text="AGE",font="Helvetica 14 bold",bg=helper.bg,bd=22)
        self.lblage.grid(row=3,column=0)
        self.lblage  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_age)
        self.lblage.grid(row=3,column=1)
        
        self.etype1=Label(self.LoginFrame,text="DOCTOR DESIGNATION",font="Helvetica 14 bold",bg=helper.bg,bd=22)
        self.etype1.grid(row=4,column=0)
        self.etype1 =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_type)
        self.etype1.grid(row=4,column=1)

        self.lblCon = Label(self.LoginFrame,text="SALARY",font="Helvetica 14 bold",bg=helper.bg,bd=22)
        self.lblCon.grid(row=0,column=2)
        self.lblCon  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_salary)
        self.lblCon.grid(row=0,column=3)
        
        self.lblAlt = Label(self.LoginFrame,text="EXPERIENCE",font="Helvetica 14 bold",bg=helper.bg,bd=22)
        self.lblAlt.grid(row=1,column=2)
        self.lblAlt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_exp)
        self.lblAlt.grid(row=1,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg=helper.bg,bd=22)
        self.lbleid.grid(row=2,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_phno)
        self.lbleid.grid(row=2,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg=helper.bg,bd=22)
        self.lbleid.grid(row=3,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.doc_email)
        self.lbleid.grid(row=3,column=3)

        self.button2 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg=helper.bg,command = self.INSERT_DOC)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg=helper.bg,command= self.DE_DISPLAY)
        self.button3.grid(row=3,column=2)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg=helper.bg,command = self.Exit)
        self.button6.grid(row=3,column=3)
        

   #FUNCTION TO EXIT PATIENT FORM
    def Exit(self):            
        self.master.destroy()
        
    #FUNCTION TO INSERT DATA IN DOCTOR FORM
        
    def INSERT_DOC(self):
        global conn, e1,e2,e3,e4,e5,e6,e7,e8,e9,var
        e1=(self.doc_ID.get())
        e2=(self.doc_name.get())
        e3=(self.doc_gender.get())
        e4=(self.doc_age.get())
        e5=(self.doc_type.get())
        e6=(self.doc_salary.get())
        e7=(self.doc_exp.get())
        e8=(self.doc_email.get())
        e9=(self.doc_phno.get())
        cursor = conn.cursor()  
          # Use database
        cursor.execute("USE hms")  
        cursor.execute("SELECT * FROM DOCTOR WHERE doc_ID = %s", (e1,))
        result = cursor.fetchone()
        
        if  result is not None:
             tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "DOCTOR ID ALREADY EXISTS")     
        else:
            cursor.execute("INSERT INTO doctors VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DOCTOR DATA ADDED")
        conn.commit()
                
    #FUNCTION TO OPEN DELETE PATIENT DISPLAY WINDOW
    def DE_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = D_DOC(self.newWindow)


#CLASS FOR DISPLAY MENU FOR DELETE DOCTOR
class D_DOC:
    def __init__(self,master):    
        global de1_DOC,de
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg=helper.bg)
        self.frame = Frame(self.master,bg=helper.bg)
        self.frame.pack()
        self.de1_DOC=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE DOCTOR WINDOW", font="Helvetica 20 bold",bg=helper.bg)
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,bg=helper.bg,bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,bg=helper.bg,bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER DOCTOR ID TO DELETE",font="Helvetica 14 bold",bg=helper.bg,bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_DOC)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg=helper.bg,command = self.DELETE_DOC)
        self.DeleteB.grid(row=3,column=1)
        
    #FUNCTION TO DELETE DATA IN DOCTOR FORM 
    def DELETE_DOC(self):        
        global conn, inp_d
        de = str(self.de1_DOC.get())
        cursor = conn.cursor() 
        # Use database
        cursor.execute("USE hms") 
        cursor.execute("select * from doctors where doc_ID=%s", (de,))
        result = cursor.fetchone()
        if  result is not None:
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
            cursor.execute("DELETE from doctors where doc_ID=%s", (de,))
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
            dme = tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DOCTOR DATA DELETED")
            
        else:
            error = tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "DOCTOR DATA DOESN'T EXIST")
        conn.commit()   
