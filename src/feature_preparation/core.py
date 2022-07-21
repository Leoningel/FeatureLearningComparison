from typing import Any, Callable, Union

from matplotlib.pyplot import grid

from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline

import global_vars as gv

class FeatureLearningMethod():
    param_grid: Union[dict, list]
    data_file: str = gv.DATA_FILE
    # method: Union[BaseEstimator, Callable[[Any], str]]
        
    def __str__(self):
        ...
        
        
class FeatureLearningOptimization():
    param_grid: Union[dict, list]
    pipeline: Pipeline
    splits = gv.SPLITS
    
    def __init__(self, param_grid: Union[dict, list], pipeline: Pipeline, splits = gv.SPLITS) -> None:
        self.param_grid = param_grid
        self.pipeline = pipeline
        self.splits = splits
        
    
    def grid_search(self, data, target):
        split_data = list()
        data_ids = list(range(len(target)))
        for split in self.splits:
            cut = int(split * len(target))
            split_data.append((data_ids[:cut],data_ids[cut:]))
        
        if gv.SCORING == 'f_score':
            scoring = 'f1'
        else:
            scoring = 'neg_mean_squared_error'
            
        grid_search = GridSearchCV(self.pipeline,
                                   self.param_grid,
                                   scoring = scoring,
                                   cv = split_data,
                                   n_jobs=1
                                   )
        grid_search.fit(data,target)
        
        self.param_grid = grid_search.best_params_
        self.pipeline = grid_search.best_estimator_
        return grid_search.best_estimator_, grid_search.best_params_
    
    
    def __str__(self):
        ...

