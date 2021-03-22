import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from tkinter.ttk import *
from typing import ValuesView
from PIL import ImageTk, Image
from functools import partial
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from db_connection import connection
from cryptography.fernet import Fernet
import pandas as pd
from user_interfaces.treeview import TreeView
from datetime import date


#This creates the main window of an application
window = tk.Tk()
window.title("Welcome to Alabama Blood Bank")
#window.geometry("1000x1000")
window.attributes('-fullscreen', True)
window.configure(background='#FFFFFF')
canvas = tk.Canvas(window, width=200, height=40, bd=0, relief='ridge',bg='white')
canvas.pack()

path = "images/blood-bank2.jpeg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = Image.open(path)
img = img.resize((1430, 1190), Image.BICUBIC)
img = ImageTk.PhotoImage(img)

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "top", fill = "both", expand = "yes")

organizer_s = StringVar()


def validateRegister(fname, mnit,lname, dob, city, bloodtype, gender, email, password, confirmpassword, weight, height, ssn, hmembership_no):
    fname = fname.get()
    mnit = mnit.get()
    lname = lname.get()
    dob = dob.get()
    city = city.get()
    bloodtype = bloodtype.get()
    gender = gender.get()
    email = email.get()
    password = password.get()
    confirmpassword = confirmpassword.get()
    weight = weight.get()
    height = height.get()
    ssn = ssn.get()
    hmembership_no = hmembership_no.get()

    # key = Fernet.generate_key()
    # cipher_suite=Fernet(key)
    # print(password)
    # password = cipher_suite.encrypt(str.encode(password))
    # print(password)
    # confirmpassword = cipher_suite.encrypt(str.encode(confirmpassword))
    # print(confirmpassword)

    if password != '' and fname!='':
        if password!=confirmpassword:
            messagebox.showerror("String doesn't match ", "Password and ConfirmPassword do not match.")

        if not fname or not lname or not dob or not bloodtype or not gender or not email or not password or not confirmpassword or not weight or not height or not ssn or not hmembership_no:
            messagebox.showerror("Missing fields", "One or more required fields are missing.")

        con = connection.Connection()

        my_data=(fname, mnit, lname, ssn, dob, city, bloodtype, gender, email, password, weight, height, hmembership_no)
        print(my_data)
        query = """INSERT INTO REGISTERED_USERS(fname, mnit, lname, ssn, dob, city, blood_type, gender, email, password, weight_in_lbs, height_in_lbs, hmembership_no)
        VALUES """+str(my_data)
        print(query)

        if fname != '':
            try:
                con.execute_command(query)
                print('query executed')
                con.commit_changes()
                messagebox.showinfo("Information","The user has been registered.")
            except Exception as e:
                messagebox.showerror("Error", e)
    return

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

    validater = partial(validateRegister, fname,mnit,lname,dob,city,bloodtype,gender,email,password,confirmpassword,weight,height,ssn, hmembership_no)

    registerButton = Button(register_window, text="Register", command=validater)
    registerButton.grid(row=20, column=3)

    register_window.mainloop
    

def validateLogin(email, password):
    email = email.get()
    password = password.get()
    print("email entered :", email)
    print("password entered :", password)

    con = connection.Connection()

    query = "SELECT * FROM REGISTERED_USERS WHERE email = '" + email + "' AND password = '" + password +"';"
    con.execute_command(query)

    if len(con.fetch_all()) > 0:
        print("reached here")
        messagebox.showinfo("Information","The user is logged in.")
        view_options()
    else:
        messagebox.showerror("Error", "credentials do not match")

    return

def check_availability(blood_type, age, weight, height, gender, quantity_in_ml):
    blood_type = blood_type.get()
    age = age.get()
    weight = weight.get()
    height = height.get()
    gender = gender.get()
    quantity_in_ml = quantity_in_ml.get()

    if blood_type !='':
        con = connection.Connection()
        query = "SELECT bs.blood_type, bs.quantity_in_ml, bs.storage_id FROM ALABAMA_BLOOD_STORAGE as bs, BLOOD as b WHERE b.storage_id = bs.storage_id AND bs.blood_type= '" + blood_type + "' AND b.d_gender= '" + gender + "' AND b.d_height>= " + str(height) + " AND b.d_weight>= " + str(weight) + " AND b.d_age<= " + str(age) + " AND b.storage_id = bs.storage_id AND bs.quantity_in_ml >= " + str(quantity_in_ml) + ";"
        con.execute_command(query)
        all_results = con.fetch_all()

        availability_results = []
        for result in all_results:
            availability_results.append(result)
        
        column_names = ("Blood Type", "Quantity", "StorageId")
        data = availability_results
        title = "Results of Blood Availability"
        tr = TreeView(column_names, data, title)
    else:
        messagebox.showerror("Error", "Blood Type is empty")
    return

def show_availability():
    availability_window = tk.Toplevel(window)
    availability_window.title("Check Blood Availability")

    l = Label(availability_window, text = 'Please fill details about persion to be transfusioned.')

    blood_type = Label(availability_window, text="Blood Type*").grid(row=0, column=0)
    blood_type = StringVar()
    bloodtypeEntry = Entry(availability_window, textvariable=blood_type).grid(row=0, column=1)

    age = Label(availability_window, text="Age").grid(row=1, column=0)
    age = IntVar()
    ageEntry = Entry(availability_window, textvariable=age).grid(row=1, column=1)
    age.set(100)

    weight = Label(availability_window, text="Weight (lbs)").grid(row=2, column=0)
    weight = IntVar()
    weightEntry = Entry(availability_window, textvariable=weight).grid(row=2, column=1)

    height = Label(availability_window, text="Height (lbs)").grid(row=3, column=0)
    height = IntVar()
    heightEntry = Entry(availability_window, textvariable=height).grid(row=3, column=1)

    gender = Label(availability_window, text="Gender*").grid(row=4, column=0)
    gender = StringVar()
    genderEntry = Entry(availability_window, textvariable=gender).grid(row=4, column=1)

    quantity = Label(availability_window, text="Quantity Required (mL)").grid(row=5, column=0)
    quantity = IntVar()
    quantityEntry = Entry(availability_window, textvariable=quantity).grid(row=5, column=1)

    validate_check = partial(check_availability,blood_type, age, weight, height, gender, quantity)

    check_blood = tk.Button(availability_window, text = "Check Availability", command=validate_check).grid(row=6, column=3)

    availability_window.mainloop


def check_click(i,ssn):
    print("You selected an option")
    print(i.get()) 

    con = connection.Connection()

    query_one = "SELECT * FROM REGISTERED_USERS WHERE ssn = '" + str(ssn.get())+"';" 
    try:
        con.execute_command(query_one)
    except Exception as e:
        messagebox.showerror("Error",e)

    if con.fetch_all():
        my_data = (ssn.get(),i.get().replace("'",""))
        query_two = "INSERT INTO PARTICIPATES_IN (pssn, event_id) VALUES " + str(my_data) + ";"
        try:
            con.execute_command(query_two)
            con.commit_changes()
            messagebox.showinfo("Information", "Saved Successfully.")
        except Exception as e:
            messagebox.showerror("Error",e)
    else:
        messagebox.showerror("Error", "This user isn't registered.")
    
def donate_blood():
    schedule_window = tk.Toplevel(window)
    schedule_window.title("Schedule Blood Donation")
    Label(schedule_window, text="Select Events").grid(row=0, column=1)

    today_date = date.today()

    con = connection.Connection()

    query = "SELECT e.event_id, e.event_name, e.date, e.street, e.city FROM BLOOD_DONATION_EVENT AS e WHERE e.date >= '" + str(today_date) + "';"
    try:
        con.execute_command(query)
    except Exception as e:
        messagebox.showerror("Error", e)
    all_results  = con.fetch_all()

    eid_list = []
    combined_text_list = []
    for result in all_results:
        result_splitted = str(result).replace("(", "").replace(")","").split(", ")
        eid_list.append(result_splitted[0])
        date_format = result_splitted[4].replace(")","") + "/" + result_splitted[3] + "/" + result_splitted[2].replace("datetime.date", "")
        combined_text_list.append(result_splitted[1] + "," + result_splitted[5] + "," + result_splitted[6].replace(")","") + "\n Date: " + date_format)

    i = StringVar()
    for j in range(0, len(combined_text_list)):
        c = Radiobutton(schedule_window, text = combined_text_list[j], value=eid_list[j], variable=i)
        c.grid(row = j+1, column=1)

    ssn = Label(schedule_window, text="Enter SSN *").grid(row=len(combined_text_list)+2, column=0)
    ssn = IntVar()
    ssnEntry = Entry(schedule_window, textvariable=ssn).grid(row=len(combined_text_list)+2, column=1)


    validate_s = partial(check_click,i,ssn)

    show_records = Button(schedule_window, text = "Save Event",command=validate_s).grid(row=len(combined_text_list)+3,column=3)

    schedule_window.mainloop

def show_donation_records(cal, city):
    today = date.today()

    con = connection.Connection()

    query = "SELECT r.fname, r.mnit, r.lname, r.dob, r.city, r.blood_type,r.gender,bd.event_name,bd.date,bd.street,bd.city FROM REGISTERED_USERS as r, BLOOD_DONATION_EVENT as bd, PARTICIPATES_IN as p WHERE p.pssn=r.ssn AND p.event_id=bd.event_id AND bd.date >= '" + str(cal.get()) + "' AND bd.date < '" + str(today) + "' AND bd.city = '" + str(city.get()) + "';"
    try:
        con.execute_command(query)
    except Exception as e:
        messagebox.showerror("Error", e)
    all_results  = con.fetch_all()

    donation_records = []
    for result in all_results:
        print(result)
        donation_records.append(result)

    column_names = ("Fname", "Mint", "Lname", "Date of Birth", "City", "Blood Type", "Gender", "Event Name", "Date of Blood Donation", "Street (Event organized)", "City (Event organized)")
    data = donation_records
    title = "Records of Donation"
    tr1 = TreeView(column_names, data, title)

    return

def view_donation_records():
    donation_records_window = tk.Toplevel(window)
    donation_records_window.title("View Donation Records")

    Label(donation_records_window, text='From:').grid(row=0, column=0)

    cal = DateEntry(donation_records_window, 
               foreground='black', date_pattern='yyyy-MM-dd')
    cal.grid(row=0,column=1)
    s = ttk.Style(donation_records_window)
    #s.theme_use('clam')

    city = Label(donation_records_window, text="City").grid(row=1, column=0)
    city = StringVar(donation_records_window)
    city.set("Huntsville")
    cityEntry = OptionMenu(donation_records_window, city, "Huntsville", "Birmingham", "Madison")
    cityEntry.grid(row=1, column=1)

    validateDonationRecords = partial(show_donation_records,cal, city)

    show_records = Button(donation_records_window, text = "Show records",command=validateDonationRecords).grid(row=2,column=3)


def blood_request_records():
    con = connection.Connection()

    query = "SELECT r.fname, r.mnit, r.lname, r.dob, r.city, r.blood_type, r.gender, bs.blood_type, bs.quantity_in_ml, bs.storage_id FROM REGISTERED_USERS AS r, BLOOD AS b, ALABAMA_BLOOD_STORAGE AS bs WHERE bs.storage_id=b.storage_id AND b.ssn=r.ssn;"
    try:
        con.execute_command(query)
    except Exception as e:
        messagebox.showerror("Error", e)
    all_results  = con.fetch_all()

    request_records = []
    for result in all_results:
        print(result)
        request_records.append(result)

    column_names = ("First Name", "Middle Name", "Last Name", "Date of Birth", "City", "Blood Type", "Gender", "Requested Blood Type", "Quantity Requested (in mL)", "Requested from Storage Id")
    data = request_records
    title = "Supplied Blood Requests Records"
    tr2 = TreeView(column_names, data, title)

    return

def get_organizers(eventname, cal, city, street):
    con = connection.Connection()

    query = "SELECT o.organizer_name, o.contact_no, o.email, e.event_name, e.date, e.street, e.city FROM ORGANIZERS as o, BLOOD_DONATION_EVENT as e WHERE o.organizer_id=e.organizer_id AND e.event_name= '" + str(eventname.get()) + "' AND e.date= '" + str(cal.get()) + "' AND e.street = '" + str(street.get()) + "' AND e.city = '" + str(city.get()) + "';"
    try:
        con.execute_command(query)
    except Exception as e:
        messagebox.showerror("Error", e)
    all_results  = con.fetch_all()

    organizerss = {}
    for result in all_results:
        result_splitted = str(result).replace("(","").replace(")","").split(",")
        organizerss['Organizer Name'] = result_splitted[0]
        organizerss['Organizer Contact No'] = result_splitted[1]
        organizerss['Organizer Email'] = result_splitted[2]

    organizer_results = str(organizerss).replace("{","").replace("}","")

    global organizer_s
    organizer_s.set(organizer_results)

    return

def organizer_details():
    organizer_window = tk.Toplevel(window)
    organizer_window.title("View Organizer")

    eventname = Label(organizer_window, text="Event Name").grid(row=0, column=0)
    eventname = StringVar()
    eventNameEntry = Entry(organizer_window, textvariable=eventname).grid(row=0, column=1)

    tk.Label(organizer_window, text='Event Date:').grid(row=1, column=0)

    cal = DateEntry(organizer_window, 
               foreground='black', date_pattern='yyyy-MM-dd')
    cal.grid(row=1,column=1)
    #s = ttk.Style(organizer_window)
    #s.theme_use('clam')

    city = Label(organizer_window, text="City").grid(row=2, column=0)
    city = StringVar()
    cityEntry = Entry(organizer_window, textvariable=city).grid(row=2, column=1) 

    street = Label(organizer_window, text="Street").grid(row=3, column=0)
    street = StringVar()
    streetEntry = Entry(organizer_window, textvariable=street).grid(row=3, column=1) 

    validate_organizers = partial(get_organizers,eventname, cal, city, street)

    show_organizers = tk.Button(organizer_window, text = "Show Organizers",command=validate_organizers).grid(row=4,column=3)

    organizers = Label(organizer_window, text="Organizer Details").grid(row=6, column=0)
    organizers_entry = Entry(organizer_window, width="100",textvariable=organizer_s)
    organizers_entry.grid(row=6,columnspan=2, padx=100,pady=100,ipady=100)

def upcoming_events():
    now = date.today()

    con = connection.Connection()

    query = "SELECT e.event_name, e.date, e.street, e.city FROM BLOOD_DONATION_EVENT AS  e WHERE e.date > '" + str(now) + "';"
    try:
        con.execute_command(query)
    except Exception as e:
        messagebox.showerror("Error", e)
    all_results  = con.fetch_all()

    event_records = []
    for result in all_results:
        print(result)
        event_records.append(result)

    column_names = ("Event Name", "Date", "Street", "City")
    data = event_records
    title = "Upcoming Events"
    tr8 = TreeView(column_names, data, title)

    return

def show_scheduled_events(ssn):

    con = connection.Connection()

    query = "SELECT e.event_name, e.date, e.street, e.city FROM BLOOD_DONATION_EVENT AS e, PARTICIPATES_IN AS p WHERE p.pssn = '" + str(ssn.get())  + "' AND p.event_id=e.event_id;"
    try:
        con.execute_command(query)
    except Exception as e:
        messagebox.showerror("Error", e)
    all_results  = con.fetch_all()

    event_records = []
    for result in all_results:
        print(result)
        event_records.append(result)

    column_names = ("Event Name", "Date", "Street", "City")
    data = event_records
    title = "All Schedules Events"
    tr9 = TreeView(column_names, data, title)

def show_schedule():
    show_schedule_window = tk.Toplevel(window)
    show_schedule_window.title("Scheduled Blood Donations")

    ssn = Label(show_schedule_window, text="Enter SSN*").grid(row=0, column=0)
    ssn = IntVar()
    ssnEntry = Entry(show_schedule_window, textvariable=ssn).grid(row=0, column=1)

    validate_schedule = partial(show_scheduled_events,ssn)

    show_organizers = tk.Button(show_schedule_window, text = "Submit",command=validate_schedule).grid(row=1,column=3)
    show_schedule_window.mainloop


def past_events():
    now = date.today()

    con = connection.Connection()

    query = "SELECT e.event_name, e.date, e.street, e.city FROM BLOOD_DONATION_EVENT AS  e WHERE e.date <= '" + str(now) + "';"
    try:
        con.execute_command(query)
    except Exception as e:
        messagebox.showerror("Error",e)
    all_results  = con.fetch_all()

    event_records = []
    for result in all_results:
        print(result)
        event_records.append(result)

    column_names = ("Event Name", "Date", "Street", "City")
    data = event_records
    title = "Past Events"
    tr9 = TreeView(column_names, data, title)

    return

def check_delete(i, ssn, con):

    query = "DELETE FROM PARTICIPATES_IN as p WHERE p.event_id = " + i.get() + " AND p.pssn = '" + str(ssn.get()) + "';"
    try:
        con.execute_command(query)
        con.commit_changes()
        messagebox.showinfo("Information", "Successfully deleted.")
    except Exception as e:
        messagebox.showerror("Error", e)

def delete_checkbox(ssn, delete_window):

    today_date = date.today()

    con = connection.Connection()

    query = "SELECT e.event_id, e.event_name, e.date, e.street, e.city FROM BLOOD_DONATION_EVENT AS e, PARTICIPATES_IN AS p WHERE p.pssn = '" + str(ssn.get())  + "' AND p.event_id=e.event_id;"
    try:
        con.execute_command(query)
    except Exception as e:
        messagebox.showerror("Error", e)
    all_results  = con.fetch_all()

    eid_list = []
    combined_text_list = []
    for result in all_results:
        result_splitted = str(result).replace("(", "").replace(")","").split(", ")
        eid_list.append(result_splitted[0])
        date_format = result_splitted[4].replace(")","") + "/" + result_splitted[3] + "/" + result_splitted[2].replace("datetime.date", "") 
        combined_text_list.append(result_splitted[1] + "," + result_splitted[5] + "," + result_splitted[6].replace(")","") + "\n Date: " + date_format)

    i = StringVar()
    for j in range(0, len(combined_text_list)):
        print(j+1)
        print(eid_list[j])
        c = Radiobutton(delete_window, text = combined_text_list[j], value=eid_list[j], variable=i)
        c.grid(row = j+2, column=1)


    validate_s = partial(check_delete,i,ssn, con)


    delete_records = Button(delete_window, text = "Delete Event",command=validate_s).grid(row=len(combined_text_list)+5,column=3)

def delete_schedule():
    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Scheduled Event")
    Label(delete_window, text="Select Event").grid(row=0, column=1)

    ssn = Label(delete_window, text="Enter SSN *").grid(row=0, column=0)
    ssn = IntVar()
    ssnEntry = Entry(delete_window, textvariable=ssn).grid(row=0, column=1)

    validate_d = partial(delete_checkbox, ssn, delete_window)

    show_records = Button(delete_window, text = "Submit",command=validate_d).grid(row=1,column=3)

    delete_window.mainloop
    

def view_options():
    options_window = tk.Toplevel(window)
    options_window.title("Options")

    button1 = tk.Button(options_window, text = "Blood Request", height=3, width=40, command=show_availability)
    button1.place(x=500, y=100)

    button2 = tk.Button(options_window, text = "Schedule Blood Donation", height=3, width=40, command=donate_blood)
    button2.place(x=500, y=158)

    button2 = tk.Button(options_window, text = "Show Scheduled Blood Donation", height=3, width=40, command=show_schedule)
    button2.place(x=500, y=216)

    button2 = tk.Button(options_window, text = "Delete Scheduled Blood Donation", height=3, width=40, command=delete_schedule)
    button2.place(x=500, y=274)

    button3 = tk.Button(options_window, text = "View Donation Records", height=3, width=40, command=view_donation_records)
    button3.place(x=500, y=332)

    button4 = tk.Button(options_window, text = "View Supplied Blood Requests Records", height=3, width=40, command=blood_request_records)
    button4.place(x=500, y=390)

    button5 = tk.Button(options_window, text = "View Organizer", height=3, width=40, command=organizer_details)
    button5.place(x=500, y=448)

    button6 = tk.Button(options_window, text = "View Upcoming Blood Donation Events", height=3, width=40, command=upcoming_events)
    button6.place(x=500, y=506)

    button7 = tk.Button(options_window, text = "View Past Blood Donation Events", height=3, width=40, command=past_events)
    button7.place(x=500, y=564)

    options_window.mainloop


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

    validate = partial(validateLogin,email, password)

    #login button
    loginButton = Button(login_window, text="Login", command=validate).grid(row=4, column=3)

    login_window.mainloop
    

buttonBG = canvas.create_rectangle(0, 0, 100,100, fill="red", outline="white")
buttonTXT = canvas.create_text(51, 25, text="Register")
canvas.tag_bind(buttonBG, "<Button-1>", register_clicked) ## when the square is clicked runs function "clicked".
canvas.tag_bind(buttonTXT, "<Button-1>", register_clicked) ## same, but for the text.   

buttonBG = canvas.create_rectangle(101, 0, 201, 100,fill="red", outline="white")
buttonTXT = canvas.create_text(150, 25, text="Login")
canvas.tag_bind(buttonBG, "<Button-1>", login_clicked) ## when the square is clicked runs function "clicked".
canvas.tag_bind(buttonTXT, "<Button-1>", login_clicked)

#Start the GUI
window.mainloop()