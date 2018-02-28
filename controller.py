import os
from werkzeug.utils import secure_filename
from readData import readData
from discretizador import discretizador

def main(data, file):
    filename = secure_filename(file.filename)
    file.save(os.path.join('databases', filename))
    print(os.path.join('databases', filename))
    rd = readData(os.path.join('databases', filename))
    bd, frames = rd.leitorCSV()
    discretizar(data, bd)
    classificar()

def discretizar(data, bd):
    metodo = data['alg_disc']
    a, b = discretizador(bd, [3,3,3,3], metodo)
    return a, b

def classificar():
    pass