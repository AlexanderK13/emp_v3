from tkinter import *
from tkinter import messagebox
import csv


def update(event=None):
    index = listbox1.curselection()[0]
    # print(index)
    First_Name_Value.config(text=Data[index][2])
    Last_Name_Value.config(text=Data[index][3])
    User_ID_Value.config(text=Data[index][4])
    Date_Value.config(text=Data[index][5])
    Age_Value.config(text=Data[index][6])
    Adress_Value.config(text=Data[index][7])
    Company_Department_Value.config(text=Data[index][8])
    Phone_Value.config(text=Data[index][9])
    Employment_Value.config(text=Data[index][10])
    Gender_Value.config(text=Data[index][11])
    Driver_license_Value.config(text=Data[index][12])
    religion_Value.config(text=Data[index][13])
    Health_Value.config(text=Data[index][14])
    marital_status_Value.config(text=Data[index][15])
    salary_Value.config(text=Data[index][16])
    email_Value.config(text=Data[index][17])
    supervisor_Value.config(text=Data[index][18])
    Entry_Value.config(text=Data[index][19])
    return None


def add_employee(event=None):
    global add_ID_Label, add_Fullname_Label, add_First_Name_Label, add_Last_Name_Label, add_User_ID_Label
    global add_Date_Label, add_Age_Label, add_Adress_Label, add_Company_Department_Label, add_Phone_Label
    global add_Employment_Label, add_Gender_Label, add_Driver_license_Label, add_religion_Label
    global add_Health_insurance_Label, add_marital_status_Label, add_salary_Label, add_email_Label
    global add_supervisor_Label, add_Entry_date_Label
    global add_emp, add_ID_Entry, add_Fullname_Entry, add_First_Name_Entry, add_Last_Name_Entry,  add_User_ID_Entry
    global add_Date_Entry,  add_Age_Entry, add_Adress_Entry, add_Company_Department_Entry, add_Phone_Entry
    global add_Employment_Entry, add_Gender_Entry, add_Driver_license_Entry, add_religion_Entry
    global add_Health_insurance_Entry, add_marital_status_Entry, add_salary_Entry, add_email_Entry, add_supervisor_Entry
    global add_Entry_date_Entry

    add_emp = Tk()
    add_emp.title("Add Employee")
    add_emp.iconbitmap('images/icon.ico')
    add_emp.geometry('350x475')
    add_emp.resizable(width=False, height=False)

    # Labels for Add Employee
    add_ID_Label = Label(add_emp, text="ID").grid(row=2, column=0, sticky="W", padx=10)
    add_Fullname_Label = Label(add_emp, text="Fullname").grid(row=3, column=0, sticky="W", padx=10)
    add_First_Name_Label = Label(add_emp, text="First Name").grid(row=4, column=0, sticky="W", padx=10)
    add_Last_Name_Label = Label(add_emp, text="Last Name").grid(row=5, column=0, sticky="W", padx=10)
    add_User_ID_Label = Label(add_emp, text="User ID").grid(row=6, column=0, sticky="W", padx=10)
    add_Date_Label = Label(add_emp, text="Date of Birth").grid(row=7, column=0, sticky="W", padx=10)
    add_Age_Label = Label(add_emp, text="Age").grid(row=8, column=0, sticky="W", padx=10)
    add_Adress_Label = Label(add_emp, text="Street").grid(row=9, column=0, sticky="W", padx=10)
    add_Company_Department_Label = Label(add_emp, text="Company Department").grid(row=10, column=0, sticky="W", padx=10)
    add_Phone_Label = Label(add_emp, text="Phone Number").grid(row=11, column=0, sticky="W", padx=10)
    add_Employment_Label = Label(add_emp, text="Employment").grid(row=12, column=0, sticky="W", padx=10)
    add_Gender_Label = Label(add_emp, text="Gender (m/w/d)").grid(row=13, column=0, sticky="W", padx=10)
    add_Driver_license_Label = Label(add_emp, text="Driver's license").grid(row=14, column=0, sticky="W", padx=10)
    add_religion_Label = Label(add_emp, text="Religion").grid(row=15, column=0, sticky="W", padx=10)
    add_Health_insurance_Label = Label(add_emp, text="Health insurance").grid(row=16, column=0, sticky="W", padx=10)
    add_marital_status_Label = Label(add_emp, text="Marital status").grid(row=17, column=0, sticky="W", padx=10)
    add_salary_Label = Label(add_emp, text="Salary").grid(row=18, column=0, sticky="W", padx=10)
    add_email_Label = Label(add_emp, text="E-Mail").grid(row=19, column=0, sticky="W", padx=10)
    add_supervisor_Label = Label(add_emp, text="Supervisor").grid(row=20, column=0, sticky="W", padx=10)
    add_Entry_date_Label = Label(add_emp, text="Entry date").grid(row=21, column=0, sticky="W", padx=10)
    
    placeholder4 = Label(add_emp, text="", font=("Arial", 6)).grid(row=22, column=0, sticky="W", padx=10)
    placeholder5 = Label(add_emp, text="", font=("Arial", 6)).grid(row=22, column=1, sticky="W")
    # Add
    button2_1 = Button(add_emp, text="Add", command=add_emp_in_to_csv)
    button2_1.grid(row=23, column=0)
    # Cancel
    button2_2 = Button(add_emp, text="Cancel", command=add_cancel)
    button2_2.grid(row=23, column=1)
    # Labels for Add Employee
    add_ID_Entry = Entry(add_emp, width=30)
    add_ID_Entry.grid(row=2, column=1, sticky="W", padx=10)
    add_Fullname_Entry = Entry(add_emp, width=30)
    add_Fullname_Entry.grid(row=3, column=1, sticky="W", padx=10)
    add_First_Name_Entry = Entry(add_emp, width=30)
    add_First_Name_Entry.grid(row=4, column=1, sticky="W", padx=10)
    add_Last_Name_Entry = Entry(add_emp, width=30)
    add_Last_Name_Entry.grid(row=5, column=1, sticky="W", padx=10)
    add_User_ID_Entry = Entry(add_emp, width=30)
    add_User_ID_Entry.grid(row=6, column=1, sticky="W", padx=10)
    add_Date_Entry = Entry(add_emp, width=30)
    add_Date_Entry.grid(row=7, column=1, sticky="W", padx=10)
    add_Age_Entry = Entry(add_emp, width=30)
    add_Age_Entry.grid(row=8, column=1, sticky="W", padx=10)
    add_Adress_Entry = Entry(add_emp, width=30)
    add_Adress_Entry.grid(row=9, column=1, sticky="W", padx=10)
    add_Company_Department_Entry = Entry(add_emp, width=30)
    add_Company_Department_Entry.grid(row=10, column=1, sticky="W", padx=10)
    add_Phone_Entry = Entry(add_emp, width=30)
    add_Phone_Entry.grid(row=11, column=1, sticky="W", padx=10)
    add_Employment_Entry = Entry(add_emp, width=30)
    add_Employment_Entry.grid(row=12, column=1, sticky="W", padx=10)
    add_Gender_Entry = Entry(add_emp, width=30)
    add_Gender_Entry.grid(row=13, column=1, sticky="W", padx=10)
    add_Driver_license_Entry = Entry(add_emp, width=30)
    add_Driver_license_Entry.grid(row=14, column=1, sticky="W", padx=10)
    add_religion_Entry = Entry(add_emp, width=30)
    add_religion_Entry.grid(row=15, column=1, sticky="W", padx=10)
    add_Health_insurance_Entry = Entry(add_emp, width=30)
    add_Health_insurance_Entry.grid(row=16, column=1, sticky="W", padx=10)
    add_marital_status_Entry = Entry(add_emp, width=30)
    add_marital_status_Entry.grid(row=17, column=1, sticky="W", padx=10)
    add_salary_Entry = Entry(add_emp, width=30)
    add_salary_Entry.grid(row=18, column=1, sticky="W", padx=10)
    add_email_Entry = Entry(add_emp, width=30)
    add_email_Entry.grid(row=19, column=1, sticky="W", padx=10)
    add_supervisor_Entry = Entry(add_emp, width=30)
    add_supervisor_Entry.grid(row=20, column=1, sticky="W", padx=10)
    add_Entry_date_Entry = Entry(add_emp, width=30)
    add_Entry_date_Entry.grid(row=21, column=1, sticky="W", padx=10)


def add_emp_in_to_csv():
    with open('export.csv', 'a') as file:
        #writer_in_file=csv.writer(file)
        writer_in_file = csv.writer(file, dialect='unix')
        writer_in_file.writerow([add_ID_Entry.get(), add_Fullname_Entry.get(), add_First_Name_Entry.get(), add_Last_Name_Entry.get(), add_User_ID_Entry.get(), add_Date_Entry.get(), add_Age_Entry.get(), add_Adress_Entry.get(), add_Company_Department_Entry.get(), add_Phone_Entry.get(), add_Employment_Entry.get(), add_Gender_Entry.get(), add_Driver_license_Entry.get(), add_religion_Entry.get(), add_Health_insurance_Entry.get(), add_marital_status_Entry.get(), add_salary_Entry.get(), add_email_Entry.get(), add_supervisor_Entry.get(), add_Entry_date_Entry.get()])   
    # Massage Box
    messagebox.showinfo("Employee add information", """To see the new added Employee, please restart the Program""")
    # Clear Text
    add_emp.destroy()
    

def add_cancel(event=None):
    add_emp.destroy()


# Main Code
# .csv File
filepath = r'export.csv'
File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
del (Data[0])

list_of_First_Name = []
for x in list(range(0, len(Data))):
    list_of_First_Name.append(Data[x][1])


# TK Window
root = Tk()
root.title("Employee info reader")
root.iconbitmap('images/icon.ico')
root.geometry('460x595')
root.resizable(width=False, height=False)

# Massage Box
messagebox.showinfo("Navigation information", """1. Select an employee
2. Press the Enter key
3. You should now be able to see the information about the employee""")

# Listbox
listbox1 = Listbox(root, width=25, height=10)
for x, y in enumerate(list_of_First_Name):
    listbox1.insert(x, y)

listbox1.grid(row=0, column=0, sticky="w", padx=10, pady=10)

# Company Logo
company_logo = PhotoImage(file="images/company_logo.png", )

company_logo_Label = Label(root, image=company_logo, width=240, height=150)
company_logo_Label.grid(row=0, column=1, sticky="w", padx=10, pady=10)

# Add Employee Button
button1 = Button(root, text="Add Employee", command=add_employee)
button1.grid(row=1, column=1)

# placeholder
placeholder1 = Label(root, text="", font=("Arial", 6)).grid(row=1, column=0, sticky="W", padx=10)
placeholder2 = Label(root, text="", font=("Arial", 6)).grid(row=1, column=1, sticky="W")
placeholder3 = Label(root, text="", font=("Arial", 6)).grid(row=1, column=2, sticky="W")

# Update
root.bind('<Return>', update)

# Labels
# ID_Label = Label(root, text="ID").grid(row=2, column=0, sticky="W", padx=10)
# Fullname_Label = Label(root, text="Fullname").grid(row=3, column=0, sticky="W", padx=10)
First_Name_Label = Label(root, text="First Name").grid(row=4, column=0, sticky="W", padx=10)
Last_Name_Label = Label(root, text="Last Name").grid(row=5, column=0, sticky="W", padx=10)
User_ID_Label = Label(root, text="User ID").grid(row=6, column=0, sticky="W", padx=10)
Date_Label = Label(root, text="Date of Birth").grid(row=7, column=0, sticky="W", padx=10)
Age_Label = Label(root, text="Age").grid(row=8, column=0, sticky="W", padx=10)
Adress_Label = Label(root, text="Street").grid(row=9, column=0, sticky="W", padx=10)
Company_Department_Label = Label(root, text="Company Department").grid(row=10, column=0, sticky="W", padx=10)
Phone_Label = Label(root, text="Phone Number").grid(row=11, column=0, sticky="W", padx=10)
Employment_Label = Label(root, text="Employment").grid(row=12, column=0, sticky="W", padx=10)
Gender_Label = Label(root, text="Gender (m/w/d)").grid(row=13, column=0, sticky="W", padx=10)
Driver_license_Label = Label(root, text="Driver's license").grid(row=14, column=0, sticky="W", padx=10)
religion_Label = Label(root, text="Religion").grid(row=15, column=0, sticky="W", padx=10)
Health_insurance_Label = Label(root, text="Health insurance").grid(row=16, column=0, sticky="W", padx=10)
marital_status_Label = Label(root, text="Marital status").grid(row=17, column=0, sticky="W", padx=10)
salary_Label = Label(root, text="Salary").grid(row=18, column=0, sticky="W", padx=10)
email_Label = Label(root, text="E-Mail").grid(row=19, column=0, sticky="W", padx=10)
supervisor_Label = Label(root, text="Supervisor").grid(row=20, column=0, sticky="W", padx=10)
Entry_date_Label = Label(root, text="Entry date").grid(row=21, column=0, sticky="W", padx=10)

# ID_Value = Label(root, text="")
# ID_Value.grid(row=2, column=1, sticky="W")

# Fullname_Value = Label(root, text="")
# Fullname_Value.grid(row=3, column=1, sticky="W")

First_Name_Value = Label(root, text="")
First_Name_Value.grid(row=4, column=1, sticky="W")

Last_Name_Value = Label(root, text="")
Last_Name_Value.grid(row=5, column=1, sticky="W")

User_ID_Value = Label(root, text="")
User_ID_Value.grid(row=6, column=1, sticky="W")

Date_Value = Label(root, text="")
Date_Value.grid(row=7, column=1, sticky="W")

Age_Value = Label(root, text="")
Age_Value.grid(row=8, column=1, sticky="W")

Adress_Value = Label(root, text="")
Adress_Value.grid(row=9, column=1, sticky="W")

Company_Department_Value = Label(root, text="")
Company_Department_Value.grid(row=10, column=1, sticky="W")

Phone_Value = Label(root, text="")
Phone_Value.grid(row=11, column=1, sticky="W")

Employment_Value = Label(root, text="")
Employment_Value.grid(row=12, column=1, sticky="W")

Gender_Value = Label(root, text="")
Gender_Value.grid(row=13, column=1, sticky="W")

Driver_license_Value = Label(root, text="")
Driver_license_Value.grid(row=14, column=1, sticky="W")

religion_Value = Label(root, text="")
religion_Value.grid(row=15, column=1, sticky="W")

Health_Value = Label(root, text="")
Health_Value.grid(row=16, column=1, sticky="W")

marital_status_Value = Label(root, text="")
marital_status_Value.grid(row=17, column=1, sticky="W")

salary_Value = Label(root, text="")
salary_Value.grid(row=18, column=1, sticky="W")

email_Value = Label(root, text="")
email_Value.grid(row=19, column=1, sticky="W")

supervisor_Value = Label(root, text="")
supervisor_Value.grid(row=20, column=1, sticky="W")

Entry_Value = Label(root, text="")
Entry_Value.grid(row=21, column=1, sticky="W")
root.mainloop()
