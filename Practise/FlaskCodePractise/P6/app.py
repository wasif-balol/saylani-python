from flask import Flask


Myapp = Flask(__name__)

@Myapp.route('/<name>')
def nam(name):
    return "hello bro: " + name

Myapp.run(debug=True)