from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    name  = request.args.get("name", "Flask")
    return f"<p>Hello {escape(name)}</p>"

@app.route('/hello')
def hello():
    return  'Hello, world'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the uswer profile for that user
    return f'user {escape(username)}'

@app.route('/projects/')# doesn't work? perhaps needs pages under it...
def projects():
    return 'The projects page'