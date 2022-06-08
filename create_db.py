
from pathlib import Path
import sqlite3

# Used to create the database and all of it's assosciated fields


def check_out():
    if Path("./MAIN.db").exists():
        print("DB Already created")
    else:
        print("Creating DB")
        open("./MAIN.DB", "x")
        create_main()



def create_main():
    con = sqlite3.connect("./MAIN.DB")
    cur = con.cursor()
    cur.execute("""create table MAIN 
    (Name Text,
    Age Int,
    Gender Text,
    Active Bool,
    Type_of_contact Text,
    Problem Text,
    Solution Text,
    Device_type Text,
    Date_of_contact Text,
    Date_of_service Text,
    Difficulty Int,
    Payment Int)
    """)
    con.commit()
check_out()
