import csv
import os
from argparse import ArgumentParser
import shutil
import time
from typing import List
import sys
import warnings
warnings.filterwarnings('ignore')

from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning

import pandas as pd

import global_vars as gv
from data_extraction.data_extraction import load
from evaluation.visualization.specifics import visualise_compare_fls, visualise_compare_folders
from evaluation.visualization.complete import plot_separated_violin_comparisons
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

 
models : List[Model] = [ DecisionTree(), RandomForest(), MLP(), SVM() ]
feature_learnings : List[FeatureLearningMethod] = [ DKA_M3GP(), DK_M3GP(), M3GP_Gengy(), TraditionalGP(), PrincipleCA(), NoFeatureLearning() ]

if __name__ == '__main__':
    args = sys.argv
    RUN_MODELS = "--run_models" in args
    PLOT_DATA = "--plot_data" in args
    CLEAN_RESULTS = "--clean_results" in args
    TEST = "--test" in args
    ON_BUDGET = "--budget" in args
    seeds = [ int(arg.split("=")[1]) for arg in args if "--seed=" in arg ]
    if not seeds:
        seeds = range(gv.N_SEEDS)
    
    if CLEAN_RESULTS:
        try:
            dest_folder = next((gv.RESULTS_FOLDER + arg.split("=")[1]) for arg in args if '--dest=' in arg)
        except:
            raise ValueError("No destination is given. Add --dest=<destination_folder> to the arguments.")
        if os.path.isdir(dest_folder):
            raise FileExistsError(f"Destination folder ({dest_folder}) already exists. First delete the destination folder or save to another folder.")
        if dest_folder != './results/-':
            shutil.move(gv.TEMP_RESULTS_FOLDER, dest_folder)
            os.mkdir(f"{gv.TEMP_RESULTS_FOLDER}")
        for feature_learning in feature_learnings:
            os.mkdir(f"{gv.TEMP_RESULTS_FOLDER}{feature_learning}")
            with open(f"{gv.TEMP_RESULTS_FOLDER}{feature_learning}/main.csv", "w", newline="") as outfile:
                writer = csv.writer(outfile)
                writer.writerow([ "method", "params", "model", "seed", "train_score", "test_score", "grid_search_time", "time", "test_ind" ])

    
    if not RUN_MODELS:
        print("Warning: Not running models. Using data stored.")
    else:
        print("Running models")
        for feature_learning in feature_learnings:
            X, y, X_train, y_train = load(gv.DATA_FILE, target_column=gv.TARGET_COLUMN, drop=[], train_proportion=gv.TRAIN_PROPORTION)
            print(f"=================\n{feature_learning}.\n--------")
            
            for model in models:
                print(f"Running model: {model}")
                for idx, seed in enumerate(seeds):
                    print(f"{round((idx/len(seeds)) * 100,1)} %", end='\r')
                    start = time.time()

                    pipeline = utils.make_pipeline(feature_learning, model, seed)
                    estimator = FeatureLearningOptimization(param_grid=feature_learning.param_grid, pipeline=pipeline)
                    
                    with ignore_warnings(category=ConvergenceWarning):
                        # utils.make_grid_search_ready(estimator.pipeline, test=TEST)
                        # _, best_params = estimator.grid_search(X_train, y_train)
                        best_params = None
                        grid_search_time = time.time() - start
                        test_scores, train_scores, test_ind = utils.cv_time_series(feature_learning, model, seed, best_params, X, y, splits = [gv.TRAIN_PROPORTION], test=TEST, on_budget=ON_BUDGET, scoring=gv.SCORING)
                    
                    duration = time.time() - start
                    
                    csv_row = [ str(feature_learning), str(estimator.param_grid), str(model), seed, train_scores[0], test_scores[0], grid_search_time, duration, test_ind ]
                    with open(f"{gv.TEMP_RESULTS_FOLDER}{feature_learning}/main.csv", "a", newline="") as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(csv_row)
    
    if not PLOT_DATA:
        print("Warning: Not plotting data.")
    else:
        print("Plotting data")
        parser = ArgumentParser()
        parser.add_argument("-fl", "--featurelearnings", dest="featurelearnings", nargs='+', type=int, default=[])
        parser.add_argument("-m", "--models", dest="models", nargs='+', type=int, default=[])
        parser.add_argument('-pd', "--plot_data", dest='pd', action='store_const', const=True, default=False)
        parser.add_argument('-t', "--test", dest='test', action='store_const', const=True, default=False)
        parser.add_argument('-fn', "--folder_name", dest='folder_name', type=str)
        parser.add_argument('-out', "--outbasename", dest='outbasename', type=str, default='')
        parser.add_argument('-p', "--pairs", dest='pairs', type=int, nargs='+', default=[])
        parser.add_argument('-o', "--outliercorrection", dest='outliercorrection', action='store_const', const=True, default=False)
        parser.add_argument('-v', "--violin", dest='violin', action='store_const', const=True, default=False)
        parser.add_argument('-g', "--per_generation", dest='per_generation', action='store_const', const=True, default=False)
        parser.add_argument('-sp', "--specifics", dest='specifics', action='store_const', const=True, default=False)
        parser.add_argument('--time', dest='time', action='store_const', const=True, default=False)
        parser.add_argument('--nodes', dest='nodes', action='store_const', const=True, default=False)
        parser.add_argument('-pt', '--per_time', dest='per_time', action='store_const', const=True, default=False)
        parser.add_argument('-of', '--output_folder', dest='output_folder', type=str, default='')
        parser.add_argument('-ofs', '--output_folder_spec', dest='output_folder_spec', type=str, default='')
        args = parser.parse_args()
    
        feature_learnings : List[FeatureLearningMethod] = [ DKA_M3GP(), DK_M3GP(), M3GP_Gengy(), TraditionalGP(), M3GP_JB(), RandomSearchFS(), FeatureToolsFS(), PrincipleCA(), NoFeatureLearning() ]
        models = [ DecisionTree(), RandomForest(), MLP(), SVM() ]
        rel_fls = list()
        for fl in args.featurelearnings:
            rel_fls.append(feature_learnings[fl])
        rel_models = list()
        for m in args.models:
            rel_models.append(models[m])
        pairs = list()
        if args.pairs:
            pair_fls = list()
            if -1 in args.pairs:
                pair_fls = rel_fls
            else:
                for p in args.pairs:
                    pair_fls.append(rel_fls[p])
            for m in rel_models:
                for idx1, fl1 in enumerate(pair_fls):
                    for idx2, fl2 in enumerate(rel_fls):
                        if (str(fl1) != str(fl2)) and ((len(pair_fls) == len(rel_fls) and idx1 < idx2) or (len(pair_fls) != len(rel_fls))): 
                            pairs.append(((str(m), str(fl1)), (str(m), str(fl2))))

        folder_name = args.folder_name
        output_folder = args.output_folder
        data_info = pd.read_csv('data/data_info.csv')
        data_info = data_info.loc[data_info['NAME'] == output_folder.split('/')[-1]].values[0]
        DATA_FILE = data_info[1]
        TARGET_COLUMN = data_info[2]
        SCORING = data_info[3]
        f_score = SCORING == 'f_score'
            
        output_folder = f'{output_folder}/{args.output_folder_spec}'
        if args.violin:
            dfs = [ pd.read_csv(f"{gv.RESULTS_FOLDER}/{folder_name}/{feature_learning}/main.csv") for feature_learning in rel_fls ]
            if dfs:
                df = pd.concat(dfs)
            if args.test:
                plot_separated_violin_comparisons(df, models=rel_models, outbasename=args.outbasename, stat_test_pairs=pairs, take_out_outliers=args.outliercorrection, f_score=f_score, output_folder=output_folder)
            else:
                if args.time:
                    plot_separated_violin_comparisons(df, models=rel_models, outbasename=args.outbasename, stat_test_pairs=pairs, column='time', take_out_outliers=args.outliercorrection, f_score=f_score, output_folder=output_folder)
                else:
                    plot_separated_violin_comparisons(df, models=rel_models, outbasename=args.outbasename, stat_test_pairs=pairs, column='train_score', take_out_outliers=args.outliercorrection, f_score=f_score, output_folder=output_folder)
                 
        column = 'Fitness'
        if args.test:
            column = 'Test Fitness'
        elif args.nodes:
            column = 'Nodes'
        
        per_column = 'Generations'
        if args.per_time:
            per_column = 'time_since_the_start_of_the_evolution'
        if args.per_generation:
            for m in rel_models:
                visualise_compare_fls(rel_fls, splits = [ 0.75 ], model = m, added_text=args.outbasename, column=column, per_column = per_column, folder=folder_name, output_folder=output_folder, f_score=f_score)
        if args.specifics:
                visualise_compare_folders(folder_paths=["credit/max_depth_12_weighted/m3gp_gengy", "credit/max_depth_12_weighted/m3gp_jb"], fl_names = ["m3gp_gengy", "m3gp_jb"], model = 'DT', added_text=args.outbasename, column=column, per_column = per_column, output_folder=output_folder, f_score=f_score)
            

    
    

