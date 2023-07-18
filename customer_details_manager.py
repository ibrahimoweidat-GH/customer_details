"""
Customer Details Manager

Author: Ibrahim Oweidat
"""
import tkinter as tk
from tkinter import ttk
import menu_manager as mn

class CusDetForm:
    """
    Customer Details Form

    """

    def __init__(self, root, frame, db_manager):
        """
        Initialize a new instance of CusDetailsForm.

        Args:
            root: The root element of the GUI.
            frame: The frame element of the GUI.
            db_manager: database manager instance.

        Returns:
            None
        """
        try:
            self.db_manager = db_manager
            self.root = root
            self.root.geometry("900x400")
            self.root.title('Customer Details Application')
            self.frame = frame
            
            mn.MenuBar(self.root, self.frame, self.db_manager)

            self.details_frame = ttk.LabelFrame(self.frame, text="Imputs")
            self.details_frame.grid(row=0, column=0, padx=20, pady=10)

            self.cus_id = ttk.Entry(self.details_frame)
            self.cus_id.grid_forget()

            self.fname_value = tk.StringVar()
            self.fname_watermark = "First Name"
            self.fname = ttk.Entry(self.details_frame, textvariable=self.fname_value)
            self.fname.insert(0, self.fname_watermark)
            self.fname.bind("<FocusIn>", lambda e: self.fname.delete('0', 'end'))
            self.fname.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

            self.lname_value = tk.StringVar()
            self.lname_watermark = "Last Name"
            self.lname = ttk.Entry(self.details_frame, textvariable=self.lname_value)
            self.lname.insert(0, self.lname_watermark)
            self.lname.bind("<FocusIn>", lambda e: self.lname.delete('0', 'end'))
            self.lname.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

            self.sb_age_value = tk.StringVar()
            self.sb_ge_watermark = "Age"
            self.sb_age = ttk.Spinbox(self.details_frame, from_=18, to=100, \
                                      textvariable=self.sb_age_value)
            self.sb_age.insert(0, self.sb_ge_watermark)
            self.sb_age.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

            self.mstatus_value = tk.StringVar()
            self.mstatus_default = 0
            self.marital_status_list = ["Single", "Married", "Widowed", "Divorced"]
            self.mstatus = ttk.Combobox(self.details_frame, values=self.marital_status_list, \
                                        textvariable=self.mstatus_value)
            self.mstatus.current(self.mstatus_default)
            self.mstatus.grid(row=3, column=0, padx=5, pady=5,  sticky="ew")

            self.cb_employed_default = 0
            self.b_employed_value = tk.BooleanVar(value=self.cb_employed_default)
            self.cb_employed = ttk.Checkbutton(self.details_frame, text="Employed", \
                                               variable=self.b_employed_value)
            self.cb_employed.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

            self.separator = ttk.Separator(self.details_frame)
            self.separator.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

            self.bottom_frame = ttk.Frame(self.frame)
            self.bottom_frame.grid(row=1, column=0, padx=5, pady=5)

            self.btn_insert = ttk.Button(self.bottom_frame, text="Insert", command=self.insert_row)
            self.btn_insert.grid(row=0, column=0, padx=5, pady=5)

            self.btn_update = ttk.Button(self.bottom_frame, text="Update", command=self.update_row)
            self.btn_update.grid(row=0, column=0, padx=5, pady=5)
            self.btn_update.grid_remove()

            self.btn_clear = ttk.Button(self.bottom_frame, text="Clear", command=self.clear_data)
            self.btn_clear.grid(row=0, column=1, padx=5, pady=5)

            self.details_list_frame = ttk.Frame(self.frame)
            self.details_list_frame.grid(row=0, column=1, pady=10, rowspan=2)
            self.details_list_scroll = ttk.Scrollbar(self.details_list_frame)
            self.details_list_scroll.pack(side="right", fill="y")

            self.cols = ("id", "first_name", "last_name", "age", "marital_status", "employed")
            self.treeview = ttk.Treeview(self.details_list_frame, show="headings",
                                    yscrollcommand=self.details_list_scroll.set, \
                                        columns=self.cols, height=13)
            # Format columns
            self.treeview.column("id", width=50)
            self.treeview.column("first_name", width=100)
            self.treeview.column("last_name", width=100)
            self.treeview.column("age", width=50)
            self.treeview.column("marital_status", width=100)
            self.treeview.column("employed", width=100)

            # define headings                      
            self.treeview.heading('id', text='ID', anchor='w')
            self.treeview.heading('first_name', text='First Name', anchor='w')
            self.treeview.heading('last_name', text='Last Name', anchor='w')
            self.treeview.heading('age', text='Age', anchor='w')
            self.treeview.heading('marital_status', text='Marital Status', anchor='w')
            self.treeview.heading('employed', text='Employed', anchor='w')

            self.treeview.bind("<<TreeviewSelect>>", self.on_select)

            self.treeview.pack()
            self.details_list_scroll.config(command=self.treeview.yview)
            self.load_data()

        except Exception as ex:
            print(f"{__file__} - __init__() Error: {ex}")

    def on_select(self, event):
        """
        on select tree view row

        Args:
            event: The event that triggered the method call.

        Returns:
            None
        """
        try:
            if len(event.widget.selection()) != 0:
                self.reset_fields()
                selected_item = event.widget.selection()[0]
                item_data = event.widget.item(selected_item)

                clm_id = item_data["values"][0]
                clm_fname = item_data["values"][1]
                clm_lname = item_data["values"][2]
                clm_age = item_data["values"][3]
                clm_mstatus = item_data["values"][4]
                clm_employed = item_data["values"][5]

                self.cus_id.insert(0, clm_id)
                self.fname.insert(0, clm_fname)
                self.lname.insert(0, clm_lname)
                self.sb_age.insert(0, clm_age)
                self.mstatus.current(self.marital_status_list.index(clm_mstatus))
                self.b_employed_value.set((lambda x: True if x == 'Yes' else False)(clm_employed))

                self.fname.unbind("<FocusIn>")
                self.lname.unbind("<FocusIn>")
                self.btn_update.grid()
        except Exception as ex:
            print(f"{__file__} - on_select() Error: {ex}")

    def reset_fields(self):
        """
        reset form fields

        Args:
            None

        Returns:
            None
        """
        try:
            self.cus_id.delete('0', "end")
            self.fname.delete('0', "end")
            self.lname.delete('0', 'end')
            self.sb_age.delete('0', 'end')
            self.mstatus.delete('0', 'end')

            self.fname.bind("<FocusIn>", lambda e: self.fname.delete('0', 'end'))
            self.lname.bind("<FocusIn>", lambda e: self.lname.delete('0', 'end'))
            self.btn_insert.grid()
            self.btn_update.grid_remove()
        except Exception as ex:
            print(f"{__file__} - reset_fields() Error: {ex}")

    def insert_row(self):
        """
        insert new customer in database
        refresh treeview

        Args:
            None

        Returns:
            None
        """
        try:
            if self.validate_mandatory_fields():
                self.db_manager.insert_customer(self.fname_value.get(), self.lname_value.get(), \
                                               self.sb_age_value.get(), self.mstatus_value.get(), \
                                                int(self.b_employed_value.get()))
                self.load_data()
                self.reset_fields()
                self.set_default_fields_data()
        except Exception as ex:
            print(f"{__file__} - insert_row() Error: {ex}")

    def update_row(self):
        """
        update customer in database
        refresh treeview

        Args:
            None

        Returns:
            None
        """
        try:
            if self.validate_mandatory_fields():
                self.db_manager.update_customer(int(self.cus_id.get()), self.fname_value.get(), \
                                               self.lname_value.get(), self.sb_age_value.get(), \
                                                self.mstatus_value.get(), \
                                                    int(self.b_employed_value.get()))
                self.load_data()
                self.reset_fields()
                self.set_default_fields_data()
        except Exception as ex:
            print(f"{__file__} - update_row() Error: {ex}")

    def clear_data(self):
        """
        clear form fields data

        Args:
            None

        Returns:
            None
        """
        try:
            self.reset_fields()
            self.set_default_fields_data()
        except Exception as ex:
            print(f"{__file__} - clear_data() Error: {ex}")

    def set_default_fields_data(self):
        """
        set form fields watermark

        Args:
            None

        Returns:
            None
        """
        try:
            self.fname.insert(0, self.fname_watermark)  
            self.lname.insert(0, self.lname_watermark)
            self.sb_age.insert(0, self.sb_ge_watermark)
            self.mstatus.current(self.mstatus_default)
            self.b_employed_value.set(self.cb_employed_default)
        except Exception as ex:
            print(f"{__file__} - set_default_fields_data() Error: {ex}")

    def clear_treeview(self):
        """
        clear treview data

        Args:
            None

        Returns:
            None
        """
        try:
            for item in self.treeview.get_children():
                self.treeview.delete(item)
        except Exception as ex:
            print(f"{__file__} - clear_treeview() Error: {ex}")

    def load_data(self):
        """
        load customers data on treeview from database

        Args:
            None

        Returns:
            None
        """
        try:
            self.clear_treeview()
            all_customers = self.db_manager.get_customers()

            for customer in list(all_customers):
                self.treeview.insert('', tk.END, values=(customer[0], customer[1],
                                                    customer[2], customer[3],
                                                    customer[4], (lambda x: "Yes" if x else "No")(customer[5])))
        except Exception as ex:
            print(f"{__file__} - load_data() Error: {ex}")

    def validate_mandatory_fields(self):
        """
        validate mandatory fields on form

        Args:
            None

        Returns:
            None
        """
        try:
            if (not self.fname_value.get() or not self.lname_value.get() or \
                not self.sb_age_value.get() or \
                    self.fname_value.get() == self.fname_watermark or \
                        self.lname_value.get() == self.lname_watermark or \
                            self.sb_age_value.get() == self.sb_ge_watermark):
                return False
            return True
        except Exception as ex:
            print(f"{__file__} - validate_mandatory_fields() Error: {ex}")
