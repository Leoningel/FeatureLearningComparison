from abc import ABC
from dataclasses import dataclass
from typing import Annotated, List, Union
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from evaluation.evaluation_metrics import cv_score
from feature_preparation.core import FeatureLearningMethod
from sklearn.base import BaseEstimator, TransformerMixin

from GeneticEngine.geneticengine.algorithms.random_search import RandomSearch as RS_alg
from GeneticEngine.geneticengine.core.grammar import extract_grammar
from GeneticEngine.geneticengine.core.representations.tree.treebased import treebased_representation
from GeneticEngine.geneticengine.metahandlers.lists import ListSizeBetween
from GeneticEngine.geneticengine.metahandlers.vars import VarRange
from GeneticEngine.geneticengine.metrics import f1_score

class Solution(ABC):
    def evaluate(self, **kwargs) -> float:
        return lambda _: 0

@dataclass
class FeatureSubset(Solution):
    subset: Annotated[List[Solution], ListSizeBetween(1, 2)]
    
    def evaluate(self, **kwargs):
        return lambda x: [ el.evaluate()(x) for el in self.subset ]
    
@dataclass
class Feature(Solution):
    feature_name: Annotated[str, VarRange(["x" , "y"])]

    def evaluate(self, **kwargs):
        return lambda x: x.append(self.feature_name)
    

def evolve(g, fitness_function, seed:int=0):
    alg = RS_alg(
        g,
        evaluation_function=fitness_function,
        representation=treebased_representation,
        seed=seed,
        population_size=10,
        number_of_generations=50,
        minimize=True,
        favor_less_deep_trees=True
        )
    (b, bf, bp) = alg.evolve()
    return b, bf, bp

class RandomSearch(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        self.selected_features = list()
    
    
    def fit(self,X,y=None):
        def fitness_function(fs: Solution):
            selected_features = list()
            fs.evaluate()(selected_features)
            
            Xt = X[selected_features]
            dt = DecisionTreeRegressor()
            scores = -1 * cv_score(dt,Xt,y,2)
            return np.mean(scores)
        
        feature_names = list(X.columns)
        feature_indices = {}
        for i, n in enumerate(feature_names):
            feature_indices[n] = i
        Feature.__annotations__["feature_name"] = Annotated[str, VarRange(feature_names)]
        Feature.feature_indices = feature_indices  # type: ignore
        
        grammar = extract_grammar([Feature, FeatureSubset], Solution)
        # print(grammar)
        best_ind, fitness, fs = evolve(grammar, fitness_function=fitness_function, seed=1)

        selected_features = list()
        fs.evaluate()(selected_features)
        self.selected_features = selected_features
        print(selected_features)
        return self
    
    def transform(self,X,y=None):
        Xt = X[self.selected_features]
        return Xt

class RandomSearchFS(FeatureLearningMethod):
    param_grid: Union[dict, list] = {}
    method = RandomSearch
    
    def mapping(self, data):
        return data
    
    def __str__(self) -> str:
        return "RandomSearch_FS"