import warnings
warnings.filterwarnings("ignore", category=FutureWarning,
                        message="From version 0.21, test_size will always complement",
                        module="sklearn")
from typing import Union

from m3gp.M3GP import M3GP as M3GP_alg
from feature_preparation.core import FeatureLearningMethod
from sklearn.base import BaseEstimator, TransformerMixin

import global_vars as gv


name = __name__.split(".")[-1]

class M3GP_JB_Method(BaseEstimator, TransformerMixin):
    def __init__(self, seed = 0, max_depth=15, elitism_size=5, n_generations=500, save_to_csv='') -> None:
        self.feature_mapping = None
        self.seed = seed
        self.max_depth = max_depth
        self.elitism_size = elitism_size
        self.n_generations = n_generations
        self.save_to_csv = save_to_csv

    def fit(self,X,y=None):
        if self.save_to_csv != '':
            save_to_csv = f"{gv.TEMP_RESULTS_FOLDER}/{name}/seed={self.seed}_{self.save_to_csv}.csv"
        else:
            save_to_csv = ''
        m3gp = M3GP_alg(
                    population_size=500,
                    max_generation=self.n_generations,
                    limit_depth=self.max_depth,
                    elitism_size=self.elitism_size,
                    max_initial_depth=self.max_depth,
                    # dim_min=11,
                    # dim_max=12,
                    model_name="DecisionTreeRegressor", 
                    fitnessType="MSE",
                    csv_file=save_to_csv,
                    random_state=self.seed,
                    verbose=False)
        m3gp.fit(X,y)

        self.feature_mapping = m3gp.getBestIndividual()
        
        return self
    
    def transform(self,X,y=None):
        Xt = self.feature_mapping.convert(X)
        assert len(Xt) == len(X.values)
        return Xt

class M3GP_JB(FeatureLearningMethod):
    param_grid: Union[dict, list] = { 
                            "feature_learning__max_depth": gv.MAX_DEPTHS,
                            "feature_learning__elitism_size": gv.ELITISMS
                            }
    method = M3GP_JB_Method
    
    def __str__(self) -> str:
        return "m3gp_jb"


