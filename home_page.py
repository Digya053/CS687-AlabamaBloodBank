import tkinter as tk
from tkinter import *

from functools import partial
from PIL import ImageTk, Image

from user_interfaces.windows import user_login

from queries.validate_register import validate_and_insert_users
from queries.validate_login import login_user
from tkcalendar import DateEntry


# This creates the main window and home page of the application
class Window:
    def __init__(self, window):
        self.window = window

        self.canvas = tk.Canvas(self.window, width=200, height=40, bd=0, relief='ridge',bg='white')
        self.canvas.pack()

        path = "images/blood-bank2.jpeg"

        #For logo
        self.img = Image.open(path)
        self.img = self.img.resize((1430, 1190), Image.BICUBIC)
        self.img = ImageTk.PhotoImage(self.img)

        self.panel = tk.Label(self.window, image = self.img)

        self.panel.pack(side = "top", fill = "both", expand = "yes")

        #For user registration
        buttonBG = self.canvas.create_rectangle(0, 0, 100,100, fill="red", outline="white")
        buttonTXT = self.canvas.create_text(51, 25, text="Register")
        self.canvas.tag_bind(buttonBG, "<Button-1>", register_clicked)
        self.canvas.tag_bind(buttonTXT, "<Button-1>", register_clicked) 

        #For login
        buttonBG = self.canvas.create_rectangle(101, 0, 201, 100,fill="red", outline="white")
        buttonTXT = self.canvas.create_text(150, 25, text="Login")
        self.canvas.tag_bind(buttonBG, "<Button-1>", login_clicked)
        self.canvas.tag_bind(buttonTXT, "<Button-1>", login_clicked)

    def return_window(self):
        return window


def register_clicked(event):
    #print("register pressed")
    register_window = tk.Toplevel(window)
    register_window.title("Registration Page")

    #username label and text entry box
    fnamelabel = Label(register_window, text="First Name*").grid(row=0, column=0)
    fname = StringVar()
    fnameEntry = Entry(register_window, textvariable=fname).grid(row=0, column=1)

    mnitlabel = Label(register_window, text="MName Initial").grid(row=1, column=0)
    mnit = StringVar()
    mnitEntry = Entry(register_window, textvariable=mnit).grid(row=1, column=1)

    lnamelabel = Label(register_window, text="Last Name*").grid(row=2, column=0)
    lname = StringVar()
    lnameEntry = Entry(register_window, textvariable=lname).grid(row=2, column=1)

    dateLabel = Label(register_window, text="Date of Birth*").grid(row=3, column=0)
    dob = DateEntry(register_window, 
               foreground='black', date_pattern='yyyy-MM-dd')
    dob.grid(row=3,column=1)

    citylabel = Label(register_window, text="City*").grid(row=4, column=0)
    city = StringVar()
    cityEntry = Entry(register_window, textvariable=city).grid(row=4, column=1)

    bloodtypelabel = Label(register_window, text="Blood Type*").grid(row=5, column=0)
    bloodtype = StringVar()
    bloodtypeEntry = Entry(register_window, textvariable=bloodtype).grid(row=5, column=1)

    genderlabel = Label(register_window, text="Gender*").grid(row=6, column=0)
    gender = StringVar()
    genderEntry = Entry(register_window, textvariable=gender).grid(row=6, column=1)

    emaillabel = Label(register_window, text="Email*").grid(row=7, column=0)
    email = StringVar()
    emailEntry = Entry(register_window, textvariable=email).grid(row=7, column=1)

    passwordlabel = Label(register_window, text="Password*").grid(row=10, column=0)
    password = StringVar()
    passwordEntry = Entry(register_window, textvariable=password,show='*').grid(row=10, column=1)

    confirmpasswordlabel = Label(register_window, text="Confirm Password*").grid(row=11, column=0)
    confirmpassword = StringVar()
    confirmpasswordEntry = Entry(register_window, textvariable=confirmpassword,show='*').grid(row=11, column=1)

    weightlabel = Label(register_window, text="Weight*").grid(row=8, column=0)
    weight = IntVar()
    weightEntry = Entry(register_window, textvariable=weight).grid(row=8, column=1)

    heightlabel = Label(register_window, text="Height*").grid(row=9, column=0)
    height = IntVar()
    heightEntry = Entry(register_window, textvariable=height).grid(row=9, column=1)

    ssnlabel = Label(register_window, text="SSN*").grid(row=13, column=0)
    ssn = IntVar()
    print(ssn)
    ssnEntry = Entry(register_window, textvariable=ssn).grid(row=13, column=1)

    hmembership_nolabel = Label(register_window, text="Hospital Membership Number*").grid(row=12, column=0)
    hmembership_no = StringVar()
    hmembershipEntry = Entry(register_window, textvariable=hmembership_no).grid(row=12, column=1)

    validater = partial(validate_and_insert_users, fname,mnit,lname,dob,city,bloodtype,gender,email,password,confirmpassword,weight,height,ssn, hmembership_no)

    registerButton = Button(register_window, text="Register", command=validater)
    registerButton.grid(row=20, column=3)

    register_window.mainloop
    return 

def login_clicked(event):
    login_window = tk.Toplevel(window)
    login_window.title("Login Page")
    
    #username label and text entry box
    emailLabel = Label(login_window, text="Email").grid(row=0, column=0)
    email = StringVar()
    emailEntry = Entry(login_window, textvariable=email).grid(row=0, column=1)  

    #password label and password entry box
    passwordLabel = Label(login_window,text="Password").grid(row=1, column=0)  
    password = StringVar()
    passwordEntry = Entry(login_window, textvariable=password, show='*').grid(row=1, column=1)  

    validate = partial(login_user,login_window, email, password)

    #login button
    loginButton = Button(login_window, text="Login", command=validate).grid(row=4, column=3)

    login_window.mainloop
    return 



window = tk.Tk()
window.title("Welcome to Alabama Blood Bank")
window.attributes('-fullscreen', True)
window.configure(background='#FFFFFF')

w = Window(window)

window.mainloop()

    #window.mainloop
