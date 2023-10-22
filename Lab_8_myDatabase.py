import sqlite3


conn = None
cursor = None

def connect_to_db():
    global conn, cursor
    if conn is None or cursor is None:
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()

def create_to_table():
    connect_to_db()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Peter
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      phone TEXT NOT NULL)''')
    conn.commit()

def read_to_contacts():
    connect_to_db()
    cursor.execute("SELECT * FROM Peter")
    contacts = cursor.fetchall()
    return contacts

def insert_to_contact(name, phone):
    connect_to_db()
    cursor.execute("INSERT INTO Peter (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()

def update_to_contact(name, phone, contact_id):
    connect_to_db()
    cursor.execute("UPDATE Peter SET name=?, phone=? WHERE id=?", (name, phone, contact_id))
    conn.commit()

def delete_to_contact(contact_id):
    connect_to_db()
    cursor.execute("DELETE FROM Peter WHERE id=?", (contact_id,))
    conn.commit()

def delete_to_all_contacts():
    connect_to_db()
    cursor.execute("DELETE FROM Peter")
    conn.commit()

def rollback_to_changes(original_contacts):
    connect_to_db()
    cursor.execute("DELETE FROM Peter")
    for _, name, phone in original_contacts:
        cursor.execute("INSERT INTO Peter (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()

def commit_to_changes():
    connect_to_db()
    conn.commit()

def close_to_connection():
    global conn, cursor
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
    cursor = None
    conn = None

