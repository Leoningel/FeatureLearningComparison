from typing import List
import numpy as np

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor

from src.feature_preparation.search_based.grammar.basic_grammar import Solution



def flatten_list(list_to_flatten):
    l = list()
    for el in list_to_flatten:
        if isinstance(el, (List)):
            for e in flatten_list(el):
                l.append(e)
        else:
            l.append(el)
    return l


def mapping(feature_names, feature_indices, X, fs: Solution, single_solution = False):
    variables = {}
    for x in feature_names:
        i = feature_indices[x]
        variables[x] = X.values[:, i]
    Xt = fs.evaluate(**variables)
    if single_solution:
        Xt = np.array([flatten_list(Xt)]).transpose()
    else:
        Xt = np.array(flatten_list(Xt)).transpose()
        
    return Xt

def feature_info(X, exclude = []):
    feature_names = list(X.columns)
    feature_indices = {}
    for i, n in enumerate(feature_names):
        if n not in exclude:
            feature_indices[n] = i
    feature_names = [ fn for fn in feature_names if fn not in exclude ]
    return feature_names, feature_indices




def cv_fitness_function(X, y, cv_percent, single_solution=False):
    scoring: str = 'neg_mean_squared_error'
    
    def fitness_function(fs: Solution):
            feature_names, feature_indices = feature_info(X)
            Xt = mapping(feature_names, feature_indices, X, fs, single_solution=single_solution)
            dt = DecisionTreeRegressor(max_depth=4)
            scores = -1 * cross_val_score(dt, Xt, y , cv=cv_percent, scoring=scoring)
            return np.mean(scores)
    
    return fitness_function