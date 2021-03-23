from tkinter import messagebox

from db_connection import connection
from user_interfaces.tables.treeview import TreeView

def request_records():
    """
    Displays user records who has requested the blood unit.
    """
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