from flask import Flask, render_template, request

app = Flask(__name__)

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

# Submit Page (for form)
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return render_template('result.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
