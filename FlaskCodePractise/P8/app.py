from flask import Flask,jsonify


Myapp = Flask(__name__)


@Myapp.route('/')
def func():
    students = [
        {"id" : '1',"name":"zeeshan"},
        {"id": '2',"name":"wasif"}
    ]
    return jsonify({"AI atudents":students})

Myapp.run(debug=True)