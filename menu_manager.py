"""
Menu Bar Manager

Author: Ibrahim Oweidat
"""
import tkinter as tk
from tkinter import messagebox
import login_manager as lg

class MenuBar:
    """
    Menu Bar

    """

    def __init__(self, root, frame, db_manager):
        """
        Initialize a new instance of MenuBar.

        Args:
            root: The root element of the GUI.
            frame: The frame element of the GUI.
            db_manager: database manager instance.

        Returns:
            None
        """
        try:
            self.root = root
            self.frame = frame
            self.db_manager = db_manager

            self.menu_bar = tk.Menu(self.root)

            self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.file_menu.add_command(label='New')
            self.file_menu.add_command(label='Open')
            self.file_menu.add_separator()
            self.file_menu.add_command(label='Exit', command=self.close_window)

            self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.help_menu.add_command(label='About', command=self.about_window)

            self.menu_bar.add_cascade(label='File', menu=self.file_menu)
            self.menu_bar.add_cascade(label='Help', menu=self.help_menu)

            self.root.config(menu=self.menu_bar)
        except Exception as ex:
            print(f"{__file__} - __init__() Error: {ex}")

    def close_window(self):
        """
        close current window and navigate to login page

        Args:
            None

        Returns:
            None
        """
        try:
            self.db_manager.disconnect()

            self.frame.pack_forget()

            #self.menu_bar.unpost()
            self.root.config(menu="")

            log_frame = tk.Frame(self.root)
            lg.LoginForm(self.root, log_frame)
            log_frame.pack()
        except Exception as ex:
            print(f"{__file__} - close_window() Error: {ex}")

    def about_window(self):
        """
        About us window

        Args:
            None

        Returns:
            None
        """
        try:
            messagebox.showinfo("About", "Customer Details Application.")
        except Exception as ex:
            print(f"{__file__} - about_window() Error: {ex}")
