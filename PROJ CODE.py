#imports
from tkinter import *
import os
from PIL import ImageTk, Image
import math


#Main screen
master = Tk()
master.title('Banking management')
master.geometry('300x400')

#import image
img1=Image.open('C:/Users/kashy/OneDrive/Desktop/BANKING MANAGEMENT/banking.jpg')
img1=img1.resize((150,150))
img1=ImageTk.PhotoImage(img1)


#label
Label(master,text="BANK MANAGER",font=('Calibri',16)).grid(row=0,sticky=N,pady=10)
Label(master,text="BANKING MADE EASY",font=('Calibri',12)).grid(row=1,sticky=N,pady=10)
Label(master,image=img1).grid(row=2,sticky=N,pady=15)
Label(master,text="DEVELOPED BY TEAM CODECRAFTERS",font=('Calibri',6)).grid(row=100,sticky=S,pady=3)

#USER REGISTRATION MODULE
def register():
    global temp_name
    global temp_age
    global temp_email
    global temp_pass
    global notif
    temp_name=StringVar()
    temp_age = StringVar()
    temp_email = StringVar()
    temp_pass = StringVar()

    #registering screen
    register_screen=Toplevel(master)
    register_screen.title('REGISTER TO BANK MANAGER')
    register_screen.geometry('500x500')

    Label(register_screen,text="FILL THE DETAILS TO REGISTER",font=('calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", font=('calibri', 12)).grid(row=1, sticky=W)
    Label(register_screen, text="Age", font=('calibri', 12)).grid(row=2, sticky=W)
    Label(register_screen, text="Email", font=('calibri', 12)).grid(row=3, sticky=W)
    Label(register_screen, text="Password", font=('calibri', 12)).grid(row=4, sticky=W)
    notif=Label(register_screen, font=('calibri', 12))
    notif.grid(row=10, sticky=N,pady=10)

    Entry(register_screen,textvariable=temp_name).grid(row=1,sticky=E,column=2)
    Entry(register_screen, textvariable=temp_age).grid(row=2, sticky=E,column=2)
    Entry(register_screen, textvariable=temp_email).grid(row=3, sticky=E,column=2)
    Entry(register_screen, textvariable=temp_pass,show="*").grid(row=4, sticky=E,column=2)

    def finish_reg():
        name=temp_name.get()
        age=temp_age.get()
        email=temp_email.get()
        password=temp_pass.get()
        all_accounts = os.listdir()

        if name == "" or age=="" or email=="" or password=="":
            notif.config(fg='red',text="ALL FIELDS ARE REQUIRED!!")
            return

        for i in all_accounts:
            if name== i:
                notif.config(fg='red',text="USER ALREADY EXIST!!")
                return
            else:
                new_file= open(name,"w")
                new_file.write(name+'\n')
                new_file.write(password + '\n')
                new_file.write(email + '\n')
                new_file.write(age+'\n')
                new_file.write('0')
                new_file.close()
                notif.config(fg='green',text="CONGRATULATIONS!! ACCOUNT SUCCESFULLY CREATED")

    Button(register_screen, text='REGISTER', font=('calibri', 12), width=20, command=finish_reg).grid(row=6, sticky=S)

b2=Button(master, text='REGISTER', font=('calibri',12),width=20,command=register).grid(row=4,sticky=N)

#USER AUTHENTICATION MODULE

def login_session():
    global login_name
    global login_password
    all_accounts= os.listdir()
    login_name=temp_login_name.get()
    login_password= temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file= open(name,"r")
            file_data=file.read()
            file_data= file_data.split('\n')
            password= file_data[1]
            if login_password == password:
                login_screen.destroy()
                account_dashboard= Toplevel(master)
                account_dashboard.title('Account Dashboard')
                account_dashboard.geometry('400x400')

                #labeling
                Label(account_dashboard,text="ACCOUNT DASHBOARD",font=('calibri',12)).grid(row=0,sticky=N,padx=10)
                Label(account_dashboard, text="Welcome "+name, font=('calibri', 12)).grid(row=1, sticky=N, padx=100)

                #buttons
                Button(account_dashboard, text='Check balance', font=('calibri', 12), width=30,command=Balance).grid(row=10, sticky=S, padx=10)
                Button(account_dashboard,text='Personal details',font=('calibri',12),width=30,command=personal_details).grid(row=7,sticky=S,padx=10)
                Button(account_dashboard, text='Deposit', font=('calibri', 12), width=30,command=deposit).grid(row=8, sticky=S,padx=10)
                Button(account_dashboard, text='Withdraw', font=('calibri', 12), width=30,command=withdraw).grid(row=9, sticky=S, padx=10)

                return

            else:
                login_notif.config(fg='red', text="PASSWORD doesnt match! Please TRY AGAIN")
            return
        else:
            login_notif.config(fg='red', text="USER NOT FOUND!!")

def login():
    global temp_login_name
    global login_notif
    global temp_login_email
    global temp_login_password
    global login_screen
    temp_login_name= StringVar()
    temp_login_password = StringVar()

    login_screen = Toplevel(master)
    login_screen.title('Login To Your Account')
    login_screen.geometry('400x400')

    Label(login_screen,text='Login To Your Account',font=('Calibri',12)).grid(row=1,sticky=N,pady=10)
    Label(login_screen, text='Username', font=('Calibri', 12)).grid(row=3, sticky=W)
    Label(login_screen, text='Password', font=('Calibri', 12)).grid(row=4, sticky=W,)

    login_notif= Label(login_screen,font=('Calibri',12))
    login_notif.grid(row=12,sticky=N,pady=5)

    Entry(login_screen, textvariable=temp_login_name).grid(row=3,sticky=E,padx=5,column=1)
    Entry(login_screen, textvariable=temp_login_password,show='*').grid(row=4,sticky=E,column=1,padx=5)

    Button(login_screen,text='Login',font=('calibri',12),width=15,command=login_session).grid(row=10,sticky=W,pady=5,padx=5)



b1=Button(master, text='LOGIN', font=('calibri',12),width=20,command=login).grid(row=3,sticky=N)

#gffdfgfg



def personal_details():
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name= user_details[0]
    details_age= user_details[3]
    details_email=user_details[2]

    #personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    personal_details_screen.geometry('400x400')

    Label(personal_details_screen, text='PERSONAL DETAILS', font=('Calibri', 16)).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text='Name : '+details_name, font=('Calibri', 12)).grid(row=1, sticky=N)
    Label(personal_details_screen, text='Age : '+details_age, font=('Calibri', 12)).grid(row=2, sticky=N)
    Label(personal_details_screen, text='Email : '+details_email, font=('Calibri', 12)).grid(row=3, sticky=N)


def deposit():
    print("kkk")
    #dummy

def withdraw():
    print("aaa")
    #dummy just to define value
def Balance():
    print("uuu")
#dummy




master.mainloop()