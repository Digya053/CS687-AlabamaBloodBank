from db_connection import connection
from tkinter import messagebox

def add_event(event_id, event_name, cal, street, city, organizer_name):
        
        """Adds new event to the database.
        """
        
        con = connection.Connection()
        try:
            query_one = "SELECT o.organizer_id FROM ORGANIZERS AS o WHERE o.organizer_name = '" + organizer_name.get() + "';"
        except Exception as e:
            messagebox.showerror("Error", e)
        con.execute_command(query_one)
        organizer_id = con.fetch_one()

        my_data=('EI' + str(event_id.get()), event_name.get(), str(cal.get()), street.get(), city.get(), organizer_id[0])
        print(my_data)
        query_two = """INSERT INTO BLOOD_DONATION_EVENT(event_id, event_name, date, street, city, organizer_id)
        VALUES """+str(my_data)
        try:
            con.execute_command(query_two)
            con.commit_changes()
            messagebox.showinfo("Information", "The event has been saved.")
        except Exception as e:
            messagebox.showerror("Error", e)
        return
        