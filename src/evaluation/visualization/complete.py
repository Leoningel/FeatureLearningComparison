import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from scipy import stats
from statannotations.Annotator import Annotator

def plot_combined_barplot_comparison(df, outbasename: str = "_comparison", column : str = 'test_score', log_scale=True):
    if type(df) == str:
        df = pd.read_csv(df)
    
    
    to_replace = {
        "No_Feature_Learning": "No FL",
        "FeatureTools_FS": "FT FS",
    }
    
    df = df.replace(to_replace)

    plot_name = column
    if column == "avg_score":
        df['avg score (MSE)'] = df.avg_score
        column = "avg score (MSE)"
    elif column == "test_score":
        df['best score (MSE)'] = df.avg_score
        column = "best score (MSE)"
    elif column == "test_score":
        df['test score (MSE)'] = df.avg_score
        column = "test score (MSE)"
    
    axis = sns.barplot(data=df, x='model', y=column, hue='method',palette='Dark2')
    if log_scale:
        axis.set_yscale("log")

    for item in axis.get_xticklabels():
            item.set_rotation(25)
        
    extra = ''
    if log_scale:
        extra = ' - (logarithmic scale)'
        
    plt.title(f"Feature Learning {column}{extra}")
    plt.tight_layout()
    plt.savefig(f"plots/{plot_name}{outbasename} ({column}).pdf")
    plt.close()

def plot_separated_violin_comparisons(
    df: pd.DataFrame, models = None, outbasename: str = "_separated_violins", column : str = 'test_score', stat_test_pairs: list = None, take_out_outliers: bool = False, f_score=False
):
    """
    Draws violin plots for all examples.

    Each facet represents an example, which
    allows for the scale of the 'column' to reflect
    absolute values, rather than relative.
    """
    sns.set_style({"font.family": "serif"})
    sns.set(font_scale=0.75)
    
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

    # to_replace = {
    #     "No_FL": "No FL",
    #     "FeatureToolsFS": "FT FS",
    #     "random_search": "RS FS",
    # }
    # df = df.replace(to_replace)
    
    if models:
        models = [ str(m) for m in models ]
        df = df[ df['model'].isin(models) ]
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
    
    if len(models) > 1:
        g = sns.boxplot(x=x,
                        y=y,
                        hue=hue,
                        data=df)
    else:
        g = sns.boxplot(x=hue,
                        y=y,
                        data=df)

    # g.set_axis_labels("", column).set_titles("{col_name}").despine(left=True)
    # [plt.setp(ax.get_xticklabels(), rotation=45) for ax in g.axes.flat]
    
    if stat_test_pairs:
        if take_out_outliers:
            df = df_wo_outliers
        if len(models) > 1:
            annotator = Annotator(g, stat_test_pairs, data=df, x=x, y=y, hue=hue, plot='boxplot')
        else:
            annotator = Annotator(g, stat_test_pairs, data=df, x=hue, y=y, plot='boxplot')
        annotator.configure(test='Mann-Whitney', text_format='full', loc='outside')
        annotator.apply_and_annotate()
    
    # g.fig.suptitle(f"Feature Learning {column}")
    # if len(models) == 1:
    #     plt.title(f'{models[0]}')
    plt.tight_layout()
    smodels = 'm='
    for m in models:
        smodels += str(m) + '_'
    sfls = 'fl='
    for fl in df['method'].unique():
        sfls += str(fl) + '_'
    path = f"plots/v_{outbasename}_{column}_{smodels}_{sfls}.pdf"
    plt.savefig(path)
    sns.set(font_scale=1) 
    plt.close()
