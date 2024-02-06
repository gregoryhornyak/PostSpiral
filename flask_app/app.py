from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

#logging.basicConfig(filename="/home/ubuntu/flask_app/app.log", level=logging.DEBUG)

dummy_user = {'username': 'lajos', 'password': 'jelszo'}

@app.route('/')
def hello():
    return "<h1>Hello there!</h1><br>login: /main<br>letterloopd: /loop"

@app.route('/test')
def test():
    return render_template('test_letter.html')

@app.route('/how')
def structure():
    return render_template('structure.txt')

@app.route('/reboot')
def restart():
    os.system("echo 'reboot' > reboot")
    return 'restarting server'

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/loop')
def rickroll():
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        app.logger.debug(f"{username = }:{password = }")
        if username == dummy_user['username'] and password == dummy_user['password']:
            # Successful login
            return render_template('inside.html')
        else:
            # Failed login
            return 'Invalid credentials. Please try again te balfasz.'
    except Exception as e:
        app.logger.error(f"An error occured: {str(e)}", exc_info=True)
        return "Gebasz", 500
if __name__ == '__main__':
    app.run(debug=True)
