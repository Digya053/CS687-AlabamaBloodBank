from tkinter import messagebox

from db_connection import connection

def save(i, ssn):

    """
    Inserts user as a participant of selected blood donation event.
    """

    con = connection.Connection()

    query_one = "SELECT * FROM REGISTERED_USERS WHERE ssn = '" + str(ssn.get())+"';" 
    try:
        con.execute_command(query_one)
    except Exception as e:
        messagebox.showerror("Error",e)

    if con.fetch_all():
        my_data = (ssn.get(),i.get().replace("'",""))
        query_two = "INSERT INTO PARTICIPATES_IN (pssn, event_id) VALUES " + str(my_data) + ";"
        try:
            con.execute_command(query_two)
            con.commit_changes()
            messagebox.showinfo("Information", "Saved Successfully.")
        except Exception as e:
            messagebox.showerror("Error",e)
    else:
        messagebox.showerror("Error", "This user isn't registered.")