from flask import Flask, url_for, request, render_template, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "This is Top $3cr31#codesoft internship"

# Routes
@app.route('/', methods=["GET", "POST"])
def root():
    if request.method == "POST":
        name = request.form["name"]
        contact = request.form["number"]
        email = request.form['email']
        address = request.form['address']
        save_data(name, contact, email, address)
        flash("Contact added successfully!")
    return render_template('index.html')

@app.route('/view')
def view():
    contacts = get_all_contacts()
    return render_template('contact_view.html', contacts=contacts)

@app.route('/delete/<int:id>')
def delete(id):
    delete_contact(id)
    flash("Contact deleted successfully!")
    return redirect(url_for('view'))

@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    if request.method == "POST":
        name = request.form["name"]
        contact = request.form["number"]
        email = request.form['email']
        address = request.form['address']
        update_contact(id, name, contact, email, address)
        flash("Contact updated successfully!")
        return redirect(url_for('view'))
    contact = get_contact_by_id(id)
    return render_template('update.html', contact=contact)

@app.route('/search', methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form['query']
        contacts = search_contacts(query)
        return render_template('view_contacts.html', contacts=contacts)
    return render_template('search.html')

# All Methods
def save_data(name, contact, email, address): # Method for Saving data in DB
    connection = sqlite3.connect('contact_book.db')
    cursor = connection.cursor()
    query = "INSERT INTO contacts (name, number, email, address) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (name, contact, email, address))
    connection.commit()
    connection.close()

def get_all_contacts(): # Method for get all data from DB
    connection = sqlite3.connect('contact_book.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    connection.close()
    return contacts

def get_contact_by_id(contact_id): # Method for Get Data by ID
    connection = sqlite3.connect('contact_book.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts WHERE id=?", (contact_id,))
    contact = cursor.fetchone()
    connection.close()
    return contact

def update_contact(contact_id, name, contact, email, address): # For Update Contact
    connection = sqlite3.connect('contact_book.db')
    cursor = connection.cursor()
    query = "UPDATE contacts SET name=?, number=?, email=?, address=? WHERE id=?"
    cursor.execute(query, (name, contact, email, address, contact_id))
    connection.commit()
    connection.close()

def delete_contact(contact_id): # For Deleting contact from DB
    connection = sqlite3.connect('contact_book.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    connection.commit()
    connection.close()

def search_contacts(query): # Search Contacts from DB
    connection = sqlite3.connect('contact_book.db')
    cursor = connection.cursor()
    query = f"%{query}%"
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR number LIKE ? OR email LIKE ? OR address LIKE ?", (query, query, query, query))
    contacts = cursor.fetchall()
    connection.close()
    return contacts

if __name__ == '__main__':
    app.run(debug=True)