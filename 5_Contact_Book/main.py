import sqlite3 # Import SQLite3

# Init. DB Connection
connection = sqlite3.connect('contact_book.db')
curser = connection.cursor()

# SQL Query for DB
query = """
    CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    number TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL
);
"""

# Execute Query
curser.execute(query)

# Commit changes & close connection
connection.commit()
connection.close()