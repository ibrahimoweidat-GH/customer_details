"""
Login Manager

Author: Ibrahim Oweidat
"""
import tkinter as tk
from tkinter import ttk
import customer_details_manager as cd
import db_manager as db

class LoginForm:
    """
    Login Form

    """

    def __init__(self, root, frame):
        """
        Initialize a new instance of LoginForm.

        Args:
            root: The root element of the GUI.
            frame: The frame element of the GUI.

        Returns:
            None
        """
        try:
            self.root = root
            self.root.geometry("300x200")
            self.root.title('Login')
            self.frame = frame

            self.lbl_username = ttk.Label(self.frame, text="Username:")
            self.lbl_username.grid(row=0, column=0, padx=5, pady=(40, 5), sticky='ew')

            self.ey_username_value = tk.StringVar()
            self.ey_username_watermark = "User Name"
            self.ey_username = ttk.Entry(self.frame, textvariable=self.ey_username_value)
            self.ey_username.insert(0, self.ey_username_watermark)
            self.ey_username.bind("<FocusIn>", lambda e: self.ey_username.delete('0', 'end'))
            self.ey_username.grid(row=0, column=1, padx=5, pady=(40, 5), sticky='ew')

            self.lbl_password = ttk.Label(self.frame, text="Password:")
            self.lbl_password.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

            self.ey_password_value = tk.StringVar()
            self.ey_password_watermark = "Password"
            self.ey_password = ttk.Entry(self.frame, textvariable=self.ey_password_value)
            self.ey_password.insert(0, self.ey_password_watermark)
            self.ey_password.bind("<FocusIn>", lambda e: self.ey_password.delete('0', 'end'))
            self.ey_password.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

            self.btn_login = ttk.Button(self.frame, text="Login", command=self.login)
            self.btn_login.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

            self.lbl_notification = ttk.Label(self.frame, foreground="red")
            self.lbl_notification.bind('<Configure>', \
                                       lambda e: self.lbl_notification.config \
                                        (wraplength=self.lbl_notification.winfo_width()))
            self.lbl_notification.grid(row=3, columnspan=2, padx=5, pady=5, sticky='nsew')

        except Exception as ex:
            print(f"{__file__} - __init__() Error: {ex}")

    def open_customer_details_form(self, db_manager):
        """
        to open customer details form

        Args:
            None
        
        Returns:
            None
        """
        try:
            self.frame.pack_forget()
            cusdetails_frame = tk.Frame(self.root)
            cd.CusDetForm(self.root, cusdetails_frame, db_manager)
            cusdetails_frame.pack()
        except Exception as ex:
            print(f"{__file__} - open_customer_details_form() Error: {ex}")

    def login(self):
        """
        this method will check the credentials and login if username and password are true

        Args:
            None
        
        Returns:
            None
        """
        try:
            if self.validate_credentials():
                db_manager = db.DB()

                # Check user if exists
                user_details = db_manager.check_user(self.ey_username_value.get(),  \
                                                    self.ey_password_value.get())
                if not user_details:
                    self.lbl_notification.config(text = "User is not registered in the system")
                    return

                # Update first login date
                if user_details[3] is None:
                    db_manager.update_first_login(int(user_details[0]))

                # Update last login date
                db_manager.update_last_login(int(user_details[0]))

                #Open customer details form
                self.open_customer_details_form(db_manager)

            else:
                self.lbl_notification.config(text = "Username and Password are mandatory")

        except Exception as ex:
            print(f"{__file__} - login() Error: {ex}")

    def validate_credentials(self):
        """
        this method to validate credentials

        Args:
            None
        
        Returns:
            false if username and password are incorrect, otherwise true 
        """
        try:
            if not self.ey_username_value.get() or not self.ey_password_value.get() or \
                self.ey_username_value.get() == self.ey_username_watermark or \
                    self.ey_password_value.get() == self.ey_password_watermark:
                return False

            return True
        except Exception as ex:
            print(f"{__file__} - validate_credentials() Error: {ex}")
