# post man login and signup methods to database suing 
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256
import pymysql
from flask import Flask,request,jsonify
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:welcome$1234@localhost/authenticationdb'
app.config["SECRET_KEY"] = "My secret key"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80),  nullable = False)
    password = db.Column(db.String(150), nullable = False)


# {
#     "username":"prasham",
#     "password":"123"
# }
@app.route('/signup',methods=["POST"])
def signup():
    if request.method == "POST":
        userdata = request.get_json()
        pwd = pbkdf2_sha256.hash(userdata["password"])
        userslist = User.query.all()
        for userinfo in userslist:
            if userinfo.name == userdata["username"]:
                return jsonify({"message": "already user signup"})
        else:
            new_user = User(name=userdata["username"], password=pwd)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message":"New user created"})


@app.route('/login',methods=["POST"])
def login():
    if request.method == 'POST':
        data = request.get_json()
        users = User.query.all()
        for user in users:
            if user.name == data["name"] and pbkdf2_sha256.verify(data["password"],user.password):
                return jsonify({"message": "username " + data["name"]})
        else:
            return jsonify({"message":"Invalid user and password"})


@app.route('/users',methods=['GET'])
def alluserlist():
    if request.method == 'GET':
        users = User.query.all()
        user_list=[]
        for user in users:
            user_list.append(user.name)
        return jsonify(user_list)

if __name__ == "__main__":
    app.run()
