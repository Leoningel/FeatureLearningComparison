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
    df: pd.DataFrame, outbasename: str = "_separated_violins", column : str = 'test_score', stat_test_pairs: list = None, take_out_outliers: bool = False,
):
    """
    Draws violin plots for all examples.

    Each facet represents an example, which
    allows for the scale of the 'column' to reflect
    absolute values, rather than relative.
    """
    sns.set_style({"font.family": "serif"})
    sns.set(font_scale=0.75)

    to_replace = {
        "No_FL": "No FL",
        "FeatureToolsFS": "FT FS",
        "random_search": "RS FS",
    }
    
    plot_name = column
    if column == "avg_score":
        df['avg score (MSE)'] = df.avg_score
        column = "avg score (MSE)"
    elif column == "best_score":
        df['best score (MSE)'] = df.best_score
        column = "best score (MSE)"
    elif column == "test_score":
        df['test score (MSE)'] = df.test_score
        column = "test score (MSE)"
    
    df = df.replace(to_replace)
    if take_out_outliers:
        outlier_cutoff = 15
        print("Outliers:")
        print(df[np.abs(df[column]-df[column].median()) > (outlier_cutoff*df[column].median())][['method', column, 'model']])
        df = df[np.abs(df[column]-df[column].median()) <= (outlier_cutoff*df[column].median())]
    
    x = "model"
    y = column
    hue = 'method'
    
    g = sns.boxplot(x=x,
                    y=y,
                    # sharey=False,
                    # sharex=False,
                    palette='Dark2',
                    # height=3.5,
                    # aspect=1, 
                    # kind="violin",
                    hue=hue,
                    # col_wrap=2,
                    # cut=0,
                    # fmt='.2',
                    data=df)

    # g.set_axis_labels("", column).set_titles("{col_name}").despine(left=True)
    # [plt.setp(ax.get_xticklabels(), rotation=45) for ax in g.axes.flat]
    
    if stat_test_pairs:
        annotator = Annotator(g, stat_test_pairs, data=df, x=x, y=y, hue=hue, plot='boxplot')
        annotator.configure(test='Mann-Whitney', text_format='full', loc='outside')
        annotator.apply_and_annotate()
    
    # g.fig.suptitle(f"Feature Learning {column}")
    plt.tight_layout()
    plt.savefig(f"plots/{plot_name}{outbasename} ({column}).pdf")
    sns.set(font_scale=1) 
