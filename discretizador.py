from discretizacao import discretizacao as disc
import numpy as np
"""
	Módulo que auxilia na discretização da BD. Com esse módulo é possivel discretizar toda a BD, ao invés de apenas um atributo por vez.
	Parâmetros:
		BD: A base de dados a ser discretizada.
		categorias: um vetor de numeros inteiros com as faixas de discretização para cada atributo respectivamente. Esse vetor deve ter a mesma quantidade de elementos que atributos existentes na BD.
		metodo: uma string, 'EFD' ou 'EWD', descrevendo o método de discretização.
"""
def discretizador(bd, categorias, metodo):
	bdd = []
	infor = []
	
	for j in range(0, len(bd[1])):
		attb_adis = disc(bd[:,j], categorias[j])
		if metodo is "EFD":
			attb_dis = (attb_adis.EFD())
		elif metodo is "EWD":
			attb_dis = (attb_adis.EWD())
		bdd.append(attb_dis[0].get_values())
		infor.append(attb_dis[1])
		print(j)
	
	nbdd = np.asarray(bdd, dtype = 'int32')
	return nbdd.T,infor
