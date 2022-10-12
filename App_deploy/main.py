#print('Hello')
#pip install flask
#pip freeze > requirements.txt
#web: gunicorn <name>:app
#bhaskar-flask
from flask import Flask
import os
app=Flask(__name__)



@app.route("/")
def Home_page():
    return ("<h1>Welcome to the Home Page</h1>")

port =int(os.environ.get("PORT",5000))

if __name__== "__main__":
    app.run(port=port)


# git commands in terminal
#(venv) PS D:\Git_Assignments\App_deploy>
# git init
# git status
# git commit -am "added first app main"
# git push heroku master

#pip freeze > requirements.txt

# heroku login

# https://bhaskar-flask.herokuapp.com/
