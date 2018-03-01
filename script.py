import classificador as clf
from discretizador import discretizador as disc
from sklearn.neural_network import MLPClassifier
from sklearn import tree
import sklearn.datasets as ds
from readData import readData
base = readData("C:\\Users\\Kaio Delmondes\\Desktop\\iris.csv")
bdd, infor, grupos = base.agrupador()

gp0 = grupos[0].get_values()
gp1 = grupos[1].get_values()
gp2 = grupos[2].get_values()

arvore = tree.DecisionTreeClassifier(criterion="entropy")
net = MLPClassifier(hidden_layer_sizes = (10))


clf_tree = clf.classificador(arvore,gp0, 60)
clf_net = clf.classificador(net,gp0, 60)
print("Resultados para o cluster 0		Quantidade de Elementos: " + str(len(gp0)) + "\n")
print("Resultados com Árvore de Decisão\n" + clf.rotular(gp0, infor, clf_tree.resultados, 10))
print("Resultado com MLP\n" + clf.rotular(gp0, infor, clf_net.resultados, 10))

print('-----------------------------------------------------------------------')


clf_tree = clf.classificador(arvore,gp1, 60)
clf_net = clf.classificador(net,gp1, 60)
print("Resultados para o cluster 1		Quantidade de Elementos: " + str(len(gp1)) + "\n")
print("Resultados com Árvore de Decisão\n" + clf.rotular(gp1, infor, clf_tree.resultados, 10))
print("Resultado com MLP\n" + clf.rotular(gp1, infor, clf_net.resultados, 10))

print('-----------------------------------------------------------------------')


clf_tree = clf.classificador(arvore,gp2, 60)
clf_net = clf.classificador(net,gp2, 60)
print("Resultados para o cluster 2		Quantidade de Elementos: " + str(len(gp2)) + "\n")
print("Resultados com Árvore de Decisão\n" + clf.rotular(gp2, infor, clf_tree.resultados, 10))
print("Resultado com MLP\n" + clf.rotular(gp2, infor, clf_net.resultados, 10))

print('-----------------------------------------------------------------------')

