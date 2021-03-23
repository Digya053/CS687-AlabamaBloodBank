from tkinter import messagebox

from db_connection import connection
from user_interfaces.tables.treeview import TreeView

def check_availability(blood_type, age, weight, height, gender, quantity_in_ml):
    """
    Query to check availability of specific blood_type, age, weight, height, gender and quantity.
    """
    blood_type = blood_type.get()
    age = age.get()
    weight = weight.get()
    height = height.get()
    gender = gender.get()
    quantity_in_ml = quantity_in_ml.get()

    if blood_type !='':
        con = connection.Connection()
        query = "SELECT bs.blood_type, bs.quantity_in_ml, bs.storage_id, b.available_from, b.d_gender, b.d_weight, b.d_height, b.d_age FROM ALABAMA_BLOOD_STORAGE as bs, BLOOD as b WHERE b.storage_id = bs.storage_id AND bs.blood_type= '" + blood_type + "' AND b.d_gender= '" + gender + "' AND b.d_height>= " + str(height) + " AND b.d_weight>= " + str(weight) + " AND b.d_age<= " + str(age) + " AND b.storage_id = bs.storage_id AND bs.quantity_in_ml >= " + str(quantity_in_ml) + ";"
        con.execute_command(query)
        all_results = con.fetch_all()

        availability_results = []
        for result in all_results:
            availability_results.append(result)
        
        column_names = ("Blood Type", "Quantity", "StorageId", "Blood Available From", "Donor Gender", "Donor Weight", "Donor Height", "Donor Age")
        data = availability_results
        title = "Results of Blood Availability"
        tr = TreeView(column_names, data, title)
    else:
        messagebox.showerror("Error", "Blood Type is empty")
    return