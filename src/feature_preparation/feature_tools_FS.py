from typing import Union
from feature_preparation.core import FeatureLearningMethod
import featuretools as ft
from featuretools.selection import remove_highly_correlated_features
from sklearn.base import BaseEstimator, TransformerMixin

class RemoveHighlyCorrelatedFeatures(BaseEstimator, TransformerMixin):
    def __init__(self,pct_corr_threshold=0.95) -> None:
        self.pct_corr_threshold = pct_corr_threshold
        self.new_features = []
    
    def fit(self,X,y=None):
        es = ft.EntitySet(id="0")
        es = es.add_dataframe(
            dataframe_name="boom_bikes",
            dataframe=X,
            index="instant"
        )
        fm, features = ft.dfs(entityset=es, target_dataframe_name="boom_bikes", max_depth=1)
        _, new_features = remove_highly_correlated_features(fm,features=features,pct_corr_threshold=self.pct_corr_threshold)
        new_features = [f._name for f in new_features]
        self.new_features = new_features
        return self
    
    def transform(self,X,y=None):
        Xt = X[self.new_features]
        return Xt

class FeatureToolsFS(FeatureLearningMethod):
    param_grid: Union[dict, list] = { "feature_learning__pct_corr_threshold": [ .6, .7, .8, .9, .95 ]}
    method = RemoveHighlyCorrelatedFeatures
    
    def mapping(self, data):
        # features = data.columns
        # es = ft.EntitySet(id="0")
        # es = es.add_dataframe(
        #     dataframe_name="boom_bikes",
        #     dataframe=data,
        #     index="instant"
        # )
        # fm, features = ft.dfs(entityset=es, target_dataframe_name="boom_bikes", max_depth=1)
        # new_fm, _ = remove_highly_correlated_features(fm,features=features)
        return data
    
    def __str__(self) -> str:
        return "FeatureTools_FS"