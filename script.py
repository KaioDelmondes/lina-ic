import classificador as clf
from sklearn.neural_network import MLPClassifier
from sklearn import tree
import sklearn.datasets as ds
from readData import readData

base = readData("C:\\Users\\LuciaEmilia\\Desktop\\Testes k-means\\g10.txt")
bdd, infor, grupos = base.dataPreparation()

gp = []
for x in range(0, len(grupos)):
	gp.append(grupos[x].get_values())

arvore = tree.DecisionTreeClassifier(criterion="entropy")
net = MLPClassifier(hidden_layer_sizes = (10))

for x in range (0, len(gp)):
	clf_tree = clf.classificador(arvore,gp[x], 60)
	clf_net = clf.classificador(net,gp[x], 60)
	print("Resultados para o cluster "+ str(x) +"             Quantidade de Elementos: " + str(len(gp[x])) + "\n")
	print("Resultados com Árvore de Decisão\n" + clf.rotular(gp[x], infor, clf_tree.resultados, 10))
	print("Resultado com MLP\n" + clf.rotular(gp[x], infor, clf_net.resultados, 10))
	print('-----------------------------------------------------------------------')
