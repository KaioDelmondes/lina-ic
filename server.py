from lesscss import LessCSS
from flask import Flask
from flask import render_template
app = Flask(__name__)

LessCSS(media_dir='static', compressed=False)

@app.route("/")
def server():
    return render_template('index.html')