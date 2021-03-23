from db_connection import connection
from tkinter import messagebox
from user_interfaces.tables.treeview import TreeView
import tkinter as tk
from tkinter import *
from functools import partial

def show_events(ssn):

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

def display_saved_events(window):
    show_schedule_window = tk.Toplevel(window)
    show_schedule_window.title("Scheduled Blood Donations")

    ssn = Label(show_schedule_window, text="Enter SSN*").grid(row=0, column=0)
    ssn = IntVar()
    ssnEntry = Entry(show_schedule_window, textvariable=ssn).grid(row=0, column=1)

    validate_schedule = partial(show_events,ssn)

    show_organizers = tk.Button(show_schedule_window, text = "Submit",command=validate_schedule).grid(row=1,column=3)
    show_schedule_window.mainloop