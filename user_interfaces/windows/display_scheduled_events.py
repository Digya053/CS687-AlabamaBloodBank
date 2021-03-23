import tkinter as tk
from tkinter import *

from functools import partial
from queries.display_scheduled_events import show_events

def display_saved_events(window):

    """
    Creates user interface for displaying scheduled blood donations.
    """

    show_schedule_window = tk.Toplevel(window)
    show_schedule_window.title("Scheduled Blood Donations")

    ssn = Label(show_schedule_window, text="Enter SSN*").grid(row=0, column=0)
    ssn = IntVar()
    ssnEntry = Entry(show_schedule_window, textvariable=ssn).grid(row=0, column=1)

    validate_schedule = partial(show_events,ssn)

    show_organizers = tk.Button(show_schedule_window, text = "Submit",command=validate_schedule).grid(row=1,column=3)
    show_schedule_window.mainloop