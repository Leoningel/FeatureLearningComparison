from feature_preparation.core import FeatureLearning
import featuretools as ft
from featuretools.selection import remove_highly_correlated_features

class FeatureToolsFS(FeatureLearning):
    
    def mapping(self, data):
        features = data.columns
        es = ft.EntitySet(id="0")
        es = es.add_dataframe(
            dataframe_name="boom_bikes",
            dataframe=data,
            index="instant"
        )
        fm, features = ft.dfs(entityset=es, target_dataframe_name="boom_bikes", max_depth=1)
        new_fm, _ = remove_highly_correlated_features(fm,features=features)
        return new_fm
    
    def __str__(self) -> str:
        return "FeatureTools_FS"