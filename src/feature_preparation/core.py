from multiprocessing import Pipe
from typing import Union
from matplotlib.pyplot import grid
from sklearn.model_selection import GridSearchCV

from sklearn.pipeline import Pipeline


class FeatureLearningMethod():
    param_grid: Union[dict, list]
    
    def mapping(self, data):
        ...
    
    def __str__(self):
        ...
        
        
class FeatureLearningOptimization():
    param_grid: Union[dict, list]
    pipeline: Pipeline
    cv: int = 4
    
    def __init__(self, param_grid: Union[dict, list], pipeline: Pipeline, cv : int = 4) -> None:
        self.param_grid = param_grid
        self.pipeline = pipeline
        self.cv = cv
        
    
    def grid_search(self, data, target):
        grid_search = GridSearchCV(self.pipeline,
                                   self.param_grid,
                                   scoring ='neg_mean_squared_error',
                                   cv = self.cv,
                                   n_jobs=1
                                   )
        grid_search.fit(data,target)
        
        self.param_grid = grid_search.best_params_
        self.pipeline = grid_search.best_estimator_
        return grid_search.best_estimator_
    
    
    def __str__(self):
        ...

