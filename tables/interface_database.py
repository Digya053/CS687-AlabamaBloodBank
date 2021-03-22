from tkinter import messagebox
import tkinter as tk
from tkinter import *
#from user_interfaces import start_page
from db_connection import connection
from cryptography.fernet import Fernet


def insert_registered_users(fname, mnit, lname, dob, city, bloodtype, gender, email, password, confirmpassword,
    weight, height, ssn, hmembership_no):
    #start_page.register_clicked(event)
    print('reached here')
    # key = Fernet.generate_key()
    # cipher_suite=Fernet(key)
    # print(password)
    # password = cipher_suite.encrypt(str.encode(password))
    # print(password)
    # confirmpassword = cipher_suite.encrypt(str.encode(confirmpassword))
    # print(confirmpassword)
    print(ssn)
    if password != '' and fname!='' and ssn>0:
        if password!=confirmpassword:
            messagebox.showerror("String doesn't match ", "Password and ConfirmPassword do not match.")

        if not fname or not lname or not dob or not bloodtype or not gender or not email or not password or not confirmpassword or not weight or not height or not ssn or not hmembership_no:
            messagebox.showerror("Missing fields", "One or more required fields are missing.")

        con = connection.Connection()

        my_data=(fname, mnit, lname, ssn, dob, city, bloodtype, gender, email, password, weight, height, hmembership_no)
        print(my_data)
        query = """INSERT INTO users_registeredusers(fname, mnit, lname, ssn, dob, city, blood_type, gender, email, password, weight_in_lbs, height_in_lbs, hmembership_no)
        VALUES """+str(my_data)
        print(query)

        if fname != '' and ssn > 0:
            con.execute_command(query)
            print('query executed')
            con.commit_changes()
            messagebox.showinfo("information","The user has been registered.")
        
    
    # con = Connection()
    # # print("=========================================")
    # # print(ssn)
    # # query = "INSERT INTO users_registeredusers(fname, mnit, lname, ssn, dob, city, blood_type, gender, email, password, weight_in_lbs, height_in_lbs, hmembership_no) \
    # #      VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 

    # my_data=(fname, mnit, lname, ssn, dob, city, bloodtype, gender, email, password, weight, height, hmembership_no)
    # print(my_data)
    # query = """INSERT INTO users_registeredusers(fname, mnit, lname, ssn, dob, city, blood_type, gender, email, password, weight_in_lbs, height_in_lbs, hmembership_no)
    # VALUES """+str(my_data)
    # print(query)
    
    # # print(query)

    # # "INSERT INTO  `student` (`name` ,`class` ,`mark` ,`gender`) \
    # #         VALUES(%s,%s,%s,%s)"
    
