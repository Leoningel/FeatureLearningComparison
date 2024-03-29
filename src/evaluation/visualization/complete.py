import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from scipy import stats
from statannotations.Annotator import Annotator
from evaluation.visualization.utils import to_replace, FONTSIZE

def plot_separated_violin_comparisons(
    df: pd.DataFrame, models = None, outbasename: str = "_separated_violins", column : str = 'test_score', stat_test_pairs: list = None, take_out_outliers: bool = False, f_score=False, output_folder=''):
    """
    Draws violin plots for all examples.

    Each facet represents an example, which
    allows for the scale of the 'column' to reflect
    absolute values, rather than relative.
    """
    
    score = 'MSE'
    if f_score:
        score = 'F1 score'
    
    if column == "avg_score":
        df[f"avg score ({score})"] = df.avg_score
        column = f"avg score ({score})"
    elif column == "train_score":
        df[f"train score ({score})"] = df.train_score
        column = f"train score ({score})"
    elif column == "test_score":
        df[f"test score ({score})"] = df.test_score
        column = f"test score ({score})"
    elif column == "time":
        df['Time (s)'] = df['time'] - df['grid_search_time']
        column = 'Time (s)'

    df = df.replace(to_replace)
    
    if models:
        models = [ str(m) for m in models ]
        df = df[ df['model'].isin(models) ]
    new_stat_test_pairs = list()
    for ((m1, fl1), (m2, fl2)) in stat_test_pairs:
        if fl1 in to_replace.keys():
            fl1 = to_replace[fl1]
        if fl2 in to_replace.keys():
            fl2 = to_replace[fl2]
        new_stat_test_pairs.append(((m1, fl1), (m2, fl2)))
    stat_test_pairs = new_stat_test_pairs
    
    if len(models) == 1:
        stat_test_pairs = [ (fl1, fl2) for ((_, fl1), (_, fl2)) in stat_test_pairs ]
    
    if take_out_outliers:
        df_wo_outliers = df
        print("Outliers:")
        for m in df['model'].unique():
            if 'MLP' == m:
                outlier_cutoff = 1
                print(df[[a and b for (a,b) in zip((np.abs(df[column]-df[column].median()) > (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] == m))]][['method', column, 'model']])
                df = df[[a or b for (a,b) in zip((np.abs(df[column]-df[column].median()) <= (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] != m))]]
                print(df[[a and b for (a,b) in zip((np.abs(df[column]-df[column].median()) > (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] == m))]][['method', column, 'model']])
                df = df[[a or b for (a,b) in zip((np.abs(df[column]-df[column].median()) <= (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] != m))]]
                print(df[[a and b for (a,b) in zip((np.abs(df[column]-df[column].median()) > (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] == m))]][['method', column, 'model']])
                df = df[[a or b for (a,b) in zip((np.abs(df[column]-df[column].median()) <= (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] != m))]]
                print(df[[a and b for (a,b) in zip((np.abs(df[column]-df[column].median()) > (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] == m))]][['method', column, 'model']])
                df = df[[a or b for (a,b) in zip((np.abs(df[column]-df[column].median()) <= (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] != m))]]
                print(df[[a and b for (a,b) in zip((np.abs(df[column]-df[column].median()) > (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] == m))]][['method', column, 'model']])
                df = df[[a or b for (a,b) in zip((np.abs(df[column]-df[column].median()) <= (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] != m))]]
                print(df[[a and b for (a,b) in zip((np.abs(df[column]-df[column].median()) > (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] == m))]][['method', column, 'model']])
                df = df[[a or b for (a,b) in zip((np.abs(df[column]-df[column].median()) <= (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] != m))]]
            outlier_cutoff = 3
            print(df[[a and b for (a,b) in zip((np.abs(df[column]-df[column].median()) > (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] == m))]][['method', column, 'model']])
            df = df[[a or b for (a,b) in zip((np.abs(df[column]-df[column].median()) <= (df[column].median() + outlier_cutoff*df[df['model'] == m][column].std())),(df['model'] != m))]]
                

    x = "model"
    y = column
    hue = 'method'
    sns.set_style("darkgrid")
    sns.set(font_scale=1.2)
    sns.set_style({"font.family": "serif"})
    
    if len(models) > 1:
        g = sns.boxplot(x=x,
                        y=y,
                        hue=hue,
                        data=df)
    else:
        g = sns.boxplot(x=hue,
                        y=y,
                        data=df)

    sns.set(font_scale=1)
    if stat_test_pairs:
        if take_out_outliers:
            df = df_wo_outliers
        if len(models) > 1:
            annotator = Annotator(g, stat_test_pairs, data=df, x=x, y=y, hue=hue, plot='boxplot')
        else:
            annotator = Annotator(g, stat_test_pairs, data=df, x=hue, y=y, plot='boxplot')
        annotator.configure(test='Mann-Whitney', text_format='star', loc='inside')
        annotator.apply_and_annotate()
    
    plt.xticks(rotation=25)
    g.set(xlabel=None)
    plt.tight_layout()
    smodels = 'm='
    for m in models:
        smodels += str(m) + '_'
    sfls = 'fl='
    for fl in df['method'].unique():
        sfls += str(fl) + '_'
    path = f"plots/{output_folder}/v_{outbasename}_{column}_{smodels}_{sfls}.pdf"
    plt.savefig(path)
    plt.close()
