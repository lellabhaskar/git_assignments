# # Task for implement of jwt -javascript web token
# from flask import Flask
#
# from flask_sqlalchemy import SQLAlchemy
#
# #pip install flask-sqlalchemy
# #pip install pyjwt
# #pip install flask
#
# from flask import request
# from flask_restful import Api,Resource
# from http import HTTPStatus
# #from passlib.hash import pbkdf2_sha256
# #import jwt
# import uuid
#
# app=Flask(__name__)
# api=Api(app)
#
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:welcome$1234@localhost/authenticationdb"
# db=SQLAlchemy(app)
#
# @app.route("/")
# def home():
#     return "<h1>welcome home page and use methods for /signup  and /login</h1>"
#
# # @app.route("/signup",methods=['POST'])
# # def signup():
# #     if request.method == 'POST':
# #         data=request.get_json()
# #         name=data["username"]
# #         password=data["password"]
# #         conn = pymysql.connect(user='root', password='welcome$1234', host='127.0.0.1', database='authenticationdb')
# #         cur = conn.cursor()
# #         user_data = f"insert into user (name,password) values('{name}','{password}' )"
# #         print(user_data)
# #         try:
# #             cur.execute(user_data)
# #             conn.commit()
# #             print("1 row inserted")
# #         except Exception as ex:
# #             print('Error')
# #             message = f'''An exception of type {type(ex).__name__} occured.Arguments:{ex.args}'''
# #             print(message)
# #             conn.rollback()
# #         finally:
# #             cur.close()
# #             conn.close()
# #
# #     return "<h2> new user created successfully.<h2>"
# #
# # @app.route("/login",methods=['POST'])
# # def login():
# #     data = request.get_json()
# #     user = data["username"]
# #     password = data["password"]
# #     print(user)
# #
# #     check_user = user_check(user,password)
# #     #print(check_user)
# #     if check_user:
# #         return "login successfully"
# #     else:
# #         return "login failed"
# #
# # def user_check(user,password):
# #     sql_query = f"select * from  user where name= '{user}' and '{password}' "
# #     conn = pymysql.connect(user='root', password='welcome$1234', host='127.0.0.1', database='authenticationdb')
# #     cur = conn.cursor()
# #     cur.execute(sql_query)
# #     print(cur.execute(sql_query))
# #     conn.commit()
# #
#
#
# class signup(Resource):
#     def post(self):
#         data=request.get_json()
#         User.add_user(name=data['name'],password=pbkdf2_sha256.hash(data['password']))
#         return  {'message':'added success','status':HTTPStatus.OK}
#
# class login(Resource):
#     def post(self):
#         data=request.get_json()
#         name=data['name']
#         password=data['password']
#         check_user=User.matching_credentails(name,password)
#         #jwt token code
#         #token=jwt.encode({"public_id":public_id})
#         if check_user:
#             return {'message':'login sucess','status':HTTPStatus.OK}
#         else:
#             return {'message':'login failed','status':404}
# class User(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.string(80),nullable=False)
#     password=db.Column(db.string(200),nullable=False)
#
#     @staticmethod
#     def add_user(name,password):
#         #public_id = str(uuid.uuid4())
#         new_user=User(name=name,password=password)
#         #new_user = User(name=name, password=password,public_id=public_id)
#         db.session.add(new_user)
#         db.session.commit()
#
#     @staticmethod
#     def matching_credentails(name, password):
#         data=User.query.all()
#         for i in data:
#             if (i,name==name):
#                 if pbkdf2_sha256.verify(password,i.password):
#                     return True
#                 else:
#                     return False
# # @app.route("/users")
# # def allusers():
#
#
# api.add_resource(User,"/signup")
# api.add_resource(User,"/login")
#
#
# if __name__=="__main__":
#     app.run()
#
# # tasks
# #1.POST /login
# # create a db and a table lets' name it as User
# #2.POST /signup
# # User will have id,name and hashed password
# #3  POST /signup
# #4 POST /login (only name and password)
#
#
#
# #1 Task POST method using postman:
# # http://127.0.0.1:5000/signup
#
# # please mention in the body of postman
# #{
#     #"username":"Bhaskar",
#     #"password":"test123"
# #}
#
# #2 Task GET method
# # http://127.0.0.1:5000/login
#
