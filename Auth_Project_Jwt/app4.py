
#pip install flask-jwt-extended
from flask_jwt_extended import create_access_token,JWTManager,jwt_required,get_jwt_identity,create_refresh_token,get_jwt

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

jwt=JWTManager()
jwt.init_app(app)

block_list = set()

@jwt.token_in_blocklist_loader
def check_if_token_in_block_list(jwt_header,jwt_payload):
    jti=jwt_payload['jti']
    return jti in block_list

# test  --Authoriztion
# {
#     "msg": "Token has expired"
# }
# revoke  post
#
# {
#     "msg": "Token has expired"
# }

# test --token logout
# {
#     "msg": "Token has expired"
# }

@app.route("/token",methods=["POST"])
def createtoken():
    data=request.get_json()
    username=data["username"]
    password=data['password']
    print(username,password)
    #check_user=User.query.filter_by(name=data["username"]).first()
    #if check_user:
    access_token=create_access_token(identity=username,fresh=True)
    refresh_token=create_refresh_token(identity=username)
    return jsonify({"access_token":access_token,"refresh_token":refresh_token})

#http://127.0.0.1:5000/test
@app.route('/test',methods=["GET","POST"])
@jwt_required(optional=True)
#@jwt_required(optional=False) if optional is False token is mandatory
def mytest():
    current_user=get_jwt_identity()
    print(current_user)
    #return jsonify({'message':'test method sucessful'})
    if current_user:
        return jsonify({'message':'thanks for wearing your badge'})
    else:
        return jsonify({'message': 'warning disciplinary action wiil take next time'})


@app.route("/refresh",methods=["POST"])
@jwt_required(refresh=True)
def refresh_token():
    current_user=get_jwt_identity()
    new_current_token=create_access_token(identity=current_user,fresh=False)
    return jsonify({"new_current_token":new_current_token})


@app.route("/revoke",methods=["POST"])
@jwt_required()
def revoke_token():
    jti=get_jwt()['jti']
    block_list.add(jti)
    return jsonify({"Message":"logged out successfully."})


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
                # as per jwt documentation please use "exp" instead of "expiry" #https://jwt.io/  go to website
                print(token)
                return jsonify({"message":" correct username "+data["username"], "token":token})
        else:
            return jsonify({"message": "Invalid user and password"})

        # else:
        #     return jsonify({"message":"Invalid user and password"})


@app.route('/users',methods=['GET'])
#@token_required
def alluserlist():
    if request.method == 'GET':
        users = User.query.all()
        user_list=[]
        for user in users:
            user_list.append(user.name)
        return jsonify(user_list)

if __name__ == "__main__":
    app.run()

#1.http://127.0.0.1:5000/token
# {
#     "username":"teju",
#     "password":"123"
# }

# {
#     "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjYzMzA2NjIwLCJqdGkiOiJjNDZkMjRiYy0yZTczLTQ2MTktODZmNS01ZDMwNmMzNDQxMmIiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoidGVqdSIsIm5iZiI6MTY2MzMwNjYyMCwiZXhwIjoxNjYzMzA3NTIwfQ.m86qbLieWn5x-EPeBy9Py-DFB_18oYq5I_YV3SFdbzc",
#     "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzMwNjYyMCwianRpIjoiZDM3YzBiMGYtOGRhYy00MjI3LThmNWEtMjZlNGE1ZmU5MDQwIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJ0ZWp1IiwibmJmIjoxNjYzMzA2NjIwLCJleHAiOjE2NjU4OTg2MjB9.FF9C_iHQL86_QJU7Ox8s-8wexnC62SLpIEwM69lRDJE"
# }
#2.http://127.0.0.1:5000/refresh  post -- using refresh_token

#Hearders:
#Authorization
#Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzMwNjYyMCwianRpIjoiZDM3YzBiMGYtOGRhYy00MjI3LThmNWEtMjZlNGE1ZmU5MDQwIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJ0ZWp1IiwibmJmIjoxNjYzMzA2NjIwLCJleHAiOjE2NjU4OTg2MjB9.FF9C_iHQL86_QJU7Ox8s-8wexnC62SLpIEwM69lRDJE

#out put token
#{
    #"new_current_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzMwNjY0MSwianRpIjoiZjMzZDc4ZmMtMGIwNy00MzUwLWE2ZDEtMjFmOWJhZWI0Y2U1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlanUiLCJuYmYiOjE2NjMzMDY2NDEsImV4cCI6MTY2MzMwNzU0MX0.g9B_aOoJXC7cIAwJzoTX4dw2uN5AFkf_MYjmqsAnu34"
#}

#2. http://127.0.0.1:5000/test get --new_current_token
# header add
#Authorization  Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzIyNjI1NCwianRpIjoiODhiZGVmODktMGM1YS00MzAxLWIwOTItYjEyODE3Mzc5NDJhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlanUiLCJuYmYiOjE2NjMyMjYyNTQsImV4cCI6MTY2MzIyNzE1NH0.SCQ2MiwD29Ypah9JQI4uSdYz5YPmBqfo7udEiDpF7hY
#{
    #"message": "test method sucessful"
#}