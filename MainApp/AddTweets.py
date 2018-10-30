#!/usr/bin/env python3
#importing required functions from sqlalchemy.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#Importing the Base class and TwitterData class from database_setup.py
from database_setup import Base, TwitterData
#Importing CSV library to read the CSV file.
import csv

#Create engine and connect to the database.
engine = create_engine('sqlite:///database.db')
#Binding the base class to the engine that we just created
Base.metadata.bind = engine
#Create a session so that we can perform Create,Read,Update and Delete operations.
DBSession = sessionmaker(bind = engine)
session = DBSession()
#Accessing the CSV file encoding it with latin1. IF original CSV has latin characters,
#then encode it.
with open('WitBrag.csv',encoding ='latin1') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Each column of CSV file is being added to the columns of the table.
        AddTweet =  TwitterData(Text = row['Text'], Hashtags = row['Hashtags'], 
                    FavCount = row['FavCount'], Language = row['Language'],Place = row['Place'], 
                    UserLocation= row['UserLocation'],RetweetCount = row['RetweetCount'],
                    Sentiment = row['Sentiment'], Polarity = row['Polarity'])
        #Using session to add the newly added tweets in the database.
        session.add(AddTweet)
        #commit the session so that the effect is reflected on the database.
        session.commit()

