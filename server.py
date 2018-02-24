from lesscss import LessCSS
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
app = Flask(__name__)

LessCSS(media_dir='static', compressed=False)

@app.route("/")
def server():
    return render_template('index.html')

@app.route("/exec", methods=['POST'])
def executar():
    alg_disc = request.form['alg_disc']
    alg_clas = request.form['alg_clas']
    faixas = request.form['faixas']
    treino = request.form['treino']
    varv = request.form['varv']
    file = request.files['database']
    return jsonify(alg_disc=alg_disc, alg_clas=alg_clas, faixas=faixas, treino=treino, varv=varv)


# Usado para executar no Windows
if __name__ == "__main__":
    app.run()
