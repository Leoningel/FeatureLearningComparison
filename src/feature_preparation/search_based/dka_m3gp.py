from typing import Annotated, List, Union
import numpy as np

from feature_preparation.core import FeatureLearningMethod
from sklearn.base import BaseEstimator, TransformerMixin

from geneticengine.algorithms.gp.gp import GP as GP_alg
from geneticengine.core.grammar import extract_grammar
from geneticengine.core.representations.tree.treebased import treebased_representation
from geneticengine.metahandlers.vars import VarRange

import feature_preparation.search_based.utils as utils
from feature_preparation.search_based.grammar.aggregations import Average
from feature_preparation.search_based.grammar.basic_grammar import (
    Solution, 
    FeatureSet, 
    Var,
    Literal,
    standard_gp_grammar,
    IfThenElse
)
from feature_preparation.search_based.grammar.categories import (
    Category,
    BoolCategory,
    Col,
    IBCategory,
    IntCategory,
)
from feature_preparation.search_based.grammar.domain_knowledge import DomainKnowledge
from feature_preparation.search_based.grammar.conditions import (
    Equals,
    InBetween,
    NotEquals
)
import global_vars as gv

name = __name__.split(".")[-1]

class DKA_M3GP_Method(BaseEstimator, TransformerMixin):
    def __init__(self, seed = 0, max_depth=gv.MAX_DEPTH, elitism_size=5, novelties_size=0, n_generations=gv.NUMBER_OF_GENERATIONS, save_to_csv='', test_data = None, on_budget = False) -> None:
        self.feature_mapping: Solution = None
        self.seed = seed
        self.max_depth = max_depth
        self.elitism_size = elitism_size
        self.novelties_size = novelties_size
        self.n_generations = n_generations
        self.save_to_csv = save_to_csv
        self.test_data = test_data
        self.on_budget = on_budget

    def evolve(self, g, fitness_function, test_fitness_function = None, verbose=1, minimize=True):
        if self.save_to_csv != '':
            save_to_csv = f"{gv.TEMP_RESULTS_FOLDER}/{name}/seed={self.seed}_{self.save_to_csv}.csv"
        else:
            save_to_csv=None
        alg = GP_alg(
            g,
            evaluation_function=fitness_function,
            representation=treebased_representation,
            seed=self.seed,
            population_size=gv.POPULATION_SIZE,
            number_of_generations=self.n_generations,
            n_elites=gv.ELITSM,
            n_novelties=self.novelties_size,
            either_mut_or_cro=0.5,
            specific_type_mutation=FeatureSet,
            specific_type_crossover=FeatureSet,
            max_depth=self.max_depth,
            minimize=minimize,
            favor_less_deep_trees=True,
            save_to_csv=save_to_csv,
            save_genotype_as_string=False,
            test_data=test_fitness_function,
            timer_stop_criteria=self.on_budget,
            timer_limit=gv.TIME_LIMIT,
            )
        (b, bf, bp) = alg.evolve(verbose=verbose)
        return b, bf, bp

    def fit(self,X,y=None):
        dk = DomainKnowledge()
        Average.__init__.__annotations__["aggregation_col"] = Annotated[str, VarRange([gv.TARGET_COLUMN])]
        
        dka_grammar = [ IfThenElse, 
                        Equals, NotEquals, InBetween,
                        Category, IntCategory, BoolCategory, IBCategory, Col,
                        Average
                        ]
        
        feature_names, feature_indices = utils.feature_info(X, exclude=list(dk.special_features.keys()) + [gv.TIME_COLUMN])
               
        if feature_names:
            Var.__init__.__annotations__["feature_name"] = Annotated[str, VarRange(feature_names)]
            Var.feature_indices = feature_indices
            dka_grammar += [ Var ]
        else:
            dka_grammar += [ Literal ]
            
        grammar = extract_grammar(standard_gp_grammar + 
                                  dka_grammar + 
                                  list(dk.special_features.values()) + 
                                  dk.ibs, 
                                  FeatureSet)

        fitness_function, minimize = utils.ff_time_series(X,y,include_all_data=True)
        if self.test_data:
            X_test, y_test = self.test_data
            self.test_data, _ = utils.ff_time_series(X_test, y_test,include_all_data=True)

        _, _, fs = self.evolve(grammar, fitness_function=fitness_function, test_fitness_function=self.test_data, verbose=1, minimize=minimize)

        self.feature_mapping = fs
        return self
    
    def transform(self,X,y=None):
        feature_names, feature_indices = utils.feature_info(X)
        Xt = utils.mapping(feature_names, feature_indices, X, self.feature_mapping, include_all_data = True)
        assert len(Xt) == len(X.values)
        return Xt

class DKA_M3GP(FeatureLearningMethod):
    param_grid: Union[dict, list] = { 
                            # "feature_learning__elitism_size": gv.ELITISMS,
                            # "feature_learning__novelties_size": gv.NOVELTIES,
                            }
    method = DKA_M3GP_Method
    
    def __str__(self) -> str:
        return name