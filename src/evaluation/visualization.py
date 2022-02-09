import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_comparison(data, column='avg_score', log_scale=True):
    if type(data) == str:
        pd.read_csv(data)
        
    axis = sns.barplot(data=data, x='model', y=column, hue='method')
    if log_scale:
        axis.set_yscale("log")

    for item in axis.get_xticklabels():
            item.set_rotation(25)

    extra = ''
    if log_scale:
        extra = ' (data follows logarithmic scale)'
    plt.title(f"Feature learning {column}{extra}")
    plt.tight_layout()
    plt.savefig(f"plots/{column}_comparison.pdf")
    plt.close()

    
