from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():                  #revise problem
    return "Merhaba, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
#new update python