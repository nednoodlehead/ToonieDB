import tkinter as tk
from tkinter import ttk
import uuid
from tkinter import messagebox
from insert_data import add_data

# Settings for the app
root = tk.Tk()
root.geometry("825x700+250+100")
root.title("ToonieDB")
root.resizable(False, False)

# Defining the style for the two tkinter frames & checkboxes
main_style = ttk.Style()
main_style.configure("TFrame", background="#656489")
checkbox_style = ttk.Style()
checkbox_style.configure("default.TCheckbutton", background="#656489")

master_notebook = ttk.Notebook(root)
view_data_frame = ttk.Frame(master_notebook, width=825, height=700, style='TFrame')
add_data_frame = ttk.Frame(master_notebook, width=825, height=700, style='TFrame')
add_data_frame.pack(fill='both', expand=True)
master_notebook.pack()
master_notebook.add(add_data_frame, text="Add Data")
master_notebook.add(view_data_frame, text="View Data")


# Good'ol Functions. Checks for invalid inputs / cleans up poor inputs

def name_check(name):
    to_return = ""
    for i in range(len(name)):
        if i == 0:
            to_return += name[i].upper()
        else:
            to_return += name[i].lower()
    return to_return


def uuid_gen():
    return str(uuid.uuid4())


def null_check():
    # Perhaps in the future this should have 'smarter' checking. CHeck for stuff that isn't just null
    # solution and problem don't have .get() because they are just assignments to strings that exist
    # list_of_error used to return all keys of values that failed to be entered
    list_of_error = []
    failed_bool = False
    list_of_data = {
        "Name Field": name_var.get(),
        "Age Field": age_var.get(),
        "Gender Field": gender_check(),  #prolem
        "Contact Type Field": contact_type_check(),
        "Contact Info Field": contact_info_var.get(),
        "Problem Field": problem_entry.get('1.0', 'end-1c'),
        "Solution Field": solution_entry.get('1.0', 'end-1c'),
        "Device Type Field": device_type_check(),  #probl
        "Time of Contact": time_of_contact_var.get(),
        "Date of Contact Field": date_of_contact_var.get(),
        "Date of Service Field": date_of_service_var.get(),
        "Difficulty Field": difficulty_var.get(),
        "Payment Field": payment_var.get(),
        "Should never fail": uuid_gen()
    }
    # Creates a list of entries that were missed
    for entry in list_of_data.items():
        if entry[1] == '':
            failed_bool = True
            list_of_error.append(entry[0])
        print(f"entry: {entry[1]}")
    if failed_bool is True:
        tk.messagebox.showerror(message=f"Data missing ! \n{list_of_error}")
    else:
        print("Full data, moving to process...")
        print(f'All data: {list_of_data.values()}')
        name_entry.delete(0, 'end')
        age_entry.delete(0, 'end')

        gender_entry_male.state(["!selected", "focus"])
        gender_entry_female.state(["!selected", "focus"])
        gender_entry_other.state(["!selected", "focus"])

        contact_info_entry.delete(0, 'end')

        contact_type_entry_facebook.state(["!selected", "focus"])
        contact_type_entry_email.state(["!selected", "focus"])
        contact_type_entry_call.state(["!selected", "focus"])

        problem_entry.delete("1.0", 'end')
        solution_entry.delete("1.0", 'end')

        device_type_entry_desktop.state(["!selected", "focus"])
        device_type_entry_phone.state(["!selected", "focus"])
        device_type_entry_laptop.state(["!selected", "focus"])

        date_of_contact_entry.delete(0, 'end')
        date_of_service_entry.delete(0, 'end')
        difficulty_entry.delete(0, 'end')
        payment_entry.delete(0, 'end')
        count = 0
        input_data = list(list_of_data.values())
        print(count)
        add_data(input_data[0], input_data[1], input_data[2], input_data[3], input_data[4], input_data[5], input_data[6]
                 , input_data[7], input_data[8], input_data[9], input_data[10], input_data[11], input_data[12],
                 uuid_gen())


def gender_check():
    return_str = ''
    sum_check = []
    check_list = [
        gender_entry_male_var.get(),
        gender_entry_female_var.get(),
        gender_entry_other_var.get()
    ]
    for item in check_list:
        if item != "":
            return_str = item
            sum_check.append(item)
    return return_str


def contact_type_check():
    return_str = ''
    sum_check = []
    check_list = [
        is_facebook.get(),
        is_call.get(),
        is_email.get()
    ]
    for item in check_list:
        if item != "":
            return_str = item
            sum_check.append(item)
    return return_str


def device_type_check():
    return_str = ''
    sum_check = []
    check_list = [
        is_desktop.get(),
        is_phone.get(),
        is_laptop.get(),
        device_type_var.get()
    ]
    for item in check_list:
        if item != "":
            return_str = item
            sum_check.append(item)
    if len(sum_check) != 1:
        pass
        # tk.messagebox.showerror(message='You need to have to have a valid # of values for Contact Type')
    else:
        return return_str


tk.Button(add_data_frame, text="TEst for contact type", command=contact_type_check).place(x=200, y=200)
tk.Button(add_data_frame, text="Test for device type", command=device_type_check).place(x=200, y=240)
tk.Button(add_data_frame, text="Test for null data", command=null_check).place(x=500, y=500)
# Variables that ttk.Entry & tk.Text outputs to. Defined as data_var.
# Must have some type of function to sort through the checkboxes and detirmines which has value. and use it

name_var = tk.StringVar()
age_var = tk.StringVar()

gender_entry_male_var = tk.StringVar()
gender_entry_female_var = tk.StringVar()
gender_entry_other_var = tk.StringVar()

device_type_var = tk.StringVar()
date_of_service_var = tk.StringVar()
date_of_contact_var = tk.StringVar()
contact_info_var = tk.StringVar()
contact_info_var.set("Email@Gmail")
time_of_contact_var = tk.StringVar()
difficulty_var = tk.StringVar()
payment_var = tk.StringVar()
# Separating similar fields. Below is Contact type. Below that is device type
is_facebook = tk.StringVar()
is_email = tk.StringVar()
is_call = tk.StringVar()

is_desktop = tk.StringVar()
is_phone = tk.StringVar()
is_laptop = tk.StringVar()

# Labels and Input boxes for Data with (snake_case) format data_label or data_entry

name_label = ttk.Label(add_data_frame, text="Name:")
name_entry = ttk.Entry(add_data_frame, textvariable=name_var)

age_label = ttk.Label(add_data_frame, text="Age")
age_entry = ttk.Entry(add_data_frame, textvariable=age_var)
# Default value is '0'. .delete() gets rid of that. It has no proper purpose
age_entry.delete("0")

gender_label = ttk.Label(add_data_frame, text="Male         Female        Other")

# Unsure if not adding an offvalue= implies 'NoneType'. Which is what i want. Leaving for now
gender_entry_male = ttk.Checkbutton(add_data_frame, onvalue="Male", style="default.TCheckbutton",
                                    variable=gender_entry_male_var)
gender_entry_female = ttk.Checkbutton(add_data_frame, onvalue="Female", style="default.TCheckbutton",
                                      variable=gender_entry_female_var)
gender_entry_other = ttk.Checkbutton(add_data_frame, onvalue="Other", style="default.TCheckbutton",
                                     variable=gender_entry_other_var)

# Clears the boxes of the weird default state. To an unchecked state
gender_entry_male.state(["!selected", "focus"])
gender_entry_female.state(["!selected", "focus"])
gender_entry_other.state(["!selected", "focus"])

contact_type_label = ttk.Label(add_data_frame, text="Contact Info & Type:")
contact_info_entry = ttk.Entry(add_data_frame, textvariable=contact_info_var)
contact_type_info = ttk.Label(add_data_frame, text="FaceBook    Email     Call  ")
contact_type_entry_facebook = ttk.Checkbutton(add_data_frame, offvalue="", onvalue="FaceBook",
                                              style="default.TCheckbutton", variable=is_facebook)
contact_type_entry_email = ttk.Checkbutton(add_data_frame, offvalue="", onvalue="Email", style="default.TCheckbutton",
                                           variable=is_email)
contact_type_entry_call = ttk.Checkbutton(add_data_frame, offvalue="", onvalue="Call", style="default.TCheckbutton",
                                          variable=is_call)

contact_type_entry_facebook.state(["!selected", "focus"])
contact_type_entry_email.state(["!selected", "focus"])
contact_type_entry_call.state(["!selected", "focus"])

problem_label = ttk.Label(add_data_frame, text="Problem:")
# tk.Text needed because ttk.Entry cannot support multiple lines
problem_entry = tk.Text(add_data_frame, width=40, height=5, font=("Arial", 10))

# tk.Text cannot map to a StringVar() so the output is down here :)
problem_var = problem_entry.get('1.0', 'end-1c')

solution_label = ttk.Label(add_data_frame, text="Solution:")
solution_entry = tk.Text(add_data_frame, width=40, height=5, font=("Arial", 10))

solution_var = solution_entry.get('1.0', 'end-1c')


device_type_label = ttk.Label(add_data_frame, text="Desktop    Phone    Laptop")
device_type_label_other = ttk.Label(add_data_frame, text="Other?")
device_type_entry_desktop = ttk.Checkbutton(add_data_frame, onvalue="Desktop", style="default.TCheckbutton",
                                            variable=is_desktop, offvalue="")
device_type_entry_phone = ttk.Checkbutton(add_data_frame, onvalue="Phone", style="default.TCheckbutton",
                                          variable=is_phone, offvalue="")
device_type_entry_laptop = ttk.Checkbutton(add_data_frame, onvalue="Laptop", style="default.TCheckbutton",
                                           variable=is_laptop, offvalue="")
device_type_entry_other = ttk.Entry(add_data_frame, textvariable=device_type_var)

device_type_entry_desktop.state(["!selected", "focus"])
device_type_entry_phone.state(["!selected", "focus"])
device_type_entry_laptop.state(["!selected", "focus"])

date_of_service_label = ttk.Label(add_data_frame, text="Date of service: (YY/MM/DD)")
date_of_service_entry = ttk.Entry(add_data_frame, textvariable=date_of_service_var)

date_of_contact_label = ttk.Label(add_data_frame, text="Date of Contact: (YY/MM/DD)")
date_of_contact_entry = ttk.Entry(add_data_frame, textvariable=date_of_contact_var)

time_of_contact_label = ttk.Label(add_data_frame, text="Time of contact: (8PM)")
time_of_contact_entry = ttk.Entry(add_data_frame, textvariable=time_of_contact_var)

difficulty_label = ttk.Label(add_data_frame, text="Difficulty (1-10)")
difficulty_entry = ttk.Entry(add_data_frame, textvariable=difficulty_var)

payment_label = ttk.Label(add_data_frame, text="Payment (8) as in 8 dollars")
payment_entry = ttk.Entry(add_data_frame, textvariable=payment_var)

# Placing all the Widgets & Labels

name_label.place(x=20, y=20)
name_entry.place(x=20, y=40)

age_label.place(x=20, y=80)
age_entry.place(x=20, y=100)

gender_label.place(x=20, y=140)
gender_entry_male.place(x=30, y=160)
gender_entry_female.place(x=85, y=160)
gender_entry_other.place(x=140, y=160)

contact_type_label.place(x=20, y=180)
contact_type_info.place(x=20, y=200)
contact_type_entry_facebook.place(x=30, y=220)
contact_type_entry_email.place(x=85, y=220)
contact_type_entry_call.place(x=140, y=220)
contact_info_entry.place(x=20, y=240)

problem_label.place(x=450, y=20)
problem_entry.place(x=450, y=40)

solution_label.place(x=450, y=130)
solution_entry.place(x=450, y=150)

device_type_label.place(x=20, y=280)
device_type_label_other.place(x=160, y=300)
device_type_entry_desktop.place(x=30, y=300)
device_type_entry_phone.place(x=85, y=300)
device_type_entry_laptop.place(x=140, y=300)
device_type_entry_other.place(x=20, y=320)

date_of_service_label.place(x=20, y=360)
date_of_service_entry.place(x=20, y=380)

date_of_contact_label.place(x=20, y=420)
date_of_contact_entry.place(x=20, y=440)

time_of_contact_label.place(x=20, y=480)
time_of_contact_entry.place(x=20, y=500)

difficulty_label.place(x=20, y=540)
difficulty_entry.place(x=20, y=560)

payment_label.place(x=20, y=600)
payment_entry.place(x=20, y=620)

root.mainloop()
