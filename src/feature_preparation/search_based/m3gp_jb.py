import warnings
warnings.filterwarnings("ignore", category=FutureWarning,
                        message="From version 0.21, test_size will always complement",
                        module="sklearn")
from typing import Union

from m3gp.M3GP import M3GP as M3GP_alg
from feature_preparation.core import FeatureLearningMethod
from sklearn.base import BaseEstimator, TransformerMixin



class M3GPFL_JB(BaseEstimator, TransformerMixin):
    def __init__(self, max_depth=15, elitism_size=5) -> None:
        self.feature_mapping = None
        self.max_depth = max_depth
        self.elitism_size = elitism_size

    def fit(self,X,y=None,seed=42):
        m3gp = M3GP_alg(
                    population_size=500,
                    max_generation=500,
                    limit_depth=self.max_depth,
                    elitism_size=self.elitism_size,
                    max_initial_depth=self.max_depth,
                    # dim_min=11,
                    # dim_max=12,
                    model_name="DecisionTreeRegressor", 
                    fitnessType="MSE",
                    random_state=seed,
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
                            "feature_learning__max_depth": [ 5, 10, 15, 20 ],
                            "feature_learning__elitism_size": [ 1, 5, 25, 100 ]
                            }
    method = M3GPFL_JB
    
    def __str__(self) -> str:
        return "M3GP_JB_FL"


