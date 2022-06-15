import sqlite3
import tkinter.messagebox
from tkinter import messagebox
# Use uuid_gen() to create the unique ID


def add_data(name, age, gender, type_of_contact, contact_info, problem, solution, device_type, time_of_contact,
             date_of_contact, date_of_service, difficulty, payment, unique_id):
    con = sqlite3.connect("./MAIN.DB")
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO MAIN VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (name, age, gender, type_of_contact,
                    contact_info, problem, solution, device_type, time_of_contact, date_of_contact, date_of_service,
                    difficulty, payment, unique_id,))
        con.commit()
        tkinter.messagebox.Message("Data Entered Successfully")
    except:
        tkinter.messagebox.showerror(message="Data input failiure")


