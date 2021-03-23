import tkinter as tk
from tkinter import *

from functools import partial
from queries.blood_request import check_availability

def show_availability(window):
    availability_window = tk.Toplevel(window)
    availability_window.title("Check Blood Availability")

    l = Label(availability_window, text = 'Please fill details about persion to be transfusioned.')

    blood_type = Label(availability_window, text="Blood Type*").grid(row=0, column=0)
    blood_type = StringVar()
    bloodtypeEntry = Entry(availability_window, textvariable=blood_type).grid(row=0, column=1)

    age = Label(availability_window, text="Age").grid(row=1, column=0)
    age = IntVar()
    ageEntry = Entry(availability_window, textvariable=age).grid(row=1, column=1)
    age.set(100)

    weight = Label(availability_window, text="Weight (lbs)").grid(row=2, column=0)
    weight = IntVar()
    weightEntry = Entry(availability_window, textvariable=weight).grid(row=2, column=1)

    height = Label(availability_window, text="Height (lbs)").grid(row=3, column=0)
    height = IntVar()
    heightEntry = Entry(availability_window, textvariable=height).grid(row=3, column=1)

    gender = Label(availability_window, text="Gender*").grid(row=4, column=0)
    gender = StringVar()
    genderEntry = Entry(availability_window, textvariable=gender).grid(row=4, column=1)

    quantity = Label(availability_window, text="Quantity Required (mL)").grid(row=5, column=0)
    quantity = IntVar()
    quantityEntry = Entry(availability_window, textvariable=quantity).grid(row=5, column=1)

    validate_check = partial(check_availability,blood_type, age, weight, height, gender, quantity)

    check_blood = tk.Button(availability_window, text = "Check Availability", command=validate_check).grid(row=6, column=3)

    availability_window.mainloop