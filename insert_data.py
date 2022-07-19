import sqlite3
import tkinter.messagebox
from tkinter import messagebox
# Use uuid_gen() to create the unique ID


def add_data(name, age, gender, type_of_contact, contact_info, problem, solution, device_type, time_of_contact,
             date_of_contact, date_of_service, difficulty, payment, unique_id):
    con = sqlite3.connect("./MAIN.DB")
    cur = con.cursor()
    values = (name, age, gender, type_of_contact,
                        contact_info, problem, solution, device_type, time_of_contact, date_of_contact, date_of_service,
                        difficulty, payment, unique_id,)
    result = cur.execute("SELECT Problem FROM MAIN Where Unique_ID=?", (unique_id,))
    for x in result:
        print(x)
    if result.fetchone() != None:
        try:
            print("Unique ID.. proceeding")
            cur.execute("INSERT INTO MAIN VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (values))
            con.commit()
            tkinter.messagebox.Message("Data Entered Successfully")
        #except:
        #    tkinter.messagebox.showerror(message="Data input failiure")
        finally:
            print('done')
    else:
        print("Duplicate ID..")
        print(f'values: {values}')
        cur.execute("""UPDATE main SET
         Name=?,
         Age=?,
         Gender=?,
         Type_of_contact=?,
         Contact_info=?,
         Problem=?,
         Solution=?,
         Device_type=?,
         Time_of_contact=?,
         Date_of_contact=?,
         Date_of_service=?,
         Difficulty=?,
         Payment=?
         Where Unique_ID=?
         """, (values))
        con.commit()
        con.close()

