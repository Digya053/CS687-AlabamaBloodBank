from tkinter import messagebox

from db_connection import connection
from user_interfaces.tables.treeview import TreeView

from datetime import date

def past_events():
    
    """
    Displays all past blood donation events.
    """

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