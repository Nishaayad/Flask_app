import sqlite3 
from flask import Flask, render_template, request

app = Flask(__name__)

# Create DB Table if it doesn't exist
def create_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# Call create_db() function to initialize the table when the app starts
create_db()

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Form Page
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the data from the form
    name = request.form['name']
    email = request.form['email']

    # Insert the data into the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

    # After saving, render the result page to show the user's info
    return render_template('result.html', name=name, email=email)


@app.route('/users-from-db')
def users_from_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    conn.close()
    return render_template('users_data.html', users=data)

@app.route('/jinja-home')
def jinja_home():
    naam = "Nisha 💖"
    return render_template('home.html', naam=naam)

@app.route('/jinja-users')
def jinja_users():
    user_list = [
        {"name": "Aman", "email": "aman@example.com"},
        {"name": "Riya", "email": "riya@example.com"},
        {"name": "Nisha", "email": "nisha@example.com"}
    ]
    return render_template('users.html', users=user_list)

if __name__ == '__main__':
    app.run(debug=True)
