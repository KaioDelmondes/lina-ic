from lesscss import LessCSS
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from controller import main
import inputs

app = Flask(__name__)

LessCSS(media_dir='static', compressed=False)

@app.route("/")
def server():
    data = inputs.get_inputs()
    return render_template('index.html', inputs=data)

@app.route("/exec", methods=['POST'])
def executar():
    data = {
        'alg_disc' : request.form['alg_disc'],
        'alg_clas' : request.form['alg_clas'],
        'faixas' : request.form['faixas'],
        'treino' : request.form['treino'],
        'varv' : request.form['varv'],
    }
    file = request.files['database']
    #main(data, file)
    return jsonify(data)


# Usado para executar no Windows
if __name__ == "__main__":
    app.run()
