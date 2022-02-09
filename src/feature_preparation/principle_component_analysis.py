from feature_preparation.core import FeatureLearning
from sklearn.decomposition import PCA

class Principle_CA(FeatureLearning):
    n_components: int = 2
    
    def mapping(self, data):
        pca = PCA(n_components=self.n_components)
        pca.fit(data)
        new_data = pca.transform(data)
        return new_data
    
    def __str__(self) -> str:
        return "PCA"