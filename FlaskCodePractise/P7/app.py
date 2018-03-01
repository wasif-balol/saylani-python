from flask import Flask, request

Myapp = Flask(__name__)


@Myapp.route('/')
def home():
    return '''
    <form action="/info" method="POST">
    <input type="text" name="user" placeholder="Full Name"><br>
<input type="email" name="email" placeholder="Email"><br>

<input type="submit" value="Send">
</form>'''


@Myapp.route("/info",methods=['GET','POST'])
def info():
    if request.method == 'GET':
        return '<h1> hello </h1> ' + request.args.get('user') + "Your Email is " + request.args.get('email')
    else:
        return "<h1>POST </h1> Name " + request.form('user') + "email is " + request.form('email')


Myapp.run(debug=True)
