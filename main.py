"""
the main script to run the application

Author: Ibrahim Oweidat
"""
import tkinter as tk
from tkinter import ttk
import login_manager as lg

def run():
    """
    Generate basic tkinter object
    Call forest light theme
    open Login Form

    Args:
        None

    Returns:
        None
    """
    try:
        # Create the main window
        root = tk.Tk()
        style = ttk.Style(root)
        root.tk.call("source", "forest-light.tcl")
        style.theme_use("forest-light")

        main_frame = tk.Frame(root)
        main_frame.pack()

        lg.LoginForm(root, main_frame)

        root.mainloop()
    except Exception as ex:
        print(f"{__file__} - Main() Error: {ex}")

if __name__ == '__main__':
    run()
