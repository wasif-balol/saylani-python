from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME']='database_1'
app.config['MONGO_URI']='mongodb://Wasif:Wasif@ds231228.mlab.com:31228/database_1'
mongo = PyMongo(app)


@app.route("/")
def index():
    students = []
    records = mongo.db.Wasif.find()
    for user in records:
        students.append({'name': user['name'],\
                         'password': user['password'],\
                        'course':user['course']})

    return jsonify({'SaylaniStudents': students})


@app.route("/add")
def add():
    add = mongo.db.Wasif.insert({'name':'ALI'})
    return "Successfully add"

app.run(debug=True)