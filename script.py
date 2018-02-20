import tree_net
from discretizador import discretizador as disc
from sklearn.neural_network import MLPClassifier
from sklearn import tree
import sklearn.datasets as ds
ids = ds.load_iris()
idsd, infor = disc(ids.data, [3,3,3,3], "EWD")
arvore = tree.DecisionTreeClassifier(criterion="entropy")
net = MLPClassifier(hidden_layer_sizes = (10))
