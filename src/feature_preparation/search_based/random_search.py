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
from GeneticEngine.geneticengine.metahandlers.vars import VarRange

from src.feature_preparation.search_based.grammar import (
    Solution, 
    FeatureSet, 
    EngineeredFeature, 
    BuildingBlock,
    Var
)

def evolve(g, fitness_function, seed:int=0, verbose=0):
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
    (b, bf, bp) = alg.evolve(verbose=verbose)
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
        Var.__annotations__["feature_name"] = Annotated[str, VarRange(feature_names)]
        Var.feature_indices = feature_indices  # type: ignore
        
        grammar = extract_grammar([Var, EngineeredFeature, FeatureSet, BuildingBlock], Solution)
        best_ind, fitness, fs = evolve(grammar, fitness_function=fitness_function, seed=1)

        selected_features = list()
        fs.evaluate()(selected_features)
        self.selected_features = selected_features
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