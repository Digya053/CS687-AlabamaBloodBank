from db_connection import connection
from tkinter import messagebox
from tkinter import *
from functools import partial

from datetime import date

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

def check_delete(i, ssn, con):

    query = "DELETE FROM PARTICIPATES_IN as p WHERE p.event_id = " + i.get() + " AND p.pssn = '" + str(ssn.get()) + "';"
    try:
        con.execute_command(query)
        con.commit_changes()
        messagebox.showinfo("Information", "Successfully deleted.")
    except Exception as e:
        messagebox.showerror("Error", e)