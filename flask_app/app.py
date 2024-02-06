from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os
import json
app = Flask(__name__)

#logging.basicConfig(filename="/home/ubuntu/flask_app/app.log", level=logging.DEBUG)

module_path = os.path.abspath(__file__)
print("Path of the module:", module_path)

@app.route('/')
def hello():
    return """<h1>Hello there!</h1><br>
    <a href="/loginpage">Login</a><br>
    <a href="/loop">Letterloopd</a>"""

@app.route('/test')
def test():
    return render_template('test_letter.html')

@app.route('/how')
def structure():
    return render_template('structure.txt')

@app.route('/reboot')
def restart():
    return 'Not implemented'

@app.route('/loginpage')
def main():
    return render_template('main.html')

@app.route('/loop')
def rickroll():
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


@app.route('/login', methods=['POST'])
def login():
    users_json = {}
    with open("users.json","r") as users:
        users_json = json.load(users)
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        app.logger.debug(f"{username = }:{password = }")
        for data in users_json.values():
            if username == data['username'] and password == data['password']:
            # Successful login
                return render_template('inside.html', name=username)
        else:
            # Failed login
            return 'Invalid credentials. Please try again te balfasz.'
    except Exception as e:
        app.logger.error(f"An error occured: {str(e)}", exc_info=True)
        return "Gebasz", 500
if __name__ == '__main__':
    app.run(debug=True)
