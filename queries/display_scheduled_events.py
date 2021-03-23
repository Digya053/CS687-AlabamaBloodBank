from db_connection import connection
from tkinter import messagebox
from user_interfaces.tables.treeview import TreeView


def show_events(ssn):

    """
    Display all scheduled events.
    """

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