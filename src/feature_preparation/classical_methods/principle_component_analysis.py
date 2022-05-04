from typing import Union

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.decomposition import PCA

from feature_preparation.core import FeatureLearningMethod

class Principle_CA_method(BaseEstimator, TransformerMixin):
    def __init__(self, n_components = 1, seed = 0) -> None:
        self.seed = seed
        self.n_components = n_components
    
    def fit(self, X, y=None):
        self.model = PCA(n_components=self.n_components,random_state=self.seed)
        self.model = self.model.fit(X,y)
        return self

    def transform(self, X, y=None):
        Xt = self.model.transform(X)
        return Xt

class Principle_CA(FeatureLearningMethod):
    param_grid: Union[dict, list] = { 'feature_learning__n_components': [1,2,3,4,5] }
    method = Principle_CA_method
        
    def __str__(self) -> str:
        return "PCA"