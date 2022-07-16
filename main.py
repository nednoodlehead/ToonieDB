import sqlite3
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import uuid
from tkinter import messagebox
from insert_data import add_data
from tkinter.messagebox import Message

# Settings for the app
class main_logic(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1400x700+250+100")
        self.title("ToonieDB")
        self.resizable(False, False)
        # used to transfer the data from the view_data to addingdata class
        self.transfer = {
            "Name Field": None,
            "Age Field": None,
            "Gender Field": None,
            "Contact Type Field": None,
            "Contact Info Field": None,
            "Problem Field": None,
            "Solution Field": None,
            "Device Type Field": None,
            "Time of Contact": None,
            "Date of Contact Field": None,
            "Date of Service Field": None,
            "Difficulty Field": None,
            "Payment Field": None,
            "Uniqueid": None
        }
        # Defining the style for the two tkinter frames & checkboxes
        main_style = ttk.Style()
        main_style.configure("TFrame", background="#656489")
        checkbox_style = ttk.Style()
        checkbox_style.configure("default.TCheckbutton", background="#656489")
        main_page_frame = tk.Frame(self)
        main_page_frame.pack(side="top", fill="both", expand=True)
        main_page_frame.grid_rowconfigure(0, weight=1)
        main_page_frame.grid_columnconfigure(0, weight=1)
        frame_style = ttk.Style()
        frame_style.configure('TFrame', background='#262626')
        bottom_frame = ttk.Frame(self, style='TFrame', height=100, width=1400)
        bottom_frame.place(x=0, y=600)
        add_data_button = ttk.Button(bottom_frame, text="Add Data", command=lambda: self.show_frame(AddingData))
        add_data_button.place(x=0, y=0)
        view_data_button = ttk.Button(bottom_frame, text="View Data", command=lambda: self.show_frame(view_data))
        view_data_button.place(x=80, y=0)
        self.frames = {}
        for each_frame in (view_data, AddingData):
            frame = each_frame(main_page_frame, self)
            self.frames[each_frame] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(AddingData)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.event_generate("<<ShowFrame>>")
        frame.tkraise()

    def create_event(self):
        print("Creating event!")
        frame = self.frames[AddingData]
        frame.event_generate("<<INCOMING>>")
        frame.tkraise()


# Good'ol Functions. Checks for invalid inputs / cleans up poor inputs
class AddingData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#656489")

        tk.Button(self, text="Enter Data!", command=self.null_check).place(x=500, y=500)
        # Variables that ttk.Entry & tk.Text outputs to. Defined as data_var.
        # Must have some type of function to sort through the checkboxes and detirmines which has value. and use it

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()

        self.gender_entry_male_var = tk.StringVar()
        self.gender_entry_female_var = tk.StringVar()
        self.gender_entry_other_var = tk.StringVar()

        self.device_type_var = tk.StringVar()
        self.date_of_service_var = tk.StringVar()
        self.date_of_contact_var = tk.StringVar()
        self.contact_info_var = tk.StringVar()
        self.contact_info_var.set("Email@Gmail")
        self.time_of_contact_var = tk.StringVar()
        self.difficulty_var = tk.StringVar()
        self.payment_var = tk.StringVar()
        self.uniqueid_var = tk.StringVar()
        # Separating similar fields. Below is Contact type. Below that is device type
        self.is_facebook = tk.StringVar()
        self.is_email = tk.StringVar()
        self.is_call = tk.StringVar()

        self.is_desktop = tk.StringVar()
        self.is_phone = tk.StringVar()
        self.is_laptop = tk.StringVar()

        # Labels and Input boxes for Data with (snake_case) format data_label or data_entry

        self.name_label = ttk.Label(self, text="Name:")
        self.name_entry = ttk.Entry(self, textvariable=self.name_var)

        self.age_label = ttk.Label(self, text="Age")
        self.age_entry = ttk.Entry(self, textvariable=self.age_var)
        # Default value is '0'. .delete() gets rid of that. It has no proper purpose
        self.age_entry.delete("0")

        self.gender_label = ttk.Label(self, text="Male         Female        Other")

        # Unsure if not adding an offvalue= implies 'NoneType'. Which is what i want. Leaving for now
        self.gender_entry_male = ttk.Checkbutton(self, onvalue="Male", style="default.TCheckbutton",
                                            variable=self.gender_entry_male_var)
        self.gender_entry_female = ttk.Checkbutton(self, onvalue="Female", style="default.TCheckbutton",
                                              variable=self.gender_entry_female_var)
        self.gender_entry_other = ttk.Checkbutton(self, onvalue="Other", style="default.TCheckbutton",
                                              variable=self.gender_entry_other_var)

         # Clears the boxes of the weird default state. To an unchecked state
        self.gender_entry_male.state(["!selected", "focus"])
        self.gender_entry_female.state(["!selected", "focus"])
        self.gender_entry_other.state(["!selected", "focus"])

        self.contact_type_label = ttk.Label(self, text="Contact Info & Type:")
        self.contact_info_entry = ttk.Entry(self, textvariable=self.contact_info_var)
        self.contact_type_info = ttk.Label(self, text="FaceBook    Email     Call  ")
        self.contact_type_entry_facebook = ttk.Checkbutton(self, offvalue="", onvalue="FaceBook",
                                                      style="default.TCheckbutton", variable=self.is_facebook)
        self.contact_type_entry_email = ttk.Checkbutton(self, offvalue="", onvalue="Email",
                                                   style="default.TCheckbutton",
                                                   variable=self.is_email)
        self.contact_type_entry_call = ttk.Checkbutton(self, offvalue="", onvalue="Call",
                                                  style="default.TCheckbutton",
                                                  variable=self.is_call)

        self.contact_type_entry_facebook.state(["!selected", "focus"])
        self.contact_type_entry_email.state(["!selected", "focus"])
        self.contact_type_entry_call.state(["!selected", "focus"])

        self.problem_label = ttk.Label(self, text="Problem:")
        # tk.Text needed because ttk.Entry cannot support multiple lines
        self.problem_entry = tk.Text(self, width=40, height=5, font=("Arial", 10))

        # tk.Text cannot map to a StringVar() so the output is down here :)
        self.problem_var = self.problem_entry.get('1.0', 'end-1c')

        self.solution_label = ttk.Label(self, text="Solution:")
        self.solution_entry = tk.Text(self, width=40, height=5, font=("Arial", 10))

        self.solution_var = self.solution_entry.get('1.0', 'end-1c')

        self.device_type_label = ttk.Label(self, text="Desktop    Phone    Laptop")
        self.device_type_label_other = ttk.Label(self, text="Other?")
        self.device_type_entry_desktop = ttk.Checkbutton(self, onvalue="Desktop", style="default.TCheckbutton",
                                                    variable=self.is_desktop, offvalue="")
        self.device_type_entry_phone = ttk.Checkbutton(self, onvalue="Phone", style="default.TCheckbutton",
                                                  variable=self.is_phone, offvalue="")
        self.device_type_entry_laptop = ttk.Checkbutton(self, onvalue="Laptop", style="default.TCheckbutton",
                                                   variable=self.is_laptop, offvalue="")
        self.device_type_entry_other = ttk.Entry(self, textvariable=self.device_type_var)

        self.device_type_entry_desktop.state(["!selected", "focus"])
        self.device_type_entry_phone.state(["!selected", "focus"])
        self.device_type_entry_laptop.state(["!selected", "focus"])

        self.date_of_service_label = ttk.Label(self, text="Date of service: (YY/MM/DD)")
        self.date_of_service_entry = ttk.Entry(self, textvariable=self.date_of_service_var)

        self.date_of_contact_label = ttk.Label(self, text="Date of Contact: (YY/MM/DD)")
        self.date_of_contact_entry = ttk.Entry(self, textvariable=self.date_of_contact_var)

        self.time_of_contact_label = ttk.Label(self, text="Time of contact: (8PM)")
        self.time_of_contact_entry = ttk.Entry(self, textvariable=self.time_of_contact_var)

        self.difficulty_label = ttk.Label(self, text="Difficulty (1-10)")
        self.difficulty_entry = ttk.Entry(self, textvariable=self.difficulty_var)

        self.payment_label = ttk.Label(self, text="Payment (8) as in 8 dollars")
        self.payment_entry = ttk.Entry(self, textvariable=self.payment_var)

        self.uniqueid_label = ttk.Label(self, text="Uniqueid (Unchangeable)")
        self.uniqueid_entry = ttk.Entry(self, textvariable=self.uniqueid_var, state="disabled", width=35)

        # Placing all the Widgets & Labels

        self.name_label.place(x=20, y=20)
        self.name_entry.place(x=20, y=40)

        self.age_label.place(x=20, y=80)
        self.age_entry.place(x=20, y=100)

        self.gender_label.place(x=20, y=140)
        self.gender_entry_male.place(x=30, y=160)
        self.gender_entry_female.place(x=85, y=160)
        self.gender_entry_other.place(x=140, y=160)

        self.contact_type_label.place(x=20, y=180)
        self.contact_type_info.place(x=20, y=200)
        self.contact_type_entry_facebook.place(x=30, y=220)
        self.contact_type_entry_email.place(x=85, y=220)
        self.contact_type_entry_call.place(x=140, y=220)
        self.contact_info_entry.place(x=20, y=240)

        self.problem_label.place(x=450, y=20)
        self.problem_entry.place(x=450, y=40)

        self.solution_label.place(x=450, y=130)
        self.solution_entry.place(x=450, y=150)

        self.uniqueid_label.place(x=450, y=240)
        self.uniqueid_entry.place(x=450, y=270)

        self.device_type_label.place(x=20, y=280)
        self.device_type_label_other.place(x=160, y=300)
        self.device_type_entry_desktop.place(x=30, y=300)
        self.device_type_entry_phone.place(x=85, y=300)
        self.device_type_entry_laptop.place(x=140, y=300)
        self.device_type_entry_other.place(x=20, y=320)

        self.date_of_service_label.place(x=20, y=360)
        self.date_of_service_entry.place(x=20, y=380)

        self.date_of_contact_label.place(x=20, y=420)
        self.date_of_contact_entry.place(x=20, y=440)

        self.time_of_contact_label.place(x=20, y=480)
        self.time_of_contact_entry.place(x=20, y=500)

        self.difficulty_label.place(x=20, y=540)
        self.difficulty_entry.place(x=20, y=560)

        self.payment_label.place(x=20, y=600)
        self.payment_entry.place(x=20, y=620)

        self.bind("<<INCOMING>>", self.ackn)

    def ackn(self, event=None):
        print("acknowledged. printing data:")
        print(self.controller.shared_data)
        # Gets each info from the shared controller data and inserts it into it's respepctive field !
        self.entry_values(self.name_entry, self.controller.shared_data["Name Field"])
        self.entry_values(self.age_entry, self.controller.shared_data["Age Field"])
        self.gender_decide(self.controller.shared_data["Gender Field"])
        self.contact_decide(self.controller.shared_data["Contact Type Field"])
        self.entry_values(self.contact_info_entry, self.controller.shared_data["Contact Info Field"])
        self.text_values(self.problem_entry, self.controller.shared_data["Problem Field"])
        self.text_values(self.solution_entry, self.controller.shared_data["Solution Field"])
        self.device_device(self.controller.shared_data['Device Type Field'])
        self.entry_values(self.time_of_contact_entry, self.controller.shared_data['Time of Contact'])
        self.entry_values(self.date_of_contact_entry, self.controller.shared_data['Date of Contact Field'])
        self.entry_values(self.date_of_service_entry, self.controller.shared_data['Date of Service Field'])
        self.entry_values(self.difficulty_entry, self.controller.shared_data['Difficulty Field'])
        self.entry_values(self.payment_entry, self.controller.shared_data['Payment Field'])
        self.id_insert(self.controller.shared_data["Should never fail"])

    def id_insert(self, val):
        self.uniqueid_entry.configure(state='normal')
        self.uniqueid_entry.delete(0, "end")
        self.uniqueid_entry.insert(0, val)
        self.uniqueid_entry.config(state='disabled')

    def gender_decide(self, val):
        if val == "Female":
            self.gender_entry_female.state(['selected'])
        elif val == "Male":
            self.gender_entry_male.state(['selected'])
        else:
            self.gender_entry_other.state(['selected'])

    def contact_decide(self, val):
        if val == "FaceBook":
            self.contact_type_entry_facebook.state(['selected'])
        elif val == "Email":
            self.contact_type_entry_email.state(['selected'])
        else:
            self.contact_type_entry_call.state(['selected'])

    def device_device(self, val):
        if val == "Desktop":
            self.device_type_entry_desktop.state(['selected'])
        elif val == "Phone":
            self.device_type_entry_phone.state(['selected'])
        elif val == "Laptop":
            self.device_type_entry_laptop.state(['selected'])
        else:
            self.entry_values(self.device_type_entry_other, val)


    def text_values(self, widg, val):
        widg.delete(0.0, "end")
        widg.insert(0.0, val)

    def entry_values(self, widg, val):
        print(val)
        widg.delete(0, "end")
        widg.insert(0, val)

    def name_check(self, name):
        to_return = ""
        for i in range(len(name)):
            if i == 0:
                to_return += name[i].upper()
            else:
                to_return += name[i].lower()
        return to_return


    def uuid_gen(self):
        x = uuid.uuid4()
        y = str(x)
        z = y.replace("-", '')
        print(f'y: {y}')
        print(f'z: {z}')
        return z


    def null_check(self):
        # Revemped version that does not fail data input if data is missing. Enters anyway. Should allow more
        # dynamic and easier to use DBing of relevent information
        list_of_data = {
            "Name Field": self.name_var.get(),
            "Age Field": self.age_var.get(),
            "Gender Field": self.gender_check(),  #prolem
            "Contact Type Field": self.contact_type_check(),
            "Contact Info Field": self.contact_info_var.get(),
            "Problem Field": self.problem_entry.get('1.0', 'end-1c'),
            "Solution Field": self.solution_entry.get('1.0', 'end-1c'),
            "Device Type Field": self.device_type_check(),  #probl
            "Time of Contact": self.time_of_contact_var.get(),
            "Date of Contact Field": self.date_of_contact_var.get(),
            "Date of Service Field": self.date_of_service_var.get(),
            "Difficulty Field": self.difficulty_var.get(),
            "Payment Field": self.payment_var.get(),
            "Should never fail": self.uniqueid_entry.get()
        }
        # Creates a list of entries that were missed
        print("Full data, moving to process...")
        print(f'All data: {list_of_data.values()}')
        self.name_entry.delete(0, 'end')
        self.age_entry.delete(0, 'end')

        self.gender_entry_male.state(["!selected", "focus"])
        self.gender_entry_female.state(["!selected", "focus"])
        self.gender_entry_other.state(["!selected", "focus"])

        self.contact_info_entry.delete(0, 'end')

        self.contact_type_entry_facebook.state(["!selected", "focus"])
        self.contact_type_entry_email.state(["!selected", "focus"])
        self.contact_type_entry_call.state(["!selected", "focus"])

        self.problem_entry.delete("1.0", 'end')
        self.solution_entry.delete("1.0", 'end')

        self.device_type_entry_desktop.state(["!selected", "focus"])
        self.device_type_entry_phone.state(["!selected", "focus"])
        self.device_type_entry_laptop.state(["!selected", "focus"])

        self.date_of_contact_entry.delete(0, 'end')
        self.date_of_service_entry.delete(0, 'end')
        self.difficulty_entry.delete(0, 'end')
        self.payment_entry.delete(0, 'end')
        count = 0
        input_data = list(list_of_data.values())
        if input_data[13] == '':
            print("getting a new UUID")
            input_data[13] = self.uuid_gen()
        print(count)
        add_data(input_data[0], input_data[1], input_data[2], input_data[3], input_data[4], input_data[5], input_data[6]
                 , input_data[7], input_data[8], input_data[9], input_data[10], input_data[11], input_data[12],
                 input_data[13])


    def gender_check(self):
        return_str = ''
        sum_check = []
        check_list = [
            self.gender_entry_male_var.get(),
            self.gender_entry_female_var.get(),
            self.gender_entry_other_var.get()
        ]
        for item in check_list:
            if item != "":
                return_str = item
                sum_check.append(item)
        return return_str


    def contact_type_check(self):
        return_str = ''
        sum_check = []
        check_list = [
            self.is_facebook.get(),
            self.is_call.get(),
            self.is_email.get()
        ]
        for item in check_list:
            if item != "":
                return_str = item
                sum_check.append(item)
        return return_str


    def device_type_check(self):
        return_str = ''
        sum_check = []
        check_list = [
            self.is_desktop.get(),
            self.is_phone.get(),
            self.is_laptop.get(),
            self.device_type_var.get()
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




class view_data(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Treeview styles
        treeview_Style = ttk.Style()
        treeview_Style.configure("main_style.Treeview", font=("Arial", 8), foreground="white",
                                 background="#262626")
        treeview_Style.layout("main_style.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        self.configure(bg="#656489")
        
        
        # Scrollbar functionality
        main_frame = tk.Frame(self, padx=10, pady=10)
        main_frame.place(x=0, y=50)
        main_scroll = tk.Scrollbar(main_frame)
        main_scroll.pack(side="right", fill="y")
        
        self.main_tree = ttk.Treeview(main_frame, yscrollcommand=main_scroll.set,
                                 xscrollcommand=main_scroll.set, style="main_style.Treeview", height=20, show='headings')
        self.main_tree['columns'] = ('Name', 'Age', 'Gender', 'Type of contact', 'Contact info', 'Problem', 'Solution', 'Device type'
                                , 'Time of contact', 'Date of contact', 'Date of service', 'Difficulty', 'Payment', 'ID')
        mn_wid = 80
        main_scroll.config(command=self.main_tree.yview)
        self.main_tree.column("#0", width=0, stretch=False)
        self.main_tree.column("Name", width=mn_wid, stretch=False)
        self.main_tree.column("Age", width=mn_wid, stretch=False)
        self.main_tree.column("Gender", width=mn_wid, stretch=False)
        self.main_tree.column("Type of contact", width=100, stretch=False)
        self.main_tree.column("Contact info", width=mn_wid, stretch=False)
        self.main_tree.column("Problem", width=165, stretch=False)
        self.main_tree.column("Solution", width=165, stretch=False)
        self.main_tree.column("Device type", width=mn_wid, stretch=False)
        self.main_tree.column("Time of contact", width=100, stretch=False)
        self.main_tree.column("Date of contact", width=100, stretch=False)
        self.main_tree.column("Date of service", width=100, stretch=False)
        self.main_tree.column("Difficulty", width=mn_wid, stretch=False)
        self.main_tree.column("Payment", width=mn_wid, stretch=False)
        self.main_tree.column("ID", width=mn_wid, stretch=False)
        # Adding headings
        self.main_tree.heading("#0", text='', anchor="center")
        self.main_tree.heading("Name", text="Name", anchor="center")
        self.main_tree.heading("Age", text="Age", anchor="center")
        self.main_tree.heading("Gender", text="Gender", anchor="center")
        self.main_tree.heading("Type of contact", text="Type of contact", anchor="center")
        self.main_tree.heading("Contact info", text="Contact info", anchor="center")
        self.main_tree.heading("Problem", text="Problem", anchor="center")
        self.main_tree.heading("Solution", text="Solution", anchor="center")
        self.main_tree.heading("Device type", text="Device type", anchor="center")
        self.main_tree.heading("Time of contact", text="Time of contact", anchor="center")
        self.main_tree.heading("Date of contact", text="Date of contact", anchor="center")
        self.main_tree.heading("Date of service", text="Date of service", anchor="center")
        self.main_tree.heading("Difficulty", text="Difficulty", anchor="center")
        self.main_tree.heading("Payment", text="Payment", anchor="center")
        self.main_tree.heading("ID", text="ID", anchor="center")
        self.main_tree.pack(fill="x")
        main_scroll.pack(side="right", fill="y")
        self.delete_edit_popup = tk.Menu(self.main_tree, tearoff=0)
        self.delete_edit_popup.add_command(label="Delete", command=lambda: self.delete_entry('x'))
        self.delete_edit_popup.add_command(label='Edit', command=lambda: self.edit_entry("yo"))
        tk.Button(self, text="Refresh", command=self.refresh_data).place(x=1250, y=10)
        self.main_tree.bind("<Button-3>", self.popup)
        self.query_main()
# view_data_frame functions ! #

    def query_main(self):
        con = sqlite3.Connection("./MAIN.DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM main")
        rows = cur.fetchall()
        for row in rows:
            self.main_tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                                 row[9], row[10], row[11], row[12], row[13]))
        con.close()

    def delete_data(self, obj):
        print(f'ovj: {obj}')
        con = sqlite3.Connection("./MAIN.DB")
        cur = con.cursor()
        cur.execute('DELETE from main where Unique_id = ?', (obj[13],))
        con.commit()


    def refresh_data(self):
        self.main_tree.delete(*self.main_tree.get_children())
        self.query_main()



    def delete_entry(self, event):
        print("delete time")
        all_selected = self.main_tree.selection()
        for one_entry in all_selected:
            selected_entry = self.main_tree.item(one_entry, 'values')
            print(selected_entry)
            x = tkinter.messagebox.askyesno(title='Continue?', message="Are you sure you wanna do that !?")
            if x:
                self.main_tree.delete(one_entry)
                self.delete_data(selected_entry)
            else:
                print("ignore...")

    def edit_entry(self, event):
        for item in self.main_tree.selection():
            chosen_entry = self.main_tree.item(item, 'values')
        print(chosen_entry)
        self.controller.shared_data = {
            "Name Field": chosen_entry[0],
            "Age Field": chosen_entry[1],
            "Gender Field": chosen_entry[2],
            "Contact Type Field": chosen_entry[3],
            "Contact Info Field": chosen_entry[4],
            "Problem Field": chosen_entry[5],
            "Solution Field": chosen_entry[6],
            "Device Type Field": chosen_entry[7],
            "Time of Contact": chosen_entry[8],
            "Date of Contact Field": chosen_entry[9],
            "Date of Service Field": chosen_entry[10],
            "Difficulty Field": chosen_entry[11],
            "Payment Field": chosen_entry[12],
            "Should never fail": chosen_entry[13]
        }
        print(self.controller.shared_data)
        # Switches to the adding_data frame
        self.controller.show_frame(AddingData)
        # Sends the signal -> controller, controller creates event -> adddata listens pulls the shared data and insertit
        self.controller.create_event()




    def popup(self, event):
        try:
            self.delete_edit_popup.tk_popup(event.x_root, event.y_root)
        finally:
            self.delete_edit_popup.grab_release()



main_app = main_logic()
main_app.mainloop()
