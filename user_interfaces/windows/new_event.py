import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry

from functools import partial
from queries.new_event import add_event

def add_new_event(window):
    """
    Creates UI for adding new event.
    """
    add_events_window = tk.Toplevel(window)
    add_events_window.title("Add Events")

    event_id = Label(add_events_window, text="Set Event Id").grid(row=0, column=0)
    event_id = IntVar()
    eventIdEntry = Entry(add_events_window, textvariable=event_id).grid(row=0, column=1)

    event_name = Label(add_events_window, text="Event Name").grid(row=1, column=0)
    event_name = StringVar()
    eventNameEntry = Entry(add_events_window, textvariable=event_name).grid(row=1, column=1)

    Label(add_events_window, text='Date of Event:').grid(row=2, column=0)
    cal = DateEntry(add_events_window, 
               foreground='black', date_pattern='yyyy-MM-dd')
    cal.grid(row=2,column=1)
    s = ttk.Style(add_events_window)
    #s.theme_use('clam')

    street = Label(add_events_window, text="Street").grid(row=3, column=0)
    street = StringVar()
    streetEntry = Entry(add_events_window, textvariable=street).grid(row=3, column=1)

    city = Label(add_events_window, text="City").grid(row=4, column=0)
    city = StringVar(add_events_window)
    city.set("Huntsville")
    cityEntry = OptionMenu(add_events_window, city, "Huntsville", "Birmingham", "Madison")
    cityEntry.grid(row=4, column=1)

    organizer_name = Label(add_events_window, text="Organizer Name").grid(row=5, column=0)
    organizer_name = StringVar(add_events_window)
    organizer_name.set("The University of Alabama in Huntsville")
    organizerNameEntry = OptionMenu(add_events_window, organizer_name, "The University of Alabama in Huntsville", "Lions club", "Red Cross Society", "Florence club", "Birmingham Club", "Athens Club", "Madison Club", "Geo club", "Womens club")
    organizerNameEntry.grid(row=5, column=1)

    validateAddEvent = partial(add_event, event_id, event_name, cal, street, city, organizer_name)

    add = Button(add_events_window, text = "Add Event",command=validateAddEvent).grid(row=6,column=3)