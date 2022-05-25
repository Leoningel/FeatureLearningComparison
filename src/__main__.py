import csv
import time
from typing import List
import sys
import warnings
warnings.filterwarnings('ignore')

from sklearn.pipeline import Pipeline
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning

import numpy as np
import pandas as pd

import src.global_vars as gv
from src.data_extraction.data_extraction import load
from src.evaluation.evaluation_metrics import cv_time_series
from src.evaluation.visualization import plot_combined_barplot_comparison, plot_separated_violin_comparisons
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
 
models : List[Model] = [ DecisionTree(), RandomForest(), MLP(), SVM() ]
feature_learnings : List[FeatureLearningMethod] = [ DKA_M3GP() ]
# feature_learnings : List[FeatureLearningMethod] = [ DKA_M3GP(), DK_M3GP(), M3GP_Gengy(), M3GP_JB(), TraditionalGP(), RandomSearchFS(), PrincipleCA(), FeatureToolsFS(), NoFeatureLearning() ]

addition = ""

if __name__ == '__main__':
    args = sys.argv
    RUN_MODELS = "--run_models" in args
    PLOT_DATA = "--plot_data" in args
    seeds = [ int(arg.split("=")[1]) for arg in args if "--seed=" in arg ]
    if not seeds:
        seeds = range(N_SEEDS)
        
    if not RUN_MODELS:
        print("Warning: Not running models. Using data stored.")
    else:
        print("Running models")
        for feature_learning in feature_learnings:
            X, y, X_train, y_train = load(gv.DATA_FILE, 'cnt', drop=[], train_proportion=TRAIN_PROPORTION)
            print(f"=================\n{feature_learning}.\n--------")
            with open(f"./results/{feature_learning}{addition}.csv", "w", newline="") as outfile:
                writer = csv.writer(outfile)
                writer.writerow([ "method", "params", "model", "seed" , "avg_score", "best_score", "test_score", "grid_search_time", "time" ])

            for model in models:
                print(f"Running model: {model}")
                for idx, seed in enumerate(seeds):
                    print(f"{(idx/len(seeds)) * 100} %", end='\r')
                    start = time.time()

                    pipeline = Pipeline(steps=[('feature_learning', feature_learning.method(seed = seed)),
                                            ('model', model.evaluate(seed))])
                    estimator = FeatureLearningOptimization(param_grid=feature_learning.param_grid, pipeline=pipeline)
                    
                    with ignore_warnings(category=ConvergenceWarning):
                        utils.make_grid_search_ready(estimator.pipeline)
                        best_estimator = estimator.grid_search(X_train, y_train)
                        grid_search_time = time.time() - start
                        utils.make_evaluation_ready(estimator.pipeline)
                        scores = cv_time_series(best_estimator, X_train, y_train)
                        test_score = cv_time_series(best_estimator, X, y, splits = [TRAIN_PROPORTION])
                    
                    avg_score = np.mean(scores)
                    best_score = min(scores)
                    duration = time.time() - start
                    
                    csv_row = [ str(feature_learning), str(estimator.param_grid), str(model), seed, avg_score, best_score, test_score, grid_search_time, duration ]
                    with open(f"./results/{feature_learning}{addition}.csv", "a", newline="") as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(csv_row)
    
    if not PLOT_DATA:
        print("Warning: Not plotting data.")
    else:
        print("Plotting data")
        other_feature_learnings = ["M3GP_Gengy_FL_Domain_Knowledge-only-season", "M3GP_Gengy_FL_Domain_Knowledge-with-in-between"]
        dfs = [ pd.read_csv(f"./results/{feature_learning}.csv") for feature_learning in feature_learnings ]
        # dfs += [ pd.read_csv(f"./results/{feature_learning}.csv") for feature_learning in other_feature_learnings ]
        df = pd.concat(dfs)
        df['avg_score'] = -1 * df['avg_score']
        plot_combined_barplot_comparison(df)
        plot_separated_violin_comparisons(df)
        df['test_score'] = -1 * df['test_score']
        plot_combined_barplot_comparison(df, column="test_score")
        plot_separated_violin_comparisons(df, column="test_score")
    

    



