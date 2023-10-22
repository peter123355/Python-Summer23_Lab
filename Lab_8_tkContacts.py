 # Name : Peter Geevarghese Alex
# Lab 8
# Course number : ITMD 513-01
"""
Des- In this program,I performed CRUD opertions to add update delete contacts 
and all the chnages are committed to the database.A scrollable listbox is used to display contacts. 
The application offers the ability to commit or rollback contact list modifications. 
Additionally, at startup, the program loads its initial contacts from the Python module "contacts.py" and shows them in the listbox."""
 
import time
print("ITMD 513-01")
print("Lab 8")
print("Programmer: Peter Geevarghese Alex")

x = 12
print("-" * 25)
## dd/mm/yyyy format
print (time.strftime("%d/%m/%Y"))

#military time
print ("Current time:",time.strftime("%X"))

# imports all modules 
from tkinter import *
from tkinter import messagebox
import myDatabase #databse opertaion
import contacts

root = None
original_contacts = []

#there is a lisbox, this fun enables to get slected conact
def mySelect():
    selected_contact = select.curselection()
    if selected_contact:
        return int(selected_contact[0])
    return None
# this is the first Function in terms of crud to add  new contact to  database
def addmyCont():
    name = nameVar.get()
    phone = phoneVar.get()
    if name and phone:
        try:
            myDatabase.insert_to_contact(name, phone)
            setList()
            print(f"New contact with the Name: {name} and Phone: {phone} is successfully added")
            messagebox.showinfo("Success", "Contact is successfully added")
            myDatabase.commit_to_changes()  
        except Exception as e:
            messagebox.showerror("Error", f"Error while adding the contact: {e}")
    else:
        messagebox.showwarning("Field cannot be blank", "Please enter a value in both fields.")
# this is the Second Function to update an old   contact to  database
def updateMyCont():
    name = nameVar.get()
    phone = phoneVar.get()
    if name and phone:
        contact_id = mySelect()
        if contact_id is not None:
            contacts_list = myDatabase.read_to_contacts()
            if contact_id >= 0 and contact_id < len(contacts_list):
                old_name, old_phone = contacts_list[contact_id][1], contacts_list[contact_id][2]
                myDatabase.update_to_contact(name, phone, contacts_list[contact_id][0])  
                setList()  # Refresh the listbox

                print(f"Contact '{old_name}' with phone '{old_phone}' has been successfully updated to '{name}' with phone '{phone}'.")
                messagebox.showinfo("Success", "Contact has been successfully updated")
                myDatabase.commit_to_changes()  
                messagebox.showerror("Contact Not Found", "Selected contact does not exist in the database")
        else:
            messagebox.showwarning("Contact Not Selected", "Please select a contact to update")
    else:
        messagebox.showwarning("Field Cannot Be Blank", "Please enter a value in both fields")
# this is the thrid Function to delete  old contact to  database
def delmyCont():
    if messagebox.askokcancel("Delete Contact", f"Are you sure you want to delete the contact '{nameVar.get()}'?"):
        try:
            contact_id = myDatabase.read_to_contacts()[mySelect()][0]
            myDatabase.delete_to_contact(contact_id)
            setList()
            print(f"The contact {nameVar.get()} is successfully deleted")
            messagebox.showinfo("Success", "Contact is successfully deleted")
            myDatabase.commit_to_changes()  
        except Exception as e:
            messagebox.showerror("Error", f"Error while deleting the contact: {e}")
# this is the forth Function to load   contact to  database
def ldmyContact():
    contact_id = mySelect()
    if contact_id is not None:
        if contact_id >= 0 and contact_id < len(myDatabase.read_to_contacts()):
            contact_details = myDatabase.read_to_contacts()[contact_id]
            nameVar.set(contact_details[1])
            phoneVar.set(contact_details[2])
        else:
            messagebox.showerror("Contact Not Found", "Selected contact does not exist in the database.")
    else:
        messagebox.showwarning("Contact Not Selected", "Please select a contact to load its details.")
#GUI funtion to create 
def bldFrame():
    global nameVar, phoneVar, select
    root = Tk()
    root.title("My Contact List")

    frame1 = Frame(root)
    frame1.pack()

    Label(frame1, text="Name:").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    contactName = Entry(frame1, textvariable=nameVar)
    contactName.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Phone:").grid(row=1, column=0, sticky=W)
    phoneVar = StringVar()
    contactPhone = Entry(frame1, textvariable=phoneVar)
    contactPhone.grid(row=1, column=1, sticky=W)

    f2 = Frame(root)
    f2.pack()
    myButton1 = Button(f2, text=" Add  ", command=addmyCont)
    myButton2 = Button(f2, text="Update ", command=updateMyCont)
    myButton3 = Button(f2, text="Delete ", command=delmyCont)
    myButton4 = Button(f2, text="Load ", command=ldmyContact)
    myButton5 = Button(f2, text="Rollback", command=rollback_changes)
    myButton1.pack(side=LEFT)
    myButton2.pack(side=LEFT)
    myButton3.pack(side=LEFT)
    myButton4.pack(side=LEFT)
    myButton5.pack(side=LEFT)

    f3 = Frame(root)
    f3.pack()
    scroll = Scrollbar(f3, orient=VERTICAL)
    select = Listbox(f3, yscrollcommand=scroll.set, height=7)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH)

    f4 = Frame(root)
    f4.pack()
    exits = Button(f4, text="Exit", command=confirmExit)
    exits.pack(side=LEFT)

    return root

def setList():
    contacts = myDatabase.read_to_contacts()
    contacts.sort()
    select.delete(0, END)
    for _, name, _ in contacts:
        select.insert(END, name)

def confirmExit():
    if messagebox.askokcancel(title="Exit", message="Are you sure you want to exit?"):
        myDatabase.commit_to_changes()  
        myDatabase.close_to_connection() 
        root.destroy()

def save_contacts_to_db():
    contacts_list = contacts.contactlist
    myDatabase.delete_to_all_contacts()  
    for contact in contacts_list:
        name, phone = contact
        myDatabase.insert_to_contact(name, phone)

def rollback_changes():
    global original_contacts
    if messagebox.askokcancel("Rollback", "Do you want to rollback changes?"):
        myDatabase.rollback_to_changes(original_contacts)
        setList()  
        print("Changes rolled back")

def main():
    global root, original_contacts
    root = bldFrame()
    myDatabase.connect_to_db()  
    myDatabase.create_to_table()
    save_contacts_to_db()  
    original_contacts = myDatabase.read_to_contacts()  
    setList() 
    root.protocol("WM_DELETE_WINDOW", confirmExit)  
    root.mainloop()

    
    contacts_list = myDatabase.read_to_contacts()
    contacts_list.sort()
    print("\nContact List in the Database:")
    for contact in contacts_list:
        print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}")

if __name__ == "__main__":
    print("Creating table 'Peter' in contacts database")
    print("Importing data from contacts.py into the table 'Peter'")
    main()
    print("Main loop exited - Changes committed to the database")
