from scipy import stats
import pandas as pd



def kolmogorov_smirnov(df1, df2, column, model):
    df1 = df1[df1['model'] == str(model)]
    df2 = df2[df2['model'] == str(model)]
    
    sample1 = df1[column].values
    sample2 = df2[column].values

    print(stats.kstest(sample1, sample2))
    print(stats.kstest(sample2, sample1))



