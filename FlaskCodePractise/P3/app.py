from flask import Flask,render_template

Myapp = Flask(__name__)


@Myapp.route('/About')
def About():
    return render_template("About.html")

@Myapp.route('/Index')
def Inde():
    return render_template('Index.html')


Myapp.run(debug=True)