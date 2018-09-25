import tweepy
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from textblob import TextBlob

TWITTER_KEY = "5DBafM7qC12MFBEG5zJQk4gGd"
TWITTER_KEY_SECRET = "sX0oQmylHOO3s8w4yCUmXnlrM6grMuvZq0TQOEYsj6ZuMaG0XO"
TWITTER_TOKEN = "826979343075332096-9dx6GiMDw1lKSRR51tgBU4Gthjacq44"
TWITTER_TOKEN_SECRET = "8Zt0sa8qspou4j8VKqZzhMWLwlzwToPf7QxPd4CyrJlZT"

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
