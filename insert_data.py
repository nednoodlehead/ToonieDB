import sqlite3
from main import uuid_gen
# Use uuid_gen() to create the unique ID


def add_data(name, age, gender, contact, contact_info, problem, solution, device_type, date_of_contact, date_of_service,
             difficulty, payment, id): #13
    con = sqlite3.connect("./MAIN.DB")
    cur = con.cursor()
    cur.execute("INSERT INTO {} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)".format(name, age, gender, contact, contact_info,
                                                                           problem, solution, device_type,
                                                                           date_of_contact, date_of_service,difficulty,
                                                                           payment, id))
    con.commit()


