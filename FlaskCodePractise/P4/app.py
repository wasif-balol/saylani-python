from flask import Flask,render_template


Myapp = Flask(__name__)

@Myapp.route('/about')
def about():
    return render_template('About.html')


@Myapp.route('/index')
def index():
    return render_template('Index.html')


Myapp.run(debug=True)