from typing import Union
from feature_preparation.core import FeatureLearningMethod
from sklearn.decomposition import PCA

class Principle_CA(FeatureLearningMethod):
    param_grid: Union[dict, list] = { 'feature_learning__n_components': [1,2,3,4,5] }
    method = PCA
        
    def __str__(self) -> str:
        return "PCA"