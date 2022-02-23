import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_combined_barplot_comparison(df, outbasename: str = "_comparison", column : str = 'avg_score', log_scale=True):
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
    plt.savefig(f"plots/{plot_name}{outbasename}.pdf")
    plt.close()

def plot_separated_violin_comparisons(
    df: pd.DataFrame, outbasename: str = "_separated_violins", column : str = 'avg_score',
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
        "No_Feature_Learning": "No FL",
        "FeatureTools_FS": "FT FS",
        "RandomSearch_FS": "RS FS",
    }
    
    plot_name = column
    if column == "avg_score":
        df['avg score (MSE)'] = df.avg_score
        column = "avg score (MSE)"
    
    df = df.replace(to_replace)
    
    g = sns.catplot(x="method",
                    y=column,
                    sharey=False,
                    sharex=False,
                    palette='Dark2',
                    height=3.5,
                    # aspect=1, 
                    kind="violin",
                    col="model",
                    col_wrap=2,
                    # cut=0,
                    # fmt='.2',
                    data=df)

    g.set_axis_labels("", column).set_titles("{col_name}").despine(left=True)
    [plt.setp(ax.get_xticklabels(), rotation=45) for ax in g.axes.flat]
    
    g.fig.suptitle(f"Feature Learning {column}")
    plt.tight_layout()
    plt.savefig(f"plots/{plot_name}{outbasename}.pdf")
    sns.set(font_scale=1) 
