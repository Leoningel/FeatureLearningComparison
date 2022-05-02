import csv
import time
from typing import List
import sys
import warnings
warnings.filterwarnings('ignore')

from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning

import numpy as np
import pandas as pd

from data_extraction.data_extraction import load
from evaluation.evaluation_metrics import cv_score
from evaluation.visualization import plot_combined_barplot_comparison, plot_separated_violin_comparisons
from feature_preparation.core import FeatureLearningMethod, FeatureLearningOptimization
from feature_preparation.classical_methods.feature_tools_FS import FeatureToolsFS
from feature_preparation.classical_methods.no_feature_construction import NoFeatureLearning
from feature_preparation.classical_methods.principle_component_analysis import Principle_CA
from feature_preparation.search_based.random_search import RandomSearchFS
from feature_preparation.search_based.traditional_gp import TraditionalGP
from feature_preparation.search_based.m3gp_jb import M3GP_JB
from feature_preparation.search_based.m3gp_gengy import M3GP_Gengy
from feature_preparation.search_based.dk_m3gp import M3GP_DK_Gengy
from feature_preparation.search_based.dka_m3gp import DKA_M3GP
from model_generation.models import DecisionTree, RandomForest, MLP, SVM, Model
import utils

N_SEEDS = 5   
CROSS_VALIDATION_GROUPS = 2
 
models : List[Model] = [ DecisionTree(), RandomForest(), MLP(), SVM() ]
feature_learnings : List[FeatureLearningMethod] = [ DKA_M3GP() ]
# feature_learnings : List[FeatureLearningMethod] = [ DKA_M3GP(), M3GP_DK_Gengy(), M3GP_Gengy(), M3GP_JB(), TraditionalGP(), RandomSearchFS(), Principle_CA(), FeatureToolsFS(), NoFeatureLearning() ]



if __name__ == '__main__':
    args = sys.argv
    RUN_MODELS = "--run_models" in args
    PLOT_DATA = "--plot_data" in args
        
    if not RUN_MODELS:
        print("Warning: Not running models. Using data stored.")
    else:
        print("Running models")
        for feature_learning in feature_learnings:
            X,y = load(feature_learning.data_file,'cnt',drop=["instant"])
            print(f"=================\n{feature_learning}.\n--------")
            with open(f"./results/{feature_learning}.csv", "w", newline="") as outfile:
                writer = csv.writer(outfile)
                writer.writerow([ "method", "params", "model", "seed" , "avg_score", "worst_score", "grid_search_time", "time" ])

            for model in models:
                print(f"Running model: {model}")
                for seed in range(N_SEEDS):
                    print(f"{(seed/N_SEEDS) * 100} %", end='\r')
                    start = time.time()

                    pipeline = Pipeline(steps=[('feature_learning', feature_learning.method()),
                                            ('model', model.evaluate(seed))])
                    estimator = FeatureLearningOptimization(param_grid=feature_learning.param_grid, pipeline=pipeline)
                    
                    with ignore_warnings(category=ConvergenceWarning):
                        utils.make_grid_search_ready(estimator.pipeline)
                        best_estimator = estimator.grid_search(X,y)
                        grid_search_time = time.time() - start
                        utils.make_evaluation_ready(estimator.pipeline)
                        scores = cv_score(best_estimator, X, y, CROSS_VALIDATION_GROUPS)
                    
                    avg_score = np.mean(scores)
                    worse_score = min(scores)
                    duration = time.time() - start
                    
                    csv_row = [ str(feature_learning), str(estimator.param_grid), str(model), seed, avg_score, worse_score, grid_search_time, duration ]
                    with open(f"./results/{feature_learning}.csv", "a", newline="") as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(csv_row)
    
    if not PLOT_DATA:
        print("Warning: Not plotting data. Using data stored.")
    else:
        print("Plotting data")
        other_feature_learnings = ["M3GP_Gengy_FL_Domain_Knowledge-only-season", "M3GP_Gengy_FL_Domain_Knowledge-with-in-between"]
        dfs = [ pd.read_csv(f"./results/{feature_learning}.csv") for feature_learning in feature_learnings ]
        dfs += [ pd.read_csv(f"./results/{feature_learning}.csv") for feature_learning in other_feature_learnings ]
        df = pd.concat(dfs)
        df['avg_score'] = -1 * df['avg_score']
        plot_combined_barplot_comparison(df)
        plot_separated_violin_comparisons(df)
    

    



