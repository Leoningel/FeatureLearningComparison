import pandas as pd



def load(path, target_column, delimiter=','):
    data = pd.read_csv(path, delimiter=delimiter)
    
    target = data[target_column]
    data = data.drop([target_column], axis=1)
    
    return data, target




