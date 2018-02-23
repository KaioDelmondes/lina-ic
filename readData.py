import pandas as pd 
import numpy as np


# Classe ReadData
# Recebe o caminho do arquivo csv já agrupado
# O método leitorCSV divide os dados em dataframes, um para cada grupo, retirando o atributo cluster da tabela
# Retorna uma lista de DF dos grupos  e a base original

class readData (object):
	
	def __init__(self, file):
		self.file = file 

	def criarsubconjunto(self, data):
		grup = pd.DataFrame(data)
		return grup		

	def leitorCSV(self):
		db = pd.read_csv(self.file,sep=',',parse_dates=True)   # read_csv carrega um arquivo csv
		col = db.shape[1]-1                                    # shape retorna uma tupla com o número de linhas e colunas - col armazena o numero de colunas
		grouped = db.groupby(db.columns[col])                  # agrupa os dados pelo atributo cluster
				
		# cria um conjunto de dataframes, cada dataframe representa um grupo
		frames = [] 								           
		for j in range(0, len(grouped)):
			cluster = grouped.get_group(j)
			cluster = cluster.drop(cluster.columns[[col]],axis = 1) 
			frames.append(self.criarsubconjunto(cluster.get_values()))
		return db, frames

	