from discretizacao import discretizacao as disc
import numpy as np
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
