from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)




if __name__ == '__main__':
    app.run(debug=True)
