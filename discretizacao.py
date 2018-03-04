import pandas as pd

# Classe de discretizacao de dados 
# Recebe como parâmetros a lista de atributos (attr_list) a serem discretizados e o número de faixas desejado (num_bins)
# Retorna a lista de atributos discretizada (discr_list)
class discretization (object):
	
	def __init__ (self, attr_list, num_bins):
		self.attr_list = attr_list
		self.num_bins = num_bins		

	#Testa se a lista de valores recebida é discreta, retornando True, ou contínua, retornando False.
	def teste (self):
		unics = sorted(set(self.attr_list))
		if len(unics)<self.num_bins: 
			return True
		else: 
			return False 

	# Discretiza os dados pelo critério de larguras iguais. Retorna faixas de valores com aproximadamente o mesmo tamanho.
	def EWD (self):
		if not self.teste():
			discr_attr = pd.cut(self.attr_list, bins = self.num_bins, labels = False, retbins= True)
			return discr_attr
		else :
			return self.attr_list
			
	# Disretiza os dados pelo critério de frequências iguais.Retorna faixas de valores com aproximadamente o mesmo número de dados.
	def EFD (self):
		if not self.teste():
			discr_attr = pd.qcut(self.attr_list, self.num_bins, labels = False, retbins = True, duplicates = 'drop')
			return discr_attr
		else: 
			return self.attr_list


	
