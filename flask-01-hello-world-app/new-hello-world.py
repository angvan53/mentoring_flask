from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Homepage!"

@app.route('/secondpage')
def second():
    return "This is the Second Page"

@app.route('/third')
def third():
    return "This is the Third Page"

@app.route('/fourth/<string:id>')
def fourth(id):
    return f"This is the Fourth Page with ID: {id}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
