from db_connection import connection
from tkinter import messagebox

def display_organizer_info(organizers, eventname, cal, city, street):
    con = connection.Connection()

    query = "SELECT o.organizer_name, o.contact_no, o.email, e.event_name, e.date, e.street, e.city FROM ORGANIZERS as o, BLOOD_DONATION_EVENT as e WHERE o.organizer_id=e.organizer_id AND e.event_name= '" + str(eventname.get()) + "' AND e.date= '" + str(cal.get()) + "' AND e.street = '" + str(street.get()) + "' AND e.city = '" + str(city.get()) + "';"
    print(query)
    try:
        con.execute_command(query)
    except Exception as e:
        messagebox.showerror("Error", e)
    all_results  = con.fetch_all()

    organizerss = {}
    for result in all_results:
        result_splitted = str(result).replace("(","").replace(")","").split(",")
        organizerss['Organizer Name'] = result_splitted[0]
        organizerss['Organizer Contact No'] = result_splitted[1]
        organizerss['Organizer Email'] = result_splitted[2]
    
    organizer_results = str(organizerss).replace("{","").replace("}","")

    organizers.set(organizer_results)

    return