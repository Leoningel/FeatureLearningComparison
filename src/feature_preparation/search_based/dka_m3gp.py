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
from src.feature_preparation.search_based.grammar.aggregations import Average
from src.feature_preparation.search_based.grammar.basic_grammar import (
    Literal,
    Solution, 
    FeatureSet, 
    EngineeredFeature, 
    BuildingBlock,
    Var,
    Plus,
    Minus,
    Mult,
    SafeDiv,
    IfThenElse
)
from src.feature_preparation.search_based.grammar.categories import (
    Category,
    BoolCategory,
    Col,
    IBCategory,
    IntCategory,
    MonthIB,
    Season,
    SeasonIB,
    WeekdayIB,
    Year,
    Month,
    Holiday,
    Weekday,
    WorkingDay,
    YearIB
)
# from src.feature_preparation.search_based.grammar.logical_ops import IfThenElse
from src.feature_preparation.search_based.grammar.conditions import (
    Equals,
    InBetween,
    NotEquals
    )


class DKA_M3GP_FL(BaseEstimator, TransformerMixin):
    def __init__(self, max_depth=15, elitism_size=5, n_generations=500) -> None:
        self.feature_mapping: Solution = None
        self.max_depth = max_depth
        self.elitism_size = elitism_size
        self.n_generations = n_generations

    special_features = {
        "season"    : Season,
        "yr"        : Year,
        "mnth"      : Month,
        "holiday"   : Holiday,
        "weekday"   : Weekday,
        "workingday": WorkingDay,
    }
    ibs = [ SeasonIB, YearIB, MonthIB, WeekdayIB ]

    def evolve(self, g, fitness_function, seed:int=0, verbose=0):
        alg = GP_alg(
            g,
            evaluation_function=fitness_function,
            representation=treebased_representation,
            seed=seed,
            population_size=500,
            number_of_generations=self.n_generations,
            n_elites=self.elitism_size,
            max_depth=self.max_depth,
            minimize=True,
            favor_less_deep_trees=True
            )
        (b, bf, bp) = alg.evolve(verbose=verbose)
        return b, bf, bp

    def fit(self,X,y=None):
        feature_names, feature_indices = utils.feature_info(X, exclude=list(self.special_features.keys()))
        Var.__init__.__annotations__["feature_name"] = Annotated[str, VarRange(feature_names)]
        Var.feature_indices = feature_indices
        
        grammar = extract_grammar([Var, Literal, Plus, SafeDiv, Mult, Minus, BuildingBlock, Solution, FeatureSet, EngineeredFeature,
                                   IfThenElse, 
                                   Equals, NotEquals, InBetween,
                                   Category, IntCategory, BoolCategory, IBCategory, Col,
                                   Average,
                                   ] + list(self.special_features.values()) + self.ibs, FeatureSet)

        print(grammar)
        
        fitness_function = utils.cv_fitness_function(X,y,2,feature_names,feature_indices)
        
        _, _, fs = self.evolve(grammar, fitness_function=fitness_function, seed=1)

        self.feature_mapping = fs
        return self
    
    def transform(self,X,y=None):
        feature_names, feature_indices = utils.feature_info(X)
        Xt = utils.mapping(feature_names, feature_indices, X, self.feature_mapping)
        assert len(Xt) == len(X.values)
        return Xt

class DKA_M3GP(FeatureLearningMethod):
    param_grid: Union[dict, list] = { 
                            "feature_learning__max_depth": [ 15, 20 ],
                            "feature_learning__elitism_size": [ 1, 5, 25, 100 ]
                            }
    method = DKA_M3GP_FL
    data_file = "data/boom_bikes_14-01-2022_without_casual_and_registered.csv"
    
    def __str__(self) -> str:
        return "dka-m3gp"