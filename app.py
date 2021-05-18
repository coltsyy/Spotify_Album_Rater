from flask import Flask;

app = Flask(__name__)


@app.route('/sugon')
def hello():
    return 'Garglon deez'