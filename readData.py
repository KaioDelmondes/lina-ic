import pandas as pd 
import numpy as np
import discretizador as disc


# Classe ReadData
# Recebe o caminho do arquivo csv já agrupado
# O método leitorCSV divide os dados em dataframes, um para cada grupo, retirando o atributo cluster da tabela
# Retorna uma lista de DF dos grupos  e a base original

class readData (object):
	
	def __init__(self, file):
		self.db = pd.read_csv(file,sep=',',parse_dates=True)   # read_csv carrega um arquivo csv

	def criarsubconjunto(self, data):
		grup = pd.DataFrame(data)
		return grup				

	def agrupador(self):
		
		col = self.db.shape[1]-1                                    # shape retorna uma tupla com o número de linhas e colunas - col armazena o numero de colunas
		bdd = self.db.drop(self.db.columns[col], axis=1)
		bdd, infor = disc.discretizador(bdd.get_values(), [3,3,3,3], "EFD")

		nova_ma = np.zeros((bdd.shape[0], bdd.shape[1]+1))
		nova_ma[:,:col] = bdd
		nova_ma[:,col] = self.db.get_values()[:,col]
		bdd = self.criarsubconjunto(nova_ma)
		
		grouped = bdd.groupby(bdd.columns[col])                  # agrupa os dados pelo atributo cluster
				
		# cria um conjunto de dataframes, cada dataframe representa um grupo
		frames = [] 								           
		for j in range(0, len(grouped)):
			cluster = grouped.get_group(j)
			cluster = cluster.drop(cluster.columns[[col]],axis = 1) 
			frames.append(self.criarsubconjunto(cluster.get_values()))
		return bdd, infor, frames

	
