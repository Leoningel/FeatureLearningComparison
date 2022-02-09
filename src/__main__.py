import csv
from multiprocessing.pool import RUN
import time
from typing import List
import numpy as np
import pandas as pd
import sys

from data_extraction.data_extraction import load
from feature_preparation.core import FeatureLearning
from feature_preparation.no_feature_construction import NoFeatureLearning
from feature_preparation.feature_tools_FS import FeatureToolsFS
from feature_preparation.principle_component_analysis import Principle_CA
from model_generation.models import DecisionTree, RandomForest, MLP, SVM, Model
from evaluation.evaluation_metrics import cv_score
from evaluation.visualization import plot_comparison

from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning

N_SEEDS = 5   
CROSS_VALIDATION_GROUPS = 10
 
models : List[Model] = [ DecisionTree(), RandomForest(), MLP(), SVM() ]
feature_learnings : List[FeatureLearning] = [ NoFeatureLearning(), FeatureToolsFS(), Principle_CA() ]



if __name__ == '__main__':
    args = sys.argv
    RUN_MODELS = "--run_models" in args
    PLOT_DATA = "--plot_data" in args
        
    if not RUN_MODELS:
        print("Warning: Not running models. Using data stored.")
    else:
        print("Running models")
        X,y = load("data/boom bikes 14-01-2022.csv",'cnt')
        for feature_learning in feature_learnings:
            with open(f"./results/{feature_learning}.csv", "w", newline="") as outfile:
                writer = csv.writer(outfile)
                writer.writerow([ "method", "model", "seed" , "avg_score", "worse_score", "time" ])

            X_mapped = feature_learning.mapping(X)
            for model in models:
                for seed in range(N_SEEDS):
                    start = time.time()
                    mod = model.model(seed)
                    with ignore_warnings(category=ConvergenceWarning):
                        scores = cv_score(mod, X_mapped, y, CROSS_VALIDATION_GROUPS)
                    avg_score = np.mean(scores)
                    worse_score = min(scores)
                    duration = time.time() - start                
                    
                    csv_row = [ str(feature_learning), str(model), seed, avg_score, worse_score, duration ]
                    print(csv_row)
                    with open(f"./results/{feature_learning}.csv", "a", newline="") as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(csv_row)
    
    if not PLOT_DATA:
        print("Warning: Not plotting data. Using data stored.")
    else:
        print("Plotting data")
        dfs = [ pd.read_csv(f"./results/{feature_learning}.csv") for feature_learning in feature_learnings ]
        df = pd.concat(dfs)
        df['avg_score'] = -1 * df['avg_score']
        plot_comparison(df)
    

    



