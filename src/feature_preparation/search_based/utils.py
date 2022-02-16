from typing import List
from src.feature_preparation.search_based.grammar import Solution
import numpy as np



def flatten_list(list_to_flatten):
    l = list()
    for el in list_to_flatten:
        if isinstance(el, (List)):
            for e in flatten_list(el):
                l.append(e)
        else:
            l.append(el)
    return l


def mapping(feature_names, feature_indices, X, fs: Solution):
    variables = {}
    for x in feature_names:
        i = feature_indices[x]
        variables[x] = X.values[:, i]
    Xt = fs.evaluate(**variables)
    Xt = np.array(flatten_list(Xt)).transpose()
    return Xt

def feature_info(X):
    feature_names = list(X.columns)
    feature_indices = {}
    for i, n in enumerate(feature_names):
        feature_indices[n] = i
    return feature_names, feature_indices

