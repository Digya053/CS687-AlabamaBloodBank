from datetime import date
from tkinter import messagebox

from db_connection import connection
from user_interfaces.tables.treeview import TreeView

def show_donation_records(cal, city):
    """
    Query to display all donation records within Alabama Blood Bank.
    """
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