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
    def __init__(self, seed = 0, max_depth=gv.MAX_DEPTH - 2, elitism_size=5, novelties_size=0, n_generations=gv.NUMBER_OF_GENERATIONS, save_to_csv='', test_data = None, on_budget = False) -> None:
        self.feature_mapping = None
        self.seed = seed
        self.max_depth = max_depth
        self.elitism_size = elitism_size
        self.novelties_size = novelties_size
        self.n_generations = n_generations
        self.save_to_csv = save_to_csv
        self.test_data = test_data
        self.on_budget = on_budget

    def fit(self,X,y=None):
        if self.save_to_csv != '':
            save_to_csv = f"{gv.TEMP_RESULTS_FOLDER}/{name}/seed={self.seed}_{self.save_to_csv}.csv"
        else:
            save_to_csv = ''
        if gv.SCORING == 'f_score':
            model_name = "DecisionTreeClassifier"
            fitness_type = "WAF"
        else:
            model_name="DecisionTreeRegressor"
            fitness_type="MSE"
        m3gp = M3GP_alg(
                    population_size=gv.POPULATION_SIZE,
                    max_generation=self.n_generations,
                    limit_depth=self.max_depth,
                    elitism_size=self.elitism_size,
                    max_initial_depth=self.max_depth,
                    # dim_min=11,
                    # dim_max=12,
                    model_name=model_name, 
                    fitnessType=fitness_type,
                    csv_file=save_to_csv,
                    random_state=self.seed,
                    verbose=False)
        if self.test_data:
            X_test, y_test = self.test_data
            m3gp.fit(X,y,Te_X=X_test, Te_Y = y_test)
        else:
            m3gp.fit(X,y)

        self.feature_mapping = m3gp.getBestIndividual()
        
        return self
    
    def transform(self,X,y=None):
        Xt = self.feature_mapping.convert(X)
        assert len(Xt) == len(X.values)
        return Xt

class M3GP_JB(FeatureLearningMethod):
    param_grid: Union[dict, list] = { 
                            "feature_learning__elitism_size": gv.ELITISMS,
                            }
    method = M3GP_JB_Method
    
    def __str__(self) -> str:
        return "m3gp_jb"


