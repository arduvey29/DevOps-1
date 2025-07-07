from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/info')
def info():
    return "Heyy!! This is the info page."

@app.route('/phone') 
def phone():
    return "This is the phone page."

@app.route('/contact')
def contact():
    return "This is the contact page."

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/help')
def help():
    return "This is the help page."

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
