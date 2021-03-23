import tkinter as tk
from tkinter import *

from functools import partial
from queries.delete_event import delete_checkbox

def delete_scheduled_events(window):

    """
    User Interface for 'Delete Scheduled Blood Donation Event' button.
    """

    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Scheduled Event")
    Label(delete_window, text="Select Event").grid(row=0, column=1)

    ssn = Label(delete_window, text="Enter SSN *").grid(row=0, column=0)
    ssn = IntVar()
    ssnEntry = Entry(delete_window, textvariable=ssn).grid(row=0, column=1)

    validate_d = partial(delete_checkbox, ssn, delete_window)

    show_records = Button(delete_window, text = "Submit",command=validate_d).grid(row=1,column=3)

    delete_window.mainloop