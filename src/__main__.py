import csv
import os
import shutil
import time
from typing import List
import sys
import warnings
warnings.filterwarnings('ignore')

from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning

import numpy as np
import pandas as pd

import global_vars as gv
from data_extraction.data_extraction import load
from evaluation.visualization.specifics import visualise_all_seeds_compare_splits, visualise_compare_fls, visualise_single_file, visualise_all_seeds, visualise_all_seeds_all_splits
from evaluation.visualization.complete import plot_combined_barplot_comparison, plot_separated_violin_comparisons
from feature_preparation.core import FeatureLearningMethod, FeatureLearningOptimization
from feature_preparation.classical_methods.feature_tools_FS import FeatureToolsFS
from feature_preparation.classical_methods.no_feature_construction import NoFeatureLearning
from feature_preparation.classical_methods.principle_component_analysis import PrincipleCA
from feature_preparation.search_based.random_search import RandomSearchFS
from feature_preparation.search_based.traditional_gp import TraditionalGP
from feature_preparation.search_based.m3gp_jb import M3GP_JB
from feature_preparation.search_based.m3gp_gengy import M3GP_Gengy
from feature_preparation.search_based.dk_m3gp import DK_M3GP
from feature_preparation.search_based.dka_m3gp import DKA_M3GP
from model_generation.models import DecisionTree, RandomForest, MLP, SVM, Model
import utils as utils

N_SEEDS = 30   
TRAIN_PROPORTION = 0.75
 
models : List[Model] = [ DecisionTree(), RandomForest(), MLP(), SVM() ]
# feature_learnings : List[FeatureLearningMethod] = [ M3GP_JB() ]
feature_learnings : List[FeatureLearningMethod] = [ M3GP_Gengy(), DKA_M3GP(), DK_M3GP(), TraditionalGP(), RandomSearchFS() ]
# feature_learnings : List[FeatureLearningMethod] = [ PrincipleCA(), FeatureToolsFS(), NoFeatureLearning() ]
# feature_learnings : List[FeatureLearningMethod] = [ M3GP_Gengy(), M3GP_JB(), DKA_M3GP(), DK_M3GP(), TraditionalGP(), RandomSearchFS(), PrincipleCA(), FeatureToolsFS(), NoFeatureLearning() ]

if __name__ == '__main__':
    args = sys.argv
    RUN_MODELS = "--run_models" in args
    PLOT_DATA = "--plot_data" in args
    CLEAN_RESULTS = "--clean_results" in args
    seeds = [ int(arg.split("=")[1]) for arg in args if "--seed=" in arg ]
    if not seeds:
        seeds = range(N_SEEDS)
    
    if CLEAN_RESULTS:
        try:
            dest_folder = next((gv.RESULTS_FOLDER + arg.split("=")[1]) for arg in args if '--dest=' in arg)
        except:
            raise ValueError("No destination is given. Add --dest=<destination_folder> to the arguments.")
        if os.path.isdir(dest_folder):
            raise FileExistsError(f"Destination folder ({dest_folder}) already exists. First delete the destination folder or save to another folder.")
        shutil.move(gv.TEMP_RESULTS_FOLDER, dest_folder)
        os.mkdir(f"{gv.TEMP_RESULTS_FOLDER}")
        for feature_learning in feature_learnings:
            os.mkdir(f"{gv.TEMP_RESULTS_FOLDER}{feature_learning}")
            with open(f"{gv.TEMP_RESULTS_FOLDER}{feature_learning}/main.csv", "w", newline="") as outfile:
                writer = csv.writer(outfile)
                writer.writerow([ "method", "params", "model", "seed" , "avg_score", "best_score", "test_score", "grid_search_time", "time", "fittest_inds", "test_ind" ])

    
    if not RUN_MODELS:
        print("Warning: Not running models. Using data stored.")
    else:
        print("Running models")
        for feature_learning in feature_learnings:
            X, y, X_train, y_train = load(gv.DATA_FILE, 'cnt', drop=[], train_proportion=TRAIN_PROPORTION)
            print(f"=================\n{feature_learning}.\n--------")
            
            for model in models:
                print(f"Running model: {model}")
                for idx, seed in enumerate(seeds):
                    print(f"{round((idx/len(seeds)) * 100,1)} %", end='\r')
                    start = time.time()

                    pipeline = utils.make_pipeline(feature_learning, model, seed)
                    estimator = FeatureLearningOptimization(param_grid=feature_learning.param_grid, pipeline=pipeline)
                    
                    with ignore_warnings(category=ConvergenceWarning):
                        utils.make_grid_search_ready(estimator.pipeline)
                        best_estimator, best_params = estimator.grid_search(X_train, y_train)
                        grid_search_time = time.time() - start
                        utils.make_evaluation_ready(estimator.pipeline)
                        scores, fittest_inds = utils.cv_time_series(feature_learning, model, seed, best_params, X_train, y_train)
                        test_score, test_ind = utils.cv_time_series(feature_learning, model, seed, best_params, X, y, splits = [TRAIN_PROPORTION], additional_text='test_data_')
                    
                    avg_score = np.mean(scores)
                    best_score = min(scores)
                    duration = time.time() - start
                    
                    csv_row = [ str(feature_learning), str(estimator.param_grid), str(model), seed, avg_score, best_score, test_score, grid_search_time, duration, fittest_inds, test_ind ]
                    with open(f"{gv.TEMP_RESULTS_FOLDER}{feature_learning}/main.csv", "a", newline="") as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(csv_row)
    
    if not PLOT_DATA:
        print("Warning: Not plotting data.")
    else:
        print("Plotting data")
        dfs = [ pd.read_csv(f"{gv.RESULTS_FOLDER}{feature_learning}/main.csv") for feature_learning in feature_learnings ]
        df = pd.concat(dfs)
        df['best_score'] = -1 * df['best_score']
        plot_combined_barplot_comparison(df)
        plot_separated_violin_comparisons(df)
    
        # visualise_single_file(DKA_M3GP(), 0, gv.SPLITS[2], DecisionTree(), column = 'fitness')
        # visualise_all_seeds_all_splits(TraditionalGP(), DecisionTree(), column = 'fitness')
        # visualise_all_seeds_compare_splits(TraditionalGP(),splits = [ 0.5, 0.66, 0.83, 0.75 ], model = DecisionTree())
        # visualise_compare_fls([TraditionalGP(), DK_M3GP(), DKA_M3GP(), RandomSearchFS()],splits = [ 0.5, 0.66, 0.83, 0.75 ], model = DecisionTree())

    

