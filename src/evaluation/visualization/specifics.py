from typing import List
import pandas as pd
import seaborn as sns
import glob
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

from feature_preparation.core import FeatureLearningMethod
import global_vars as gv
from model_generation.models import Model
from evaluation.visualization.utils import to_replace, FONTSIZE


def visualise_compare_fls(feature_learnings: List[FeatureLearningMethod], model: Model, column: str = 'fitness', per_column: str = 'number_of_the_generation', splits: List[float] = [ 0.75 ], added_text = '', folder = 'ml', output_folder='', f_score: bool = False):
    sns.set_style("darkgrid")
    sns.set_style({"font.family": "serif",
                   'font.size' : FONTSIZE
                   })

    li = []

    for feature_learning in feature_learnings:
        for split in splits:
            all_files = glob.glob(f"{gv.RESULTS_FOLDER}/{folder}/{feature_learning}/seed=*_model={model}_split={split}.csv")

            if split == 0.75:
                split = 'whole dataset'
            
            for idx, filename in enumerate(all_files):
                print(f"{round((idx/(len(all_files) + 1)) * 100,1)} %", end='\r')
                df = pd.read_csv(filename, index_col=None, header=0)
                df = df[[column, per_column]]
                df = df.replace(to_replace)
                # df = df[[column, per_column, "nodes"]]
                df = df.groupby([per_column]).min()
                fl = str(feature_learning)
                if fl in to_replace.keys():
                    fl = to_replace[fl]
                df['fl'] = fl
                df = df.reset_index()
                li.append(df)
        # print(f"Average nodes: {sum(list(map(lambda x: x.nodes.values[-1], li)))/len(li)}. FL method: {feature_learning}.")
        # print(f"Average generations: {sum(list(map(lambda x: x.number_of_the_generation.max(), li)))/len(li)}. FL method: {feature_learning}.")
        
    df = pd.concat(li, axis=0, ignore_index=True)
    
    plt.close()
    sns.set_style("darkgrid")
    sns.set(font_scale=1.2)
    sns.set_style({"font.family": "serif"})

    new_column = column 
    if column != 'nodes':
        if new_column == 'test_fitness':
            new_column = 'test fitness'
        if f_score:
            new_column = f'{column} (f1 score)'
        else:
            new_column = f'{column} (MSE)'
    else: 
        new_column = 'Number of nodes'
    new_per_column = 'Generations'
    df[new_column] = df[[column]]
    df[new_per_column] = df[[per_column]]

    a = sns.lineplot(
            data=df,
            x = new_per_column,
            y = new_column,
            hue = 'fl'
            )

    # a.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.ticklabel_format(axis='y', style="sci", scilimits=(-2,2))
    sns.set(font_scale=1.4)
    a.set_title(f"FL {new_column} comparison")
    plt.tight_layout()
    smodel = 'm=' + str(model)
    sfls = 'fl='
    for fl in feature_learnings:
        sfls += str(fl) + '_'
    path = f"plots/{output_folder}/g_{added_text}_{new_column}_{smodel}_{sfls}.pdf"
    plt.savefig(path)
    print(f"Saved figure to {path}.")


def visualise_compare_folders(folder_paths, fl_names, model: str, column: str = 'fitness', per_column: str = 'number_of_the_generation', added_text = '', output_folder='', f_score: bool = False):
    sns.set_style("darkgrid")
    sns.set_style({"font.family": "serif",
                   'font.size' : FONTSIZE
                   })

    li = []

    for jdx, folder_path in enumerate(folder_paths):
            all_files = glob.glob(f"{gv.RESULTS_FOLDER}/{folder_path}/seed=*_model={model}_split=*.csv")

            for idx, filename in enumerate(all_files):
                print(f"{round((idx/(len(all_files) + 1)) * 100,1)} %", end='\r')
                df = pd.read_csv(filename, index_col=None, header=0)
                df = df[[column, per_column]]
                # df = df[[column, per_column, "nodes"]]
                df = df.groupby([per_column]).min()
                df = df.replace(to_replace)
                try:
                    df['fl'] = fl_names[jdx]
                except:
                    df['fl'] = jdx
                df = df.reset_index()
                li.append(df)
        # print(f"Average nodes: {sum(list(map(lambda x: x.nodes.values[-1], li)))/len(li)}. FL method: {feature_learning}.")
        # print(f"Average generations: {sum(list(map(lambda x: x.number_of_the_generation.max(), li)))/len(li)}. FL method: {feature_learning}.")
        
    df = pd.concat(li, axis=0, ignore_index=True)
    plt.close()
    sns.set_style("darkgrid")
    sns.set(font_scale=1.2)
    sns.set_style({"font.family": "serif"})

    if column in ['fitness', 'test_fitness']:
        new_column = column
        if column == 'test_fitness':
            new_column = 'test fitness'
        if f_score:
            new_column = f'{new_column} (f1 score)'
        else:
            new_column = f'{new_column} (MSE)'
    new_per_column = 'Generations'
    df[new_column] = df[[column]]
    df[new_per_column] = df[[per_column]]

    a = sns.lineplot(
            data=df,
            x = new_per_column,
            y = new_column,
            hue = 'fl'
            )

    # a.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.ticklabel_format(axis='y', style="sci", scilimits=(-2,2))
    sns.set(font_scale=1.4)
    a.set_title(f"FL {new_column} comparison")
    plt.tight_layout()
    smodel = 'm=' + str(model)
    sfls = 'fl='
    for fl in fl_names:
        sfls += str(fl) + '_'
    path = f"plots/{output_folder}/g_{added_text}_{new_column}_{smodel}_{sfls}.pdf"
    plt.savefig(path)
    print(f"Saved figure to {path}.")


    
