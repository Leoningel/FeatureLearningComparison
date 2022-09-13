from typing import Annotated, List, Union

from feature_preparation.core import FeatureLearningMethod
from sklearn.base import BaseEstimator, TransformerMixin

from geneticengine.algorithms.random_search import RandomSearch as RS_alg
from geneticengine.core.grammar import extract_grammar
from geneticengine.core.representations.tree.treebased import treebased_representation
from geneticengine.metahandlers.vars import VarRange

import feature_preparation.search_based.utils as utils
from feature_preparation.search_based.grammar.basic_grammar import (
    Solution, 
    FeatureSet, 
    BuildingBlock,
    Var,
)
import global_vars as gv

name = __name__.split(".")[-1]

class RandomSearchFS_Method(BaseEstimator, TransformerMixin):
    def __init__(self, seed = 0, max_depth=gv.MAX_DEPTH, n_generations=gv.NUMBER_OF_GENERATIONS, save_to_csv='') -> None:
        self.feature_mapping: Solution = None
        self.seed = seed
        self.max_depth = max_depth
        self.n_generations = n_generations
        self.save_to_csv = save_to_csv

    def evolve(self, g, fitness_function, test_fitness_function = None, verbose=0, minimize=True):
        if self.save_to_csv != '':
            save_to_csv = f"{gv.TEMP_RESULTS_FOLDER}/{name}/seed={self.seed}_{self.save_to_csv}.csv"
        else:
            save_to_csv=None
        alg = RS_alg(
            g,
            evaluation_function=fitness_function,
            representation=treebased_representation,
            seed=self.seed,
            population_size=gv.POPULATION_SIZE,
            number_of_generations=self.n_generations,
            max_depth=self.max_depth,
            minimize=minimize,
            favor_less_deep_trees=True,
            save_to_csv=save_to_csv,
            save_genotype_as_string=False,
            )
        (b, bf, bp) = alg.evolve(verbose=verbose)
        return b, bf, bp

    def fit(self,X,y=None):
        feature_names, feature_indices = utils.feature_info(X, exclude = [gv.TIME_COLUMN])
        Var.__init__.__annotations__["feature_name"] = Annotated[str, VarRange(feature_names)]
        Var.feature_indices = feature_indices
        
        grammar = extract_grammar([Var,  FeatureSet, BuildingBlock], Solution)
        
        fitness_function, minimize = utils.ff_time_series(X,y)
        
        _, _, fs = self.evolve(grammar, fitness_function=fitness_function, minimize=minimize)

        self.feature_mapping = fs
        return self
    
    def transform(self,X,y=None):
        feature_names, feature_indices = utils.feature_info(X)
        Xt = utils.mapping(feature_names, feature_indices, X, self.feature_mapping)
        assert len(Xt) == len(X.values)
        return Xt

class RandomSearchFS(FeatureLearningMethod):
    param_grid: Union[dict, list] = {}
    method = RandomSearchFS_Method
    
    def mapping(self, data):
        return data
    
    def __str__(self) -> str:
        return name