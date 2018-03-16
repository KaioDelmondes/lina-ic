import os
from werkzeug.utils import secure_filename
from readData import readData
import inputs

'''
Método responsável por obter as inputs que serão
renderizadas no formulário da página inicial.
'''
def get_inputs():
    return inputs.inputs

'''
Método responsável por salvar o arquivo no servidor.
Parâmetro: 
    file: arquivo advindo da request.
Retorna o nome do arquivo.
'''
def save_file(file):
    filename = secure_filename(file.filename)
    file.save(os.path.join('databases', filename))
    return filename

'''
Método responsável por encaminhar a execução dos algoritmos.
Busca o arquivo salvo através do filename.
Discretização.
Classificação.
Retorna.
'''
def main(data):
    base = readData(os.path.join('databases', data['filename']))
    discretization(data, base)
    classificar()

def discretization(data, base):
    method = data['alg_disc']
    bdd, infor, grupos = base.dataPreparation()#(method)

def classificar():
    pass