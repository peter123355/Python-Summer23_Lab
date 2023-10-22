contactList = [
    ['Siemens, Harper', '323-4149'],
    ['Smith, Patti', '239-1212'],
    ['Jackson, Janet', '313-1352'],
    ['Manfredi, Ralph', '872-2221'],
    ['Thompson, Bobby', '365-2622'],
    ['James, Lebron', '457-6223'],
    ['Ziegler, Zig', '667-1101'],
    ['Robbins, Tony', '329-2310']
]

def saveContacts():
    with open("contacts.py", "w") as file:
        file.write("contactList = [\n")
        for contact in contactList:
            file.write(f"    {repr(contact)},\n")
        file.write("]\n")

def loadMyContacts():
    global contactList
    with open("contacts.py", "r") as file:
        exec(file.read(), globals())

loadMyContacts()
