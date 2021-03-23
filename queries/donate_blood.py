import tkinter as tk
from tkinter import *

from functools import partial
from queries.save_event import save

from db_connection import connection
from tkinter import messagebox

from datetime import date

def donate(window):
    """
    Creates UI selection buttons for scheduling donation.
    """
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


    validate_s = partial(save,i,ssn)

    show_records = Button(schedule_window, text = "Save Event",command=validate_s).grid(row=len(combined_text_list)+3,column=3)

    schedule_window.mainloop