from typing import List
import pandas as pd
import seaborn as sns
import glob
import matplotlib.pyplot as plt

from feature_preparation.core import FeatureLearningMethod
import global_vars as gv
from model_generation.models import Model



def visualise_single_file(feature_learning: FeatureLearningMethod, seed: int, split: float, model: Model, column: str = 'fitness'):
    df = pd.read_csv(f"{gv.RESULTS_FOLDER}/{feature_learning}/seed={seed}_model={model}_split={split}.csv")
    df = df[[column, "number_of_the_generation"]]
    df = df.groupby(['number_of_the_generation']).min()
    df = df.reset_index()
    
    plt.close()
    sns.set_style({"font.family": "serif"})
    sns.set(font_scale=0.75)

    a = sns.lineplot(data=df, x = "number_of_the_generation", y = column)

    a.set_title(f"{feature_learning} {column}")
    path = f"plots/test_single_file/{feature_learning}/seed={seed}_model={model}_split={split}.pdf"
    plt.savefig(path)
    print(f"Saved figure to {path}.")
    

def visualise_all_seeds(feature_learning: FeatureLearningMethod, split: float, model: Model, column: str = 'fitness'):

    all_files = glob.glob(f"{gv.RESULTS_FOLDER}/{feature_learning}/seed=*_model={model}_split={split}.csv")

    li = []

    for idx, filename in enumerate(all_files):
        print(f"{round((idx/(len(all_files) + 1)) * 100,1)} %", end='\r')
        df = pd.read_csv(filename, index_col=None, header=0)
        df = df[[column, "number_of_the_generation"]]
        df = df.groupby(['number_of_the_generation']).min()
        df = df.reset_index()
        li.append(df)
    
    df = pd.concat(li, axis=0, ignore_index=True)
    
    plt.close()
    sns.set_style({"font.family": "serif"})
    sns.set(font_scale=0.75)

    a = sns.lineplot(data=df, x = "number_of_the_generation", y = column)

    a.set_title(f"{feature_learning} {column}")
    path = f"plots/test_single_file/{feature_learning}/all_seeds_model={model}_split={split}.pdf"
    plt.savefig(path)
    print(f"Saved figure to {path}.")

def visualise_all_seeds_compare_splits(feature_learning: FeatureLearningMethod, model: Model, column: str = 'fitness', splits: List[float] = [ 0.75 ]):

    li = []

    for split in splits:
        all_files = glob.glob(f"{gv.RESULTS_FOLDER}/{feature_learning}/seed=*_model={model}_split={split}.csv")

        if split == 0.75:
            split = 'whole dataset'
        
        for idx, filename in enumerate(all_files):
            print(f"{round((idx/(len(all_files) + 1)) * 100,1)} %", end='\r')
            df = pd.read_csv(filename, index_col=None, header=0)
            df = df[[column, "number_of_the_generation"]]
            df = df.groupby(['number_of_the_generation']).min()
            df['split'] = str(split)
            df = df.reset_index()
            li.append(df)
        
    df = pd.concat(li, axis=0, ignore_index=True)
    
    plt.close()
    sns.set_style({"font.family": "serif"})
    sns.set(font_scale=0.75)

    a = sns.lineplot(
            data=df,
            x = "number_of_the_generation",
            y = column,
            hue = 'split'
            )

    a.set_title(f"{feature_learning} {column}")
    path = f"plots/test_single_file/{feature_learning}/all_seeds_model={model}_splits_comparison.pdf"
    plt.savefig(path)
    print(f"Saved figure to {path}.")
        

def visualise_all_seeds_all_splits(feature_learning: FeatureLearningMethod, model: Model, column: str = 'fitness'):

    all_files = glob.glob(f"{gv.RESULTS_FOLDER}/{feature_learning}/seed=*_model={model}_split=*.csv")

    li = []

    for idx, filename in enumerate(all_files):
        print(f"{round((idx/(len(all_files) + 1)) * 100,1)} %", end='\r')
        df = pd.read_csv(filename, index_col=None, header=0)
        df = df[[column, "number_of_the_generation"]]
        df = df.groupby(['number_of_the_generation']).min()
        df = df.reset_index()
        li.append(df)
    
    df = pd.concat(li, axis=0, ignore_index=True)
    
    plt.close()
    sns.set_style({"font.family": "serif"})
    sns.set(font_scale=0.75)

    a = sns.lineplot(data=df, x = "number_of_the_generation", y = column)

    a.set_title(f"{feature_learning} {column}")
    path = f"plots/test_single_file/{feature_learning}/seed=all_model={model}_split=all.pdf"
    plt.savefig(path)
    print(f"Saved figure to {path}.")
    

def visualise_compare_fls(feature_learnings: List[FeatureLearningMethod], model: Model, column: str = 'fitness', splits: List[float] = [ 0.75 ], added_text = '', server = 'ml'):

    li = []

    for feature_learning in feature_learnings:
        for split in splits:
            all_files = glob.glob(f"{gv.RESULTS_FOLDER}/{server}/{feature_learning}/seed=*_model={model}_split={split}.csv")

            if split == 0.75:
                split = 'whole dataset'
            
            for idx, filename in enumerate(all_files):
                print(f"{round((idx/(len(all_files) + 1)) * 100,1)} %", end='\r')
                df = pd.read_csv(filename, index_col=None, header=0)
                df = df[[column, "number_of_the_generation"]]
                df = df.groupby(['number_of_the_generation']).min()
                df['fl'] = str(feature_learning)
                df = df.reset_index()
                li.append(df)
        
    df = pd.concat(li, axis=0, ignore_index=True)
    
    plt.close()
    sns.set_style({"font.family": "serif"})
    sns.set(font_scale=0.75)

    a = sns.lineplot(
            data=df,
            x = "number_of_the_generation",
            y = column,
            hue = 'fl'
            )

    a.set_title(f"{column} comparison")
    path = f"plots/compare_fls_model={model}{added_text}.pdf"
    plt.savefig(path)
    print(f"Saved figure to {path}.")


    
