import os

from flask import Flask,request,jsonify,render_template
from flask_sqlalchemy import SQLAlchemy

from flask_restful import Api,Resource
from http import HTTPStatus
import pymysql

#flask-migrate
from flask_migrate import Migrate


class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://root:1234@localhost/moviedatabase2'


class Development_Config(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:1234@localhost/moviedatabase2'


class Production_Config(Config):
    uri=os.environ.get("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = uri


env = os.environ.get("ENV","Development")

if env == "Production":
    config_str=Production_Config
else:
    config_str=Development_Config

app= Flask(__name__)

app.config.from_object(config_str)

api=Api(app)

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#mysql database
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:welcome$1234@localhost/moviedatabase"

#postgre sql

#comments using Heroku
#app.config['SQLALCHEMY_DATABASE_URI']  = 'postgresql+psycopg2://root:1234@localhost/moviedatabase2'

# go to post gre sql follow the steps
#1.open postgre and right click on postgreSQL 14
#2. create -login /group rule
#3. General Tab -name -root , Definitions Tab-password -1234 and priviliges Tab-- can login? enable after save
#4.create database --General Tab database and owner should be root and save
db=SQLAlchemy(app)

#flask-migrate
migrate=Migrate(app,db)
        #1
# class user(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     username=db.Column(db.String(80),unique=True,nullable=False)
#     email=db.Column(db.String(120),unique=True,nullable=False)


        #1 run through python console
# from flasksqlalchemy_test import db
# db.create_all()



# class profile(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     username=db.Column(db.String(80),unique=True,nullable=False)
#     email=db.Column(db.String(120),unique=True,nullable=False)

        # 2 run through python console
    # from flasksqlalchemy_test import profile
    # admin=profile(username='bhaskar',email='lellabhaskar@gmail.com')
    # db.session.add(admin)
    # db.session.commit()

       #3
# from flasksqlalchemy_test import db
# db.create_all()

        #4
# from flasksqlalchemy_test import profile
# admin=profile(username='teja',email='teja@gmail.com')
# db.session.add(admin)
# db.session.commit()


        #5

#profile.query.all()
# [<profile 1>, <profile 3>, <profile 4>, <profile 5>]

# profile.query.filter_by(username='bhaskar').first()
# <profile 1>
# profile.query.filter_by(username='teja').first()
# <profile 5>
# profile.query.filter_by(username='siris').first()
# <profile 3>
# profile.query.filter_by(username='devaansh').first()
# <profile 4>


#             # 6 new movie
# class movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # this is the primary key
#     title = db.Column(db.String(80), nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     genre = db.Column(db.String(80), nullable=False)


      # task 1
#from flasksqlalchemy_test import profile
#db.create_all()



                     # 7 new movie using classes

# class Movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # this is the primary key
#     title = db.Column(db.String(80), nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     genre = db.Column(db.String(80), nullable=False)
#
#     @staticmethod
#     def add_movie(title, year, genre):
#         new_movie=Movie(title=title,year=year,genre=genre)
#         db.session.add(new_movie)
#         db.session.commit()
#
#     @staticmethod
#     def get_movies():
#         data=Movie.query.all()
#         return data
#
#
#
# class AllMovies(Resource):
#     def post(self):
#         data=request.get_json()
#         print(data)
#
#         Movie.add_movie(title=data["title"],year=data['year'],genre=data['genre'])
#         return ""
#
#
#     def get(self):
#         data=Movie.get_movies()
#         print(data)
#         movielst=[]
#
#         for moviedata in data:
#             dictmove={'title':moviedata.title,'year':moviedata.year,'genre':moviedata.genre}
#             movielst.append(dictmove)
#         return movielst
#
#

# api.add_resource(AllMovies,"/movies")
# app.run()




 # task 1
#from flasksqlalchemy_test import db
#db.create_all()

# task 2

# from flasksqlalchemy_test import movie
# add_movie=profile(title='aditya 365',year='1995',genre='')
# db.session.add(add_movie)
# db.session.commit()


                    # 8 get_id based on ID
# class Movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # this is the primary key
#     title = db.Column(db.String(80), nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     genre = db.Column(db.String(80), nullable=False)
#
#     @staticmethod
#     def add_movie(title, year, genre):
#         new_movie=Movie(title=title,year=year,genre=genre)
#         db.session.add(new_movie)
#         db.session.commit()
#
#     @staticmethod
#     def get_movies():
#         data=Movie.query.all()
#         return data
#


# class AllMovies(Resource):
#     def post(self):
#         data=request.get_json()
#         print(data)
#
#         Movie.add_movie(title=data["title"],year=data['year'],genre=data['genre'])
#         return ""
#
#
#     def get(self):
#         data=Movie.get_movies()
#         print(data)
#         movielst=[]
#
#         for moviedata in data:
#             dictmove={'title':moviedata.title,'year':moviedata.year,'genre':moviedata.genre}
#             movielst.append(dictmove)
#         return movielst



#api.add_resource(AllMovies,"/movies")

# run postman
#http://127.0.0.1:5000/movies

# class Movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # this is the primary key
#     title = db.Column(db.String(80), nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     genre = db.Column(db.String(80), nullable=False)
#
#     @staticmethod
#     def add_movie(title, year, genre):
#         new_movie=Movie(title=title,year=year,genre=genre)
#         db.session.add(new_movie)
#         db.session.commit()
#
#     @staticmethod
#     def get_movies():
#         data=Movie.query.all()
#         return data
#
#
# class AllMovies(Resource):
#     def post(self):
#         data=request.get_json()
#         print(data)
#         Movie.add_movie(title=data["title"],year=data['year'],genre=data['genre'])
#         return ""
#
#     def get(self):
#         data=Movie.get_movies()
#         print(data)
#         movielst=[]
#
#         for moviedata in data:
#             dictmove={'title':moviedata.title,'year':moviedata.year,'genre':moviedata.genre}
#             movielst.append(dictmove)
#         return movielst
#
#
# class OneMovie(Resource):
#     def get(self,id):
#         data=Movie.get_movies()
#         for movieone in data:
#             dicmovie={}
#             print(movieone)
#             if movieone.id == id:
#                 dicmovie['title']=movieone.title
#                 dicmovie['year'] = movieone.year
#                 dicmovie['genre'] = movieone.genre
#                 return jsonify(dicmovie)
#         else:
#              return jsonify({'message':'ID not found','status':404})

#
# api.add_resource(AllMovies,"/movies")
# api.add_resource(OneMovie,"/movies/<int:id>")
# app.run()

                # filter by option instead of for loop

# class Movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # this is the primary key
#     title = db.Column(db.String(80), nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     genre = db.Column(db.String(80), nullable=False)
#
#     @staticmethod
#     def add_movie(title, year, genre):
#         new_movie=Movie(title=title,year=year,genre=genre)
#         db.session.add(new_movie)
#         db.session.commit()
#
#     @staticmethod
#     def get_movies():
#         data=Movie.query.all()
#         return data
#
#     @staticmethod
#     def get_movie_id(id):
#         data=Movie.query.filter_by(id=id).first()
#         return data
#
#     @staticmethod
#     def get_movie_delete_id(id):
#         delmovie = Movie.query.filter_by(id=id).delete()
#         db.session.commit()
#         return delmovie
#
#
# class AllMovies(Resource):
#     def post(self):
#         data=request.get_json()
#         print(data)
#         Movie.add_movie(title=data["title"],year=data['year'],genre=data['genre'])
#         return "Sucessfully added the Movie"
#
#     def get(self):
#         data=Movie.get_movies()
#         print(data)
#         movielst=[]
#
#         for moviedata in data:
#             dictmove={'title':moviedata.title,'year':moviedata.year,'genre':moviedata.genre}
#             movielst.append(dictmove)
#         return movielst
#
#
# class OneMovie(Resource):
#     def get(self,id):
#         dicdata = {}
#         data=Movie.get_movie_id(id)
#         if data:
#             dicdata['title'] = data.title
#             dicdata['year'] = data.year
#             dicdata['genre'] = data.genre
#
#             return jsonify((dicdata),{'status':HTTPStatus.OK})
#         else:
#             #return jsonify({'message':'ID not found','status':404})
#             return jsonify({'message': 'ID not found', 'status': HTTPStatus.NOT_FOUND})
#
#     def delete(self,id):
#         onemovie=Movie.get_movie_delete_id(id)
#         print(onemovie)
#         if onemovie:
#             return "sucessfully deleted the movie id {0}".format(id)
#         else:
#             return jsonify({'message': 'ID not found', 'status': HTTPStatus.NOT_FOUND})
#
#
# api.add_resource(AllMovies,"/movies")
# api.add_resource(OneMovie,"/movie/<int:id>")
# app.run()

                # filter by option update
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)


    @staticmethod
    def add_movie(title, year, genre):
        new_movie=Movie(title=title,year=year,genre=genre)
        db.session.add(new_movie)
        db.session.commit()

    @staticmethod
    def get_movies():
        data=Movie.query.all()
        return data

    @staticmethod
    def get_movie_id(id):
        data=Movie.query.filter_by(id=id).first()
        return data

    @staticmethod
    def get_movie_delete_id(id):
        delmovie = Movie.query.filter_by(id=id).delete()
        db.session.commit()
        return delmovie

    @staticmethod
    def update(id,title,year,genre):
        updatemovie = Movie.query.filter_by(id=id).first()

        updatemovie.title=title
        updatemovie.year = year
        updatemovie.genre = genre

        db.session.commit()

class AllMovies(Resource):
    def post(self):
        data=request.get_json()
        print(data)
        Movie.add_movie(title=data["title"],year=data['year'],genre=data['genre'])
        return "Sucessfully added the Movie"

    def get(self):
        data=Movie.get_movies()
        print(data)
        movielst=[]

        for moviedata in data:
            dictmove={'id':moviedata.id,'title':moviedata.title,'year':moviedata.year,'genre':moviedata.genre}
            movielst.append(dictmove)
        return movielst


class OneMovie(Resource):


    def get(self,id):
        dicdata = {}
        data=Movie.get_movie_id(id)
        if data:
            dicdata['title'] = data.title
            dicdata['year'] = data.year
            dicdata['genre'] = data.genre

            return jsonify((dicdata),{'status':HTTPStatus.OK})
        else:
            return jsonify({'message': 'ID not found', 'status': HTTPStatus.NOT_FOUND})

    def delete(self,id):
        onemovie=Movie.get_movie_delete_id(id)
        print(onemovie)
        if onemovie:
            return "sucessfully deleted the movie id {0}".format(id)
        else:
            return jsonify({'message': 'ID not found', 'status': HTTPStatus.NOT_FOUND})

    def put(self,id):
        moviedata = request.get_json()
        Movie.update(id,moviedata['title'],moviedata['year'],moviedata['genre'])
        if moviedata:
            return "sucessfully updated the movie id {0}".format(id)
        else:
            return jsonify({'message': 'ID not found', 'status': HTTPStatus.NOT_FOUND})


api.add_resource(AllMovies,"/movies")
#api.add_resource(OneMovie,"/movie/<int:id>")
api.add_resource(OneMovie,"/movies/<int:id>")
#app.run()

@app.route("/")
def home_page():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()
    #app.run(port=5001)

#app.run(port=5001)
#npx kill-port 5000

#1.way
    # run on python console  and run the Python console
    #1. from movie import db
    #2. db.create_all()



#2.way  flask-migrate
    # Flask - Migrate command
    #pip install flask-migrate

# go to terminal write below commands

    #1. flask --app movie.py db init               --after running check migrations folder created under project
    #2. flask --app movie.py db migrate
    #3. flask --app movie.py db upgrade

    #4. check or validation purpose go to postgre SQL -- Table is created


#3 way heroku deployment changes

# create Procfile and add below
    #release: flask db upgrade
    #web: gunicorn movie:app

#go to Terminal
    #pip install gunicorn

#pip freeze > requirements.txt

# create new file .gitignore and add below lines
#venv/
#.idea/

# using git heroku deployment
#git init
#git status
# go the Heroku Deploy Tab and click --see below commands

#heroku login  after login using browser
#heroku git:remote -a bhaskar-movieapp
# git add .
# git commit -am "added movie app"
#git push heroku master

#error show due to old version
#remote: Error: Could not locate a Flask application. Use the 'flask --app' option, 'FLASK_APP' environment variable, or a 'wsgi.py' or 'app.py' file in the current
 #directory.

#relaease: flask --app movie.py db upgrade

#git status
#git add Procfile
#git commit -am "updated Procfile"
#git push heroku master

# 2nd times
# git add .
# git remote add origin bhaskar-movieapp
# git commit -m "added new home page files to movies"
# git push heroku master

#https://bhaskar-movieapp.herokuapp.com/

