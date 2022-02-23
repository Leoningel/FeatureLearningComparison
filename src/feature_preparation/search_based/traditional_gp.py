from abc import ABC
import csv
from dataclasses import dataclass
from typing import Annotated, List, Union
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from evaluation.evaluation_metrics import cv_score
from feature_preparation.core import FeatureLearningMethod
from sklearn.base import BaseEstimator, TransformerMixin

from geneticengine.algorithms.gp.gp import GP as GP_alg
from geneticengine.core.grammar import extract_grammar
from geneticengine.core.representations.tree.treebased import treebased_representation
from geneticengine.metahandlers.vars import VarRange

import src.feature_preparation.search_based.utils as utils
from src.feature_preparation.search_based.grammar import (
    Solution, 
    FeatureSet, 
    EngineeredFeature, 
    BuildingBlock,
    Var,
    Plus,
    Minus,
    Mult,
    SafeDiv
)
    

def evolve(g, fitness_function, seed:int=0, verbose=0):
    alg = GP_alg(
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

class GPFL(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        self.feature_mapping: Solution = None

    def fit(self,X,y=None):
        feature_names, feature_indices = utils.feature_info(X)
        Var.__annotations__["feature_name"] = Annotated[str, VarRange(feature_names)]
        Var.feature_indices = feature_indices
        
        grammar = extract_grammar([Var, Plus, SafeDiv, Mult, Minus, EngineeredFeature, FeatureSet, BuildingBlock], Solution)
        
        def fitness_function(fs: Solution):
            Xt = utils.mapping(feature_names, feature_indices, X, fs)
            dt = DecisionTreeRegressor()
            scores = -1 * cv_score(dt,Xt,y,2)
            return np.mean(scores)
        
        _, _, fs = evolve(grammar, fitness_function=fitness_function, seed=1)

        self.feature_mapping = fs
        with open(f"./results/traditional_gp_mappings/2.csv", "a", newline="") as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow([  (str(fs).count(',') + 1), str(fs) ])
        return self
    
    def transform(self,X,y=None):
        feature_names, feature_indices = utils.feature_info(X)
        Xt = utils.mapping(feature_names, feature_indices, X, self.feature_mapping)
        return Xt

class TraditionalGP(FeatureLearningMethod):
    param_grid: Union[dict, list] = {}
    method = GPFL
    
    def __str__(self) -> str:
        return "GP_FL"