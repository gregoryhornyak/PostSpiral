from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os
import json
import datetime

app = Flask(__name__)

#logging.basicConfig(filename="/home/ubuntu/flask_app/app.log", level=logging.DEBUG)

module_path = os.path.abspath(__file__)
print("Path of the module:", module_path)

@app.route('/')
def hello():
    return render_template('welcome.html')
    #render_template('map.html',date=datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H:%M:%S"))

@app.route('/test')
def test():
    return render_template('test_letter.html')

@app.route('/how')
def structure():
    return render_template('structure.txt')

@app.route('/loginpage')
def main():
    return render_template('main.html')

@app.route('/loop')
def rickroll():
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@app.route('/login', methods=['POST'])
def login():
    users_json = {}
    with open("/var/www/html/flask_app/users.json","r") as users:
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
    
@app.route('/readIssue/<issueName>', methods=['GET'])
def currentIssue(issueName):
    newsletter_json = {}
    with open("/var/www/html/flask_app/newsletters.json","r") as file:
        newsletter_json = json.load(file)
    users_json = {}
    with open("/var/www/html/flask_app/users.json","r") as file2:
        users_json = json.load(file2)
    try:
        thread = []
        for nl_id,nl_data in newsletter_json.items():
            for issue_id,issue_data in nl_data["issues"].items():
                if issue_data["name"] == issueName:
                    # issue exists
                    thread = []
                    for q in issue_data["assets"].values():
                        querier = ""
                        if q["querier"] in users_json.keys():  
                            querier = users_json[q["querier"]]["username"]
                        else:
                            querier = q["querier"]
                        thread.append(f'{querier}: {q["question"]}')
                        for a in q["answers"].values():
                            respondent = ""
                            if a["respondent"] in users_json.keys():  
                                respondent = users_json[a["respondent"]]["username"]
                            else:
                                respondent = a["respondent"]
                            thread.append(f'  - {respondent}: {a["answer"]}')
                    break
        return render_template("newsletter.html",thread=thread)
    except Exception as e:
        return str(e), 500
    

if __name__ == '__main__':
    app.run(debug=True)
