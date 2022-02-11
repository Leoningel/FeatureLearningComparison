from typing import Union
from feature_preparation.core import FeatureLearningMethod
from sklearn.decomposition import PCA

class Principle_CA(FeatureLearningMethod):
    param_grid: Union[dict, list] = { 'feature_learning__n_components': [1,2,3,4,5] }
    method = PCA
    
    def mapping(self, data, n_components=2):
        pca = PCA(n_components=n_components)
        pca.fit(data)
        new_data = pca.transform(data)
        return new_data
    
    def __str__(self) -> str:
        return "PCA"