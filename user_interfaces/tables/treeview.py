from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.ttk import Treeview, Scrollbar

class TreeView:
    """
    Constructs table.
    """
    def __init__(self, columns, data, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("500x500")
        self.columns = tuple(columns)

        self.my_tree = ttk.Treeview(self.root)
        self.my_tree['columns'] = self.columns
        self.my_tree.column("#0", width=0, stretch=NO)
        
        for i in columns:
            self.my_tree.column(i, stretch=tk.YES)

        self.my_tree.heading("#0", text="")
        for i in columns:
            self.my_tree.heading(i, text=i)

        id=0
        self.data = data
        for d in self.data:
            self.my_tree.insert(parent='',index='end', text="",iid=id, values=d)
            id=id+1

        self.my_tree.pack(pady=20)

        # vsb = Scrollbar(self.root, orient="vertical", command=self.my_tree.yview)
        # vsb.place(relx=0.978, rely=0.175, relheight=0.713, relwidth=0.020)

        hsb = Scrollbar(self.root, orient="horizontal", command=self.my_tree.xview)
        hsb.place(relx=0.014, rely=0.875, relheight=0.020, relwidth=0.965)

        #self.my_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.my_tree.configure(xscrollcommand=hsb.set)

        self.root.mainloop()