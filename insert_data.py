import sqlite3
import tkinter.messagebox
from tkinter import messagebox
from main import uuid_gen
# Use uuid_gen() to create the unique ID


def add_data(name, age, gender, contact_type, contact_info, problem, solution, device_type, time_of_contact,
             date_of_contact, date_of_service,
             difficulty, payment, id): #13
    con = sqlite3.connect("./MAIN.DB")
    cur = con.cursor()
    cur.execute("INSERT INTO {} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)".format(name, age, gender, contact_type,
                                                                           contact_info, problem, solution, device_type,
                                                                           time_of_contact, date_of_contact,
                                                                           date_of_service, difficulty, payment, id))
    con.commit()
    tkinter.messagebox.Message("Data Entered Successfully")


