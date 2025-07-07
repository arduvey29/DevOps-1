from flask import Flask

app = Flask(__name__)

@app.route('/info')
def info():
    return "Heyy!! This is the info page."

@app.route('/phone') 
def phone():
    return "This is the phone page."

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
