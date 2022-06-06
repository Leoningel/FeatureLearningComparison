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
    
    plt.close()
    sns.set_style({"font.family": "serif"})
    sns.set(font_scale=0.75)

    a = sns.lineplot(data=df, x = "number_of_the_generation", y = column)

    a.set_title(f"{feature_learning} {column}")
    plt.savefig(f"plots/test_single_file/seed={seed}_model={model}_split={split}.pdf")
    

def visualise_all_seeds(feature_learning: FeatureLearningMethod, split: float, model: Model, column: str = 'fitness'):

    all_files = glob.glob(f"{gv.RESULTS_FOLDER}/{feature_learning}/seed=*_model={model}_split={split}.csv")

    li = []

    for idx, filename in enumerate(all_files):
        print(f"{round((idx/(len(all_files) + 1)) * 100,1)} %", end='\r')
        df = pd.read_csv(filename, index_col=None, header=0)
        df = df[[column, "number_of_the_generation"]]
        df.groupby(['number_of_the_generation']).min()
        li.append(df)
    
    df = pd.concat(li, axis=0, ignore_index=True)
    
    plt.close()
    sns.set_style({"font.family": "serif"})
    sns.set(font_scale=0.75)

    a = sns.lineplot(data=df, x = "number_of_the_generation", y = column)

    a.set_title(f"{feature_learning} {column}")
    plt.savefig(f"plots/test_single_file/all_seeds_model={model}_split={split}.pdf")
    print(f"Done!!!")
    


    
