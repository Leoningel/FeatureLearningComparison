from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR


class Model():
    model: object

    def evaluate(self, seed: int):
        ...
    def __str__(self):
        ...

class DecisionTree(Model):
    model = DecisionTreeRegressor
    
    def evaluate(self, seed: int):
        return self.model(random_state=seed, max_depth=4)

    def __str__(self):
        return "DT"

class RandomForest(Model):
    model = RandomForestRegressor
    
    def evaluate(self, seed: int):
        return self.model(random_state=seed, max_depth=4)

    def __str__(self):
        return "RF"

class MLP(Model):
    model = MLPRegressor

    def evaluate(self, seed: int):
        return self.model(random_state=seed)

    def __str__(self):
        return "MLP"

class SVM(Model):
    model = SVR
    C: float = 1.0
    epsilon: float = 0.2
    
    def evaluate(self, seed: int):
        return self.model(C=self.C, epsilon=self.epsilon)

    def __str__(self):
        return "SVM"
        
