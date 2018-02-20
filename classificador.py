from sklearn import tree
import numpy as np
from collections import Counter
from copy import copy

class classificador(object):
	"""Construtor da classe 'classificador'. 
	Parâmetros:
		metodo: Método de Aprendizagem Supervisionada de preferência(MLP ou Árvore de Decisão).
		cluster: conjunto de dados a serem usados na rede neural.
		perc_trein: a porcentagem de dados que será usada no treinamento da rede. O restante será usado como conjunto de teste.
	"""
	def __init__(self, metodo, cluster, perc_trein):
		super(classificador, self).__init__()
		self.cluster = cluster
		self.porc_treino = int(perc_trein*(self.cluster.shape[0]/100)) #Usa o perc_trein para definir quantas tuplas serão usadas no treino da MLP
		self.resultados = np.zeros((cluster.shape[1],10), dtype = np.float64) #Matriz de resultados retornados pelo método de classificação. Usada na linha 40.
		self.classificar(metodo)

	"""
		Método principal. Não recebe nada como parâmetro pois usa somente a matriz de dados(cluster) como entrada
		para os métodos 'fit' e 'score' pertencentes ao objeto 'clf'
	"""	
	def classificar(self, metodo):
		
		for i in range(0, 10):
			for j in range(0, self.cluster.shape[1]):
				#Define os conjuntos de treino e teste para cada iteração. Para deixar claro, cada iteração modifica o atributo
				#que será usado como atributo classe
				cj_treino,cj_teste = self.treino_teste(j) 
				clf = copy(metodo) #Instancia uma nova rede neutal multicamadas

				#Essa parte trata os dados para ficarem de acordo com o necessário para o treinamento da MLP
				target = self.cluster[:self.porc_treino,j]	#cria uma lista com o atributo classe usado na iteração corrente

				clf.fit(X = cj_treino, y = target) #Método que faz o treinamento da MLP.

				#Mesma intenção do trecho de código das linhas 27 e 28
				target = self.cluster[self.porc_treino:,j]
				self.resultados[j,i] = clf.score(cj_teste, target)	#Matriz resultados recebe a taxa de acerto [0, 1] da MLP treinada com o conjunto de treino


	"""Método auxiliar para separar conjunto de treino e de teste usando a coluna usada como atributo classe de acordo com a iteração corrente no método 'classificar'"""
	def treino_teste(self,j):
		

		#Cria o conjunto de teste/treino usando a quantidade de tuplas definidas pelo Atributo 'perc_trein' passado como parâmetro na instanciação do objeto
		treino = np.hstack((self.cluster[:self.porc_treino, :j], self.cluster[:self.porc_treino, j+1:]))
		teste = np.hstack((self.cluster[self.porc_treino:, :j],self.cluster[self.porc_treino:, j+1:]))
		return treino,teste

"""
	Método que apenas monta uma string com o rótulo final. Todos os dados usados para montar a string podem ser manipulados de forma separada.
	V: Valor V que 'define se o atributo é importante o suficiente para estar no rótulo'
	Parâmetros:
		cluster: o cluster a ser rotulado.
		infor: as informações obtidas na etapa de discretização. Úteis na obtenção das faixas de valores dos atributos.
		holdout_val: A matriz de resultados obtidos na fase de classificação do cluster.
		V: o valor V que irá destacar apenas os atributos mais importantes do cluster na montagem do rótulo.
	"""
def rotular(cluster, infor, holdout_val, V):
	
	medias = 100*(holdout_val.mean(1)) #Calcula a média de acerto para cada atributo do cluster
	valor_max = medias.max() #Pega o valor do atributo 
	rotulo = ''
	for i in range(0, medias.shape[0]):
		if (medias[i] < valor_max - V): 
			continue
		else:
			mr = Counter(cluster[:,i]).most_common(1) #retorna uma tupla com o numero que mais aparece no atributo avaliado e quantas ocorrencias
			mr = mr[0][0] #Retira apenas a parte que mais interessa
			rotulo += "Atributo " + str(i) + ": " + str(infor[i][mr]) + " ~ " + str(infor[i][mr + 1]) + " | Relevância: " + str(medias[i]) + "%\n"

	return rotulo
