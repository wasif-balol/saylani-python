from flask import Flask

MyApp = Flask(__name__)


@MyApp.route('/Home')
def home():
    return 'I am studying \
    in saylani \
    and enrollled in AI course \
    and sir zeeshan is our teacher '


@MyApp.route('/About')
def about():
    return '<h1>This is about page</h1> \
    and this text text is written in about page \
    <h3> this is end <h3>'


MyApp.run(debug=True)