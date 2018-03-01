from flask import Flask, render_template, url_for


Myapp = Flask(__name__)


@Myapp.route('/about')
def about():
    return render_template('about.html')

@Myapp.route('/')
def home():
    return render_template('index.html')

Myapp.run(debug=True)