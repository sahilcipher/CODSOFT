import sqlite3
from faker import Faker
fake = Faker()

# Connect to SQLite database
conn = sqlite3.connect('contact_book.db')
cursor = conn.cursor()

# Create the contacts table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS contacts (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         number TEXT NOT NULL,
#         email TEXT NOT NULL,
#         address TEXT NOT NULL
#     )
# ''')

# Reset the AUTOINCREMENT
cursor.execute('DELETE FROM sqlite_sequence WHERE name="contacts"')

# Generate and insert 20 dummy data entries
for _ in range(20):
    name = fake.name()
    number = fake.phone_number()
    email = fake.email()
    address = fake.address()

    cursor.execute('''
        INSERT INTO contacts (name, number, email, address)
        VALUES (?, ?, ?, ?)
    ''', (name, number, email, address))

# Commit changes & close connection
conn.commit()
conn.close()

print("20 dummy data entries inserted into the 'contacts' table.")
