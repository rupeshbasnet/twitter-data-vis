#!/usr/bin/env python3
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# declarative_base() is a factory function that constructs a base class for 
# declarative class definitions so that we can construct other classes using
# Base variable.
Base = declarative_base()

#Every class corresponds to the table in the database.
class TwitterData(Base):
    __tablename__ = 'twitterdata'
    #Creating the columns for our table with respective datatypes.
    Text = Column(String(2000))
    Hashtags = Column(String(250))
    FavCount = Column(String(10))
    Language = Column(String(10))
    Place = Column(String(100))
    UserLocation = Column(String(100))
    RetweetCount = Column(String(10))
    Date = Column(String(100))
    Sentiment = Column(String(300))
    Polarity = Column(String(20))
    id = Column(Integer, primary_key=True)

    # Function Declaration for Flask API.
    @property
    # serialize property will be used to call the JSON properties
    # as defined below.
    def serialize(self):
        return {
               # Declaring the way how the JSON will be represented.
              'Hashtags' : self.Hashtags,
              'FavCount' : self.FavCount,
              'Language' : self.Language,
              'Place'    : self.Place,
              'UserLocation': self.UserLocation,
              'RetweetCount': self.RetweetCount,
              'Sentiment'   : self.Sentiment,
              'Polarity'    : self.Polarity,
              'id'       : self.id, 
              'Text'        : self.Text,
        }
# 
engine = create_engine('postgresql://ankit:chhewang@localhost/twitter')
Base.metadata.create_all(engine)