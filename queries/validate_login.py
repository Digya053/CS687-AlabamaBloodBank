from db_connection import connection
from tkinter import messagebox
from user_interfaces.options import view_options

def login_user(window, email, password):
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
        view_options(window)
    else:
        messagebox.showerror("Error", "credentials do not match")

    return