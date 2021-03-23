import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry

from functools import partial
from queries.organizer_details import display_organizer_info

def organizer_details(window):
    """
    Creates UI for displaying organizer details.
    """
    organizer_window = tk.Toplevel(window)
    organizer_window.title("View Organizer")

    eventname = Label(organizer_window, text="Event Name").grid(row=0, column=0)
    eventname = StringVar()
    eventNameEntry = Entry(organizer_window, textvariable=eventname).grid(row=0, column=1)

    tk.Label(organizer_window, text='Event Date:').grid(row=1, column=0)

    cal = DateEntry(organizer_window, 
               foreground='black', date_pattern='yyyy-MM-dd')
    cal.grid(row=1,column=1)

    city = Label(organizer_window, text="City").grid(row=2, column=0)
    city = StringVar()
    cityEntry = Entry(organizer_window, textvariable=city).grid(row=2, column=1) 

    street = Label(organizer_window, text="Street").grid(row=3, column=0)
    street = StringVar()
    streetEntry = Entry(organizer_window, textvariable=street).grid(row=3, column=1) 

    organizers = Label(organizer_window, text="Organizer Details").grid(row=6, column=0)
    organizers = StringVar()
    organizers_entry = Entry(organizer_window, width="100",textvariable=organizers)
    organizers_entry.grid(row=6,columnspan=2, padx=100,pady=100,ipady=100)

    validate_organizers = partial(display_organizer_info, organizers, eventname, cal, city, street)

    show_organizers = tk.Button(organizer_window, text = "Show Organizers",command=validate_organizers).grid(row=4,column=3)

    



