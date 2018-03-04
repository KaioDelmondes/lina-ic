import pandas as pd 
import numpy as np
import discretizador as disc


# Classe ReadData
# Recebe o caminho do arquivo csv já agrupado
# O método leitorCSV divide os dados em dataframes, um para cada grupo, retirando o atributo cluster da tabela
# Retorna a base de dados discretizada, as informações da discretização e um frame de cada grupo

class readData (object):
	
	def __init__(self, file):
		self.db = pd.read_csv(file,sep=',',parse_dates=True)   # read_csv carrega um arquivo csv

	def criarsubconjunto(self, data):
		grup = pd.DataFrame(data)
		return grup				

	def agrupador(self):
		col = self.db.shape[1]-1                                    # shape retorna uma tupla com o número de linhas e colunas - col armazena o numero de colunas
		data = self.db.drop(self.db.columns[col], axis=1)		    # data copia os valores da base de dados ignorando o atributo cluster
		bdd_, infor = disc.discretizador(data.get_values(), [3,3,3,3], "EFD") # bdd_ recebe os valores da base discretizados
		
		# Sobrescreve a base de dados original (db) com os atributos discretizados
		for x in range (0,col):
			self.db.loc[:,self.db.columns[x]] = [y[x] for y in bdd_]
		
		# agrupa os dados pelo atributo cluster	
		grouped = self.db.groupby(self.db.columns[col])                 
				
		# cria um conjunto de dataframes, cada dataframe representa um grupo
		frames = [] 								           
		for j in range(0, len(grouped)):
			cluster = grouped.get_group(j)
			cluster = cluster.drop(cluster.columns[[col]],axis = 1) 
			frames.append(self.criarsubconjunto(cluster.get_values()))

		#retorna a base de dados discretizada, as informações da discretização e um frame de cada grupo
		return self.db, infor, frames

#caminho = "C:\\Users\\LuciaEmilia\\Desktop\\iris.csv"
	
