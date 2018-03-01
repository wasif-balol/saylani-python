from flask import Flask

Myapp = Flask(__name__)


@Myapp.route("/")
def index():
    return "Hello World"


Myapp.run(debug=True)


