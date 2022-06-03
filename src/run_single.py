import csv
import time
from typing import List
from optparse import OptionParser
import warnings
warnings.filterwarnings('ignore')

from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning

import numpy as np

import src.global_vars as gv
from src.data_extraction.data_extraction import load
from src.feature_preparation.core import FeatureLearningMethod, FeatureLearningOptimization
from src.feature_preparation.classical_methods.feature_tools_FS import FeatureToolsFS
from src.feature_preparation.classical_methods.no_feature_construction import NoFeatureLearning
from src.feature_preparation.classical_methods.principle_component_analysis import PrincipleCA
from src.feature_preparation.search_based.random_search import RandomSearchFS
from src.feature_preparation.search_based.traditional_gp import TraditionalGP
from src.feature_preparation.search_based.m3gp_jb import M3GP_JB
from src.feature_preparation.search_based.m3gp_gengy import M3GP_Gengy
from src.feature_preparation.search_based.dk_m3gp import DK_M3GP
from src.feature_preparation.search_based.dka_m3gp import DKA_M3GP
from src.model_generation.models import DecisionTree, RandomForest, MLP, SVM, Model
import src.utils as utils

N_SEEDS = 30   
TRAIN_PROPORTION = 0.75
 

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-s", "--seed", dest="seed", type="int")
    parser.add_option("-m", "--model", dest="model", type="int")
    parser.add_option("-f", "--flm", dest="flm", type="int")

    (options, args) = parser.parse_args()
    models : List[Model] = [ DecisionTree(), RandomForest(), MLP(), SVM() ]
    # feature_learnings : List[FeatureLearningMethod] = [ PrincipleCA(), FeatureToolsFS(), NoFeatureLearning(), M3GP_JB(), TraditionalGP(), DKA_M3GP(), DK_M3GP(), M3GP_Gengy(), RandomSearchFS() ]

    seed = options.seed
    model = models[options.model]
    # feature_learning = feature_learnings[options.flm]
    feature_learning = PrincipleCA()
    
    X, y, X_train, y_train = load(gv.DATA_FILE, 'cnt', drop=[], train_proportion=TRAIN_PROPORTION)
    
    start = time.time()

    pipeline = utils.make_pipeline(feature_learning, model, seed)
    estimator = FeatureLearningOptimization(param_grid=feature_learning.param_grid, pipeline=pipeline)
    
    with ignore_warnings(category=ConvergenceWarning):
        utils.make_grid_search_ready(estimator.pipeline)
        best_estimator, best_params = estimator.grid_search(X_train, y_train)
        grid_search_time = time.time() - start
        utils.make_evaluation_ready(estimator.pipeline)
        scores = utils.cv_time_series(feature_learning, model, seed, best_params, X_train, y_train)
        test_score = utils.cv_time_series(feature_learning, model, seed, best_params, X, y, splits = [TRAIN_PROPORTION], additional_text='test_data_')
    
    avg_score = np.mean(scores)
    best_score = min(scores)
    duration = time.time() - start
    
    csv_row = [ str(feature_learning), str(estimator.param_grid), str(model), seed, avg_score, best_score, test_score, grid_search_time, duration ]
    with open(f"{gv.TEMP_RESULTS_FOLDER}{feature_learning}/main.csv", "a", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(csv_row)
    
    
    



