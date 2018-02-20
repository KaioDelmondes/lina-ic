import pandas as pd

# Classe de discretizacao de dados 
# Recebe como parâmetros a lista de dados a serem discretizados e o número de faixas desejado

class discretizacao (object):
	
	def __init__ (self, lista, numIntervalos):
		self.lista = lista
		self.numIntervalos = numIntervalos		

	#Testa se a lista de valores recebida tem intervalo maior que zero, ou seja, todos os dados sao iguais.
	def teste (self):
		unics =  sorted(set(self.lista))
		if len(unics)<2: 
			return True
		else: 
			return False 

	# Discretiza os dados pelo critério de larguras iguais, ou seja, retorna faixas de valores com aproximadamente o mesmo tamanho.
	def EWD (self):
		if not self.teste():
			dados_discr = pd.cut(self.lista, bins = self.numIntervalos, labels = range(self.numIntervalos),retbins= True)
			return dados_discr
		else :
			return 'Dados iguais.'
			
	# Disretiza os dados pelo critério de frequências iguais, ou seja, retorna faixas de valores com aproximadamente o mesmo número de dados.
	def EFD (self):
		if not self.teste():
			dados_discr = pd.qcut(self.lista, self.numIntervalos, labels = range(self.numIntervalos), retbins = True, duplicates = 'drop')
			return dados_discr
		else: 
			return 'Dados iguais'


	
