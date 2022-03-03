import warnings
warnings.filterwarnings("ignore", category=FutureWarning,
                        message="From version 0.21, test_size will always complement",
                        module="sklearn")
from typing import Union

from m3gp.M3GP import M3GP as M3GP_alg
from feature_preparation.core import FeatureLearningMethod
from sklearn.base import BaseEstimator, TransformerMixin



class M3GPFL(BaseEstimator, TransformerMixin):
    def __init__(self, max_depth=15) -> None:
        self.feature_mapping = None
        self.max_depth = max_depth

    def fit(self,X,y=None,seed=42):
        m3gp = M3GP_alg(
                    max_generation=50, 
                    population_size=50, 
                    limit_depth=self.max_depth,
                    elitism_size=5,
                    max_initial_depth=self.max_depth,
                    model_name="DecisionTreeRegressor", 
                    fitnessType="mse",
                    random_state=seed,
                    verbose=False)
        m3gp.fit(X,y)

        self.feature_mapping = m3gp.getBestIndividual()
        
        return self
    
    def transform(self,X,y=None):
        Xt = self.feature_mapping.convert(X)
        assert len(Xt) == len(X.values)
        return Xt

class M3GP(FeatureLearningMethod):
    param_grid: Union[dict, list] = { "feature_learning__max_depth": [ 10, 15 ]}
    method = M3GPFL
    
    def __str__(self) -> str:
        return "M3GP_FL"


