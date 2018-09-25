from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
from passwords import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

TWITTER_KEY = API_KEY
TWITTER_KEY_SECRET = API_SECRET_KEY
TWITTER_TOKEN = ACCESS_TOKEN
TWITTER_TOKEN_SECRET = ACCESS_TOKEN_SECRET

app = Flask(__name__)
Bootstrap(app)

auth = tweepy.OAuthHandler(consumer_key=TWITTER_KEY, consumer_secret=TWITTER_KEY_SECRET)
auth.set_access_token(TWITTER_TOKEN, TWITTER_TOKEN_SECRET)
api = tweepy.API(auth)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        userInput = request.form['userInput']
        # Once we get the user input we will process it with the Twitter
        # Sentiment Analysis Pipeline and display the results/Visualization
        tweets = tweepy.Cursor(api.search, q=userInput, lang="English").items(30)

        positiveCount = 0
        negativeCount = 0
        neutralCount = 0
        sentiments = 0
        for tweet in tweets:
            textAnalysis = TextBlob(tweet.text)
            sentiments += textAnalysis.sentiment.polarity
            if (textAnalysis.sentiment.polarity == 0):
                neutralCount += 1
            elif (textAnalysis.sentiment.polarity < 0.00):
                negativeCount += 1
            elif (textAnalysis.sentiment.polarity > 0.00):
                positiveCount += 1

    return render_template('index.html', neutralCount = neutralCount,
                                         negativeCount = negativeCount,
                                         positiveCount = positiveCount)

if __name__ == '__main__':
    app.run(debug=True)
