from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Website Routes
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['password_length'])
    include_uppercase = 'include_uppercase' in request.form
    include_lowercase = 'include_lowercase' in request.form
    include_digits = 'include_digits' in request.form
    include_symbols = 'include_symbols' in request.form

    password = gen_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
    return render_template('index.html', password=password)

# Function to generate Password
def gen_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if len(characters) == 0:
        return "Please select at least one character type."

    password = ''.join(random.choices(characters, k=length))
    return password

if __name__ == '__main__':
    app.run(debug=True)
