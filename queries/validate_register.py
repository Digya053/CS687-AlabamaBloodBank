from db_connection import connection
from tkinter import messagebox

def validate_and_insert_users(fname, mnit,lname, dob, city, bloodtype, gender, email, password, confirmpassword, weight, height, ssn, hmembership_no):
    """
    Add user information into the database.
    """
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

    if password != '' and fname!='':
        if password!=confirmpassword:
            messagebox.showerror("String doesn't match ", "Password and ConfirmPassword do not match.")
            return

        if not fname or not lname or not dob or not bloodtype or not gender or not email or not password or not confirmpassword or not weight or not height or not ssn or not hmembership_no:
            messagebox.showerror("Missing fields", "One or more required fields are missing.")
            return

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
        