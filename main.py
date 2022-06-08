# import sqlite3
import tkinter as tk
from tkinter import ttk

# Settings for the app
root = tk.Tk()
root.geometry("825x700+250+100")
root.title("ToonieDB")
root.resizable(False, False)

# Defining the style for the two tkinter frames
main_style = ttk.Style()
main_style.configure("TFrame", background="#656489")


master_notebook = ttk.Notebook(root)
view_data_frame = ttk.Frame(master_notebook, width=825, height=700, style='TFrame')
add_data_frame = ttk.Frame(master_notebook, width=825, height=700, style='TFrame')
add_data_frame.pack(fill='both', expand=True)
master_notebook.pack()
master_notebook.add(add_data_frame, text="Add Data")
master_notebook.add(view_data_frame, text="View Data")
view_data_frame.configure()

# Variables that ttk.Entry & tk.Text outputs to. Defined as data_var.

name_var = tk.StringVar()
age_var = tk.IntVar()
gender_var = tk.StringVar()
contact_type_var = tk.StringVar()
device_type_var = tk.StringVar()
date_of_service_var = tk.StringVar()
date_of_contact_var = tk.StringVar()
time_of_contact_var = tk.StringVar()
difficulty_var = tk.StringVar()
payment_var = tk.StringVar()


# Labels and Input boxes for Data with (snake_case) format data_label or data_entry

name_label = ttk.Label(add_data_frame, text="Name:")
name_entry = ttk.Entry(add_data_frame, textvariable=name_var)

age_label = ttk.Label(add_data_frame, text="Age")
age_entry = ttk.Entry(add_data_frame, textvariable=age_var)

gender_label = ttk.Label(add_data_frame, text="Gender")
gender_entry = ttk.Entry(add_data_frame, textvariable=gender_var)

contact_type_label = ttk.Label(add_data_frame, text="Contact Type:")
contact_type_entry = ttk.Entry(add_data_frame, textvariable=contact_type_var)

problem_label = ttk.Label(add_data_frame, text="Problem:")
# tk.Text needed because ttk.Entry cannot support multiple lines
problem_entry = tk.Text(add_data_frame, width=50, height=5, font=("Arial", 10))

# tk.Text cannot map to a StringVar() so the output is down here :)
problem_var = problem_entry.get('1.0', 'end')

solution_label = ttk.Label(add_data_frame, text="Solution:")
solution_entry = tk.Text(add_data_frame, width=50, height=5, font=("Arial", 10))

solution_var = problem_entry.get('1.0', 'end')

device_type_label = ttk.Label(add_data_frame, text="Device Type:")
device_type_entry = ttk.Entry(add_data_frame, textvariable=device_type_var)

date_of_service_label = ttk.Label(add_data_frame, text="Date of service: (YY/MM/DD)")
date_of_service_entry = ttk.Entry(add_data_frame, textvariable=date_of_service_var)

date_of_contact_label = ttk.Label(add_data_frame, text="Date of Contact: (YY/MM/DD)")
date_of_contact_entry = ttk.Entry(add_data_frame, textvariable=date_of_contact_var)

time_of_contact_label = ttk.Label(add_data_frame, text="Time of contact:")
time_of_contact_entry = ttk.Entry(add_data_frame, textvariable=time_of_contact_var)

difficulty_label = ttk.Label(add_data_frame, text="Difficulty")
difficulty_entry = ttk.Entry(add_data_frame, textvariable=difficulty_var)

payment_label = ttk.Label(add_data_frame, text="Payment")
payment_entry = ttk.Entry(add_data_frame, textvariable=payment_var)

# Placing all the Widgets & Labels






























root.mainloop()
