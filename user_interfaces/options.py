from user_interfaces.windows.blood_request import show_availability
from user_interfaces.windows.delete_event import delete_scheduled_events
from user_interfaces.windows.donation_records import view_donation_records
from user_interfaces.windows.organizer_details import organizer_details
from user_interfaces.windows.new_event import add_new_event
from user_interfaces.windows.display_scheduled_events import display_saved_events

from queries.donate_blood import donate
from queries.blood_request_records import request_records
from queries.upcoming_events import upcoming_events
from queries.past_events import past_events

import tkinter as tk
from functools import partial


def view_options(window):

    """
    Creates UI for Options Page after Login.
    """
    
    options_window = tk.Toplevel(window)
    options_window.title("Options")

    window_show_availability = partial(show_availability, window)
    window_schedule_blood_donation = partial(donate, window)
    window_show_scheduled_blood_donation = partial(display_saved_events, window)
    window_delete_scheduled_blood_donation = partial(delete_scheduled_events, window)
    window_view_donation_records = partial(view_donation_records, window)
    window_view_organizer_details = partial(organizer_details, window)
    window_add_new_event = partial(add_new_event, window)

    button1 = tk.Button(options_window, text = "Blood Request", height=3, width=40, command=window_show_availability)
    button1.place(x=500, y=100)
    button2 = tk.Button(options_window, text = "Schedule Blood Donation", height=3, width=40, command=window_schedule_blood_donation)
    button2.place(x=500, y=158)
    button3 = tk.Button(options_window, text = "Show Scheduled Blood Donation", height=3, width=40, command=window_show_scheduled_blood_donation)
    button3.place(x=500, y=216)
    button4 = tk.Button(options_window, text = "Delete Scheduled Blood Donation", height=3, width=40, command=window_delete_scheduled_blood_donation)
    button4.place(x=500, y=274)
    button5 = tk.Button(options_window, text = "View Donation Records", height=3, width=40, command=window_view_donation_records)
    button5.place(x=500, y=332)
    button6 = tk.Button(options_window, text = "View Supplied Blood Requests Records", height=3, width=40, command=request_records)
    button6.place(x=500, y=390)
    button7 = tk.Button(options_window, text = "View Organizer", height=3, width=40, command=window_view_organizer_details)
    button7.place(x=500, y=448)
    button8 = tk.Button(options_window, text = "View Upcoming Blood Donation Events", height=3, width=40, command=upcoming_events)
    button8.place(x=500, y=506)
    button9 = tk.Button(options_window, text = "View Past Blood Donation Events", height=3, width=40, command=past_events)
    button9.place(x=500, y=564)
    button10 = tk.Button(options_window, text = "Add New Event", height=3, width=40, command=window_add_new_event)
    button10.place(x=500, y=622)

    options_window.mainloop