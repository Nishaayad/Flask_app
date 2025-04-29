from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my First Flask App 🔥My Hubbiee..I Love You Sooo...Much 🩷....Muaaah 😘"

if __name__ == '__main__':
    app.run(debug=True)
