#!/usr/bin/env python3
#import Flask and jsonify from flask
from flask import Flask,jsonify
#create an app using __name__ variable when the python
#program in interpreted.
app = Flask(__name__)

#import engine and sessionmaker from sqlalchemy to connect
#to the database and create sessions.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#import Base and TwitterData class from database_setup.py to 
#access the data in the database.
from database_setup import Base, TwitterData

#Using create_engine to connect to the database.db 
#that was created using database_setup.py.
engine = create_engine('sqlite:///database.db')
#Binding Base class to the engine that we just created.
Base.metadata.bind=engine

#Creating session to perform CRUD(Create,Read,Update, and Delete) operations.
DBSession = sessionmaker(bind=engine)
session = DBSession()

#creating URL route for WITBRAGDAY 
@app.route('/twitterData/WITBRAGDAY')
def twitterDataJSON():
	#Get all the data from TwitterData and save it in Data.
	Data = session.query(TwitterData).all()
	#Using Jsonify function from flask to access each piece of
	#information from Data and use serialize property defined
	# in database_setup.py to create JSON objects.
	return jsonify(Tweets = [i.serialize for i in Data] )
#creating URL route for WITBRAGDAY when tweets are filtered by id.
@app.route('/twitterData/<int:id>/JSON')
def twitterDataPerIDJSON(id):
	#Get information on each tweet filtered by id and save it into Data.
    Data = session.query(TwitterData).filter_by(id = id).all()
    #Using jsonify function from flask to access the tweets from Data and use
    #serialize property in database_setup.py to create JSON objects.
    return jsonify(Tweets = [i.serialize for i in Data])
#if the program is interpreted using python, do the following.
if __name__ == '__main__':
    #app.secret_key = 'super_secret-key'
    #Everytime, there is a change in code, the server automatically reloads.
    app.debug = True
    # App is going to run on the localhost with port number, 5000.
    app.run(host = '0.0.0.0', port = 5000)
