import tkinter as tk
from tkinter import ttk
from tkinter import *

from functools import partial
from tkcalendar import DateEntry

from queries.display_donation_records import show_donation_records


def view_donation_records(window):
    donation_records_window = tk.Toplevel(window)
    donation_records_window.title("View Donation Records")

    Label(donation_records_window, text='From:').grid(row=0, column=0)

    cal = DateEntry(donation_records_window, 
               foreground='black', date_pattern='yyyy-MM-dd')
    cal.grid(row=0,column=1)
    s = ttk.Style(donation_records_window)
    #s.theme_use('clam')

    city = Label(donation_records_window, text="City").grid(row=1, column=0)
    city = StringVar(donation_records_window)
    city.set("Huntsville")
    cityEntry = OptionMenu(donation_records_window, city, "Huntsville", "Birmingham", "Madison")
    cityEntry.grid(row=1, column=1)

    validateDonationRecords = partial(show_donation_records,cal, city)

    show_records = Button(donation_records_window, text = "Show records",command=validateDonationRecords).grid(row=2,column=3)

