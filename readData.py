import pandas as pd 
import numpy as np
from discretizacao import discretization as disc


# Classe ReadData
# Recebe o caminho do arquivo csv já agrupado
# Retorna a base de dados discretizada, as informações da discretização e um frame de cada grupo


class readData (object):
	
	def __init__(self, file):
		self.db = pd.read_csv(file,sep=',',parse_dates=True)  

	# makeDF - Método para construção de DataFrames. 
	# Recebe um conjunto de dados (data) e retorna o DataFrame (df)
	def makeDF(self, data):
		df = pd.DataFrame(data)
		return df	
	
	#agroup - Método para divisão da base de dados em um conjunto de dataframes de acordo com o atributo cluster
	# Recebe um DataFrame (data). Retorna um conjunto de DataFrames (frames)
	def agroup(self, data):
		# calcula a quantidade de colunas do dataframe
		col = data.shape[1]-1      		

		# agrupa os dados pelo atributo cluster	
		grouped = data.groupby(data.columns[col])                
				
		# cria um conjunto de dataframes, cada dataframe representa um grupo
		frames = [] 								           
		for j in range(0, len(grouped)):
			cluster = grouped.get_group(j)
			cluster = cluster.drop(cluster.columns[[col]],axis = 1) 
			frames.append(self.makeDF(cluster.get_values()))		
		
		return frames				

	#discretization - Método de discretização da base de dados
	# Recebe um ndarray da base de dados (db), um vetor com o número de faixas para cada atributo (num_bins)
	# e o método de discretização escolhido (method). Retorna um ndarray com a base de dados discretizada (ddb)
	# e os limites de cada faixa (info)
	def discretization (self,db,num_bins,method):
		ddb = []
		info = []
		
		# Para cada atributo, chama a classe de discretização, passando como
		# parâmetro a coluna do atributo e o número de faixas desejado
		for j in range(0, len(num_bins)):
			attr = disc(db[:,j], num_bins[j])
			if method is "EFD":
				disc_attb = (attr.EFD())
			elif method is "EWD":
				disc_attb = (attr.EWD())
			ddb.append(disc_attb[0])
			info.append(disc_attb[1])
		
		ddb = np.asarray(ddb, dtype = 'int32')
		
		return ddb.T, info

	def dataPreparation(self):
		col = self.db.shape[1]-1                                    # shape retorna uma tupla com o número de linhas e colunas 
		data = self.db.drop(self.db.columns[col], axis=1)		    # data copia os valores da base de dados ignorando o atributo cluster
		
		#Copia a base de dados original
		ddb = self.db.copy()
		
		# Chama o método de discretização
		ddb_, info = self.discretization(data.get_values(),[3,3,3,3,3,3,3,3,3,3,3],"EFD" )
		
		# Sobrescreve ddb com os atributos discretizados
		for x in range (0,col):
			ddb.loc[:,ddb.columns[x]] = [y[x] for y in ddb_]
		
		# Divide a base discretizada em dataframes de acordo com a atributo cluster
		frames = self.agroup(ddb)		
		
		#Retorna a base de dados discretizada, as informações da discretização e um frame de cada grupo
		return ddb, info, frames

#caminho = "C:\\Users\\LuciaEmilia\\Desktop\\iris.csv"