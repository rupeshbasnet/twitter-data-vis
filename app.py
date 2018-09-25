from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        userInput = request.form['userInput']

        # Once we get the user input we will process it with the Twitter
        # Sentiment Analysis Pipeline and display the results/Visualization

    return render_template('index.html', output = userInput)

if __name__ == '__main__':
    app.run(debug=True)
