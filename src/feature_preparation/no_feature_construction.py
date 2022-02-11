from typing import Union
from feature_preparation.core import FeatureLearningMethod

class NoFeatureLearning(FeatureLearningMethod):
    param_grid: Union[dict, list] = dict()
    method = lambda _: "passthrough"
    
    def mapping(self, data):
        return data
    
    def __str__(self) -> str:
        return "No_Feature_Learning"