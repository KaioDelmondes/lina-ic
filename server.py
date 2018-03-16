from lesscss import LessCSS
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import controller

app = Flask(__name__)

# Configuração do Less
LessCSS(media_dir='static', compressed=False)

'''
URL responsável por renderizar a página inicial
Obtém os campos que serão renderizados no formulário
Renderiza a página inicial enviando os inputs.
'''
@app.route("/")
def server():
    data = controller.get_inputs()
    return render_template('index.html', inputs=data)

'''
URL responsável por realizar o upload do arquivo referente a base de dados
Obtém o arquivo advindo da request.
Salva o arquivo no servidor com um nome seguro.
Retorna o nome do arquivo
'''
@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['file']
    filename = controller.save_file(file)
    return filename

'''
URL responsável pela execução dos algoritmos
Obtém os dados advindos do formulário.
Envia os dados ao controller para que este cuide da execução dos algoritmos
Retorna os dados da execução dos algoritmos.
'''
@app.route("/exec", methods=['POST'])
def executar():
    data = {
        'filename' : request.form['filename'],
        'alg_disc' : request.form['alg_disc'],
        'alg_clas' : request.form['alg_clas'],
        'faixas' : request.form['faixas'],
        'treino' : request.form['treino'],
        'varv' : request.form['varv'],
    }
    controller.main(data)
    return jsonify(data)


# Usado para executar no Windows
if __name__ == "__main__":
    app.run()
