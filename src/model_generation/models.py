from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR


class Model():
    def model(self, seed: int):
        ...
    def __str__(self):
        ...

class DecisionTree(Model):
    def model(self, seed: int):
        return DecisionTreeRegressor(random_state=seed)

    def __str__(self):
        return "Decision Tree"

class RandomForest(Model):
    def model(self, seed: int):
        return RandomForestRegressor(random_state=seed)

    def __str__(self):
        return "Random Forest"

class MLP(Model):
    def model(self, seed: int):
        return MLPRegressor(random_state=seed)

    def __str__(self):
        return "MLP"

class SVM(Model):
    C: float = 1.0
    epsilon: float = 0.2
    
    def model(self, seed: int):
        return SVR(C=self.C, epsilon=self.epsilon)

    def __str__(self):
        return "SVM"
        
