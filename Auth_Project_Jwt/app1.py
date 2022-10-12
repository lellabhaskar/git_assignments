#jwt token validation
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256
import jwt
import uuid
import pymysql
import time
from datetime import datetime,timedelta
from flask import Flask,request,jsonify
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:welcome$1234@localhost/authenticationdb'
app.config["SECRET_KEY"] = "My secret key"
db = SQLAlchemy(app)

##use hearders in post man Key --x-access-token value ==token  --request --get
def token_required(f):
    def decorated(*args,**kwargs):
        token=None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({"message":"Token is missing"})
        else:
            #pass
            # data=jwt.decode(token,app.config["SECRET_KEY"],algorithms=["HS256"])
            # print(data)
            # current_user=User.query.filter_by(public_id=data["public_id"]).first()
            # if current_user:
            #     return f()
            # else:
            #     return jsonify({'message':'token invalid'})
            try:
                data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
                print(data)
                current_user = User.query.filter_by(public_id=data["public_id"]).first()
                if current_user:
                    return f()
                else:
                    return jsonify({'message': 'token invalid'})
            except:
                return jsonify({'message': 'token invalid'})

    return decorated


class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    public_id = db.Column(db.String(150),unique = True)
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
            public_id = str(uuid.uuid4())
            new_user = User(name=userdata["username"], password=pwd,public_id=public_id)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message":"New user created"})


@app.route('/login',methods=["POST"])
def login():
    if request.method == 'POST':
        data = request.get_json()
        users = User.query.all()
        for user in users:
            print("inside login users")
            if user.name == data["username"] and pbkdf2_sha256.verify(data["password"],user.password):
                #return jsonify({"message": "username " + data["name"]})
                #token = jwt.encode({"public_id":user.public_id},app.config["SECRET_KEY"])
                token = jwt.encode({"public_id": user.public_id,
                                    "exp":datetime.utcnow()+timedelta(seconds=40)},
                                   app.config["SECRET_KEY"])
                # as per jwt documentation please use "exp" instead of "expiry"
                print(token)
                return jsonify({"message":" correct username "+data["username"], "token":token})
        else:
            return jsonify({"message": "Invalid user and password"})

        # else:
        #     return jsonify({"message":"Invalid user and password"})


@app.route('/users',methods=['GET'])
@token_required
def alluserlist():
    if request.method == 'GET':
        users = User.query.all()
        user_list=[]
        for user in users:
            user_list.append(user.name)
        return jsonify(user_list)

if __name__ == "__main__":
    app.run()

#1 python console
# form app1 import db
#db.create_all()