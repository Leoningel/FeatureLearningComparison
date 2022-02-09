from feature_preparation.core import FeatureLearning

class NoFeatureLearning(FeatureLearning):
    
    def mapping(self, data):
        return data
    
    def __str__(self) -> str:
        return "No_Feature_Learning"