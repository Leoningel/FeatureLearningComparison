import csv
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
    

class M3GPFL_Gengy(BaseEstimator, TransformerMixin):
    def __init__(self, max_depth=15) -> None:
        self.feature_mapping: Solution = None
        self.max_depth = max_depth

    def evolve(self, g, fitness_function, seed:int=0, verbose=0):
        alg = GP_alg(
            g,
            evaluation_function=fitness_function,
            representation=treebased_representation,
            seed=seed,
            population_size=50,
            number_of_generations=50,
            max_depth=self.max_depth,
            minimize=True,
            favor_less_deep_trees=True
            )
        (b, bf, bp) = alg.evolve(verbose=verbose)
        return b, bf, bp

    def fit(self,X,y=None):
        feature_names, feature_indices = utils.feature_info(X)
        Var.__annotations__["feature_name"] = Annotated[str, VarRange(feature_names)]
        Var.feature_indices = feature_indices
        
        grammar = extract_grammar([Var, Plus, SafeDiv, Mult, Minus, BuildingBlock, FeatureSet, EngineeredFeature, Solution], Solution)
        
        def fitness_function(fs: Solution):
            Xt = utils.mapping(feature_names, feature_indices, X, fs)
            dt = DecisionTreeRegressor(max_depth=15)
            scores = -1 * cv_score(dt,Xt,y,2)
            return np.mean(scores)
        
        _, _, fs = self.evolve(grammar, fitness_function=fitness_function, seed=1)

        self.feature_mapping = fs
        with open(f"./results/mappings/2_m3gp_gengy.csv", "a", newline="") as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow([  (str(fs).count(',') + 1), str(fs) ])
        return self
    
    def transform(self,X,y=None):
        feature_names, feature_indices = utils.feature_info(X)
        Xt = utils.mapping(feature_names, feature_indices, X, self.feature_mapping)
        assert len(Xt) == len(X.values)
        return Xt

class TraditionalGP(FeatureLearningMethod):
    param_grid: Union[dict, list] = { "feature_learning__max_depth": [ 10, 15 ]}
    method = M3GPFL_Gengy
    
    def __str__(self) -> str:
        return "M3GP_FL_Gengy"