import os
from flask import Flask, request, url_for, render_template, redirect, session
from markupsafe import escape

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', b'_5#y2L"F4Q8z\n\xec]/')

# @app.route("/")
# def index():
#     name  = request.args.get("name", "Flask")
#     return f"<p>Hello {escape(name)}</p>"

@app.route('/')
def index():
    # if 'username' in session:
    #     return f'Logged in as {session["username"]}'
    
    username = session.get("username",None)
    return render_template('red_scar_overview.html', person=username, image_url='/static/red scar region.png')

@app.route('/scars_watch')
def scars_watch():
    return render_template('scars_watch.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# @app.route('/hello')
# def hello():
#     return  'Hello, world'

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', person=name, image_url='/static/red scar region.png')

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'user {escape(username)}'

@app.route('/projects/')# doesn't work? perhaps needs pages under it...
def projects():
    return 'The projects page'


if __name__ == '__main__':
    # For Codespaces and local development
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', True)
    host = os.environ.get('FLASK_HOST', '0.0.0.0')

    with app.test_request_context():
        print(f"Routes available:")
        print(f"  {url_for('index')}")
        print(f"  {url_for('scars_watch')}")
        print(f"  {url_for('profile', username='sample')}")

    print(f"\nStarting Flask app on {host}:{port}")
    app.run(host=host, port=port, debug=debug)

