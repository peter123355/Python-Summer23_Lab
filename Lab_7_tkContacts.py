# Name : Peter Geevarghese Alex
# Lab 7
# Course number : ITMD 513-01
# Description :
import time
print("ITMD 513-01")
print("Lab 7")
print("Programmer: Peter Geevarghese Alex")

x = 12
print("-" * 25)
## dd/mm/yyyy format
print (time.strftime("%d/%m/%Y"))


#military time
print ("Current time:",time.strftime("%X"))

from tkinter import *
from tkinter import messagebox
import contacts
def mySelect():
    print("At %s of %d" % (select.curselection(), len(contacts.contactList)))
    return int(select.curselection()[0])

def addmyCont():
    contacts.contactList.append([nameVar.get(), phoneVar.get()])
    setList()
    saveContacts()
    messagebox.showinfo("Success", "Contact is now added successfully")

def updateMyCont():
    contacts.contactList[mySelect()] = [nameVar.get(), phoneVar.get()]
    setList()
    saveContacts()
    messagebox.showinfo("Success", "Contact is now updated successfully")

def delmyCont():
    if messagebox.askokcancel(title="Delete", message="Are you sure you want to delete this contact?"):
        del contacts.contactList[mySelect()]
        setList()
        saveContacts()
        messagebox.showinfo("Success", "Contact is now deleted successfully")

def ldmyContact():
    if select.curselection():
        contactName, contactPhone = contacts.contactList[mySelect()]
        nameVar.set(contactName)
        phoneVar.set(contactPhone)

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
    myButton5 = Button(f2, text="Save ", command=saveContacts)
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
    contacts.contactList.sort()
    select.delete(0, END)
    for name, phone in contacts.contactList:
        select.insert(END, name)

def saveContacts():
    contacts.saveContacts()
    messagebox.showinfo("Saved", "Contact list has now been saved")

def confirmExit():
    if messagebox.askokcancel(title="Exit", message="Are you sure you want to exit?"):
        root.destroy()

root = bldFrame()
setList()

root.mainloop()
