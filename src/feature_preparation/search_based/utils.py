from typing import List
import numpy as np
import pandas as pd

from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score, mean_squared_error
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

from feature_preparation.search_based.grammar.basic_grammar import Solution
import global_vars as gv


def flatten_list(list_to_flatten):
    l = list()
    for el in list_to_flatten:
        if isinstance(el, (List)):
            for e in flatten_list(el):
                l.append(e)
        else:
            l.append(el)
    return l


def mapping(feature_names, feature_indices, X, fs: Solution, include_all_data = False, single_solution = False):
    variables = {}
    for x in feature_names:
        i = feature_indices[x]
        variables[x] = X.values[:, i]
    if include_all_data:
        variables['data'] = pd.read_csv(gv.DATA_FILE, delimiter=gv.DELIMITER)
    Xt = fs.evaluate(**variables)
    if single_solution:
        Xt = np.array([flatten_list(Xt)]).transpose()
    else:
        Xt = np.array(flatten_list(Xt)).transpose()
        
    return Xt

def feature_info(X, exclude = []):
    '''
    Returns feature_names, feature_indices.
    '''
    feature_names = list(X.columns)
    feature_indices = {}
    for i, n in enumerate(feature_names):
        if n not in exclude:
            feature_indices[n] = i
    feature_names = [ fn for fn in feature_names if fn not in exclude ]
    return feature_names, feature_indices

def ff_time_series(X, y, single_solution=False, include_all_data = False):
    if gv.SCORING == 'f_score':
        scoring = lambda pred,gt: f1_score(pred, gt, average='weighted')
        ffmodel = DecisionTreeClassifier
        minimize = False
    else:
        scoring = lambda pred,gt: mean_squared_error(pred, gt)
        ffmodel = DecisionTreeRegressor
        minimize = True
    
    def fitness_function(fs: Solution):
            feature_names, feature_indices = feature_info(X)
            Xt = mapping(feature_names, feature_indices, X, fs, include_all_data, single_solution=single_solution)
            dt = ffmodel(max_depth=4)
            model = dt.fit(Xt,y)
            predictions = model.predict(Xt)
            score = scoring(predictions,y)
            return score
    
    return fitness_function, minimize

