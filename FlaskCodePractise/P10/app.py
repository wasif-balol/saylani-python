from flask import Flask,jsonify,request
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'database_1'
app.config['MONGO_URI']='mongodb://Wasif:Wasif@ds231228.mlab.com:31228/database_1'
mongo = PyMongo(app)


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "POST":
        usearch=request.form['user']
        students=[]
        records = mongo.db.Wasif.find({'name': usearch})
        for user in records:
            students.append({'name': user['name'],\
            'password': user['Password'],\
             'Course': user['course']})
        return jsonify({'SearchData': students})
    else:
        return '''
        <form method="POST">
        <h2>Search</h2>
        <input type="text" name="user">
        <input type="submit" value="search">
        </form>
    '''

app.run(debug=True)