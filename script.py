import classificador as clf
from discretizador import discretizador as disc
from sklearn.neural_network import MLPClassifier
from sklearn import tree
import sklearn.datasets as ds
ids = ds.load_iris()
idsd, infor = disc(ids.data, [3,3,3,3], "EWD")
arvore = tree.DecisionTreeClassifier(criterion="entropy")
net = MLPClassifier(hidden_layer_sizes = (10))


clf_tree = clf.classificador(arvore,idsd[:50,:], 60)
clf_net = clf.classificador(net,idsd[:50,:], 60)
print("Resultados para o cluster com plantas do tipo iris setosa\n")
print("Resultados com Árvore de Decisão\n" + clf.rotular(idsd[:50,:], infor, clf_tree.resultados, 10))
print("Resultado com MLP\n" + clf.rotular(idsd[:50,:], infor, clf_net.resultados, 10))

print('-----------------------------------------------------------------------')


clf_tree = clf.classificador(arvore,idsd[50:100,:], 60)
clf_net = clf.classificador(net,idsd[50:100,:], 60)
print("Resultados para o cluster com plantas do tipo iris versicolor\n")
print("Resultados com Árvore de Decisão\n" + clf.rotular(idsd[50:100,:], infor, clf_tree.resultados, 10))
print("Resultado com MLP\n" + clf.rotular(idsd[50:100,:], infor, clf_net.resultados, 10))

print('-----------------------------------------------------------------------')


clf_tree = clf.classificador(arvore,idsd[100:,:], 60)
clf_net = clf.classificador(net,idsd[100:,:], 60)
print("Resultados para o cluster com plantas do tipo iris virginica\n")
print("Resultados com Árvore de Decisão\n" + clf.rotular(idsd[100:,:], infor, clf_tree.resultados, 10))
print("Resultado com MLP\n" + clf.rotular(idsd[100:,:], infor, clf_net.resultados, 10))

print('-----------------------------------------------------------------------')
