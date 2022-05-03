import pandas as pd



def load_no_split(path, target_column, delimiter=',',drop=[]):
    data = pd.read_csv(path, delimiter=delimiter)
    
    target = data[target_column]
    data = data.drop([target_column], axis=1)
    data = data.drop(drop, axis=1)
    
    return data, target


def load(path, target_column, delimiter=',',drop=[], train_proportion: float = 0.75):
    '''
    Returns X, y, X_train, y_train
    '''
    
    
    data = pd.read_csv(path, delimiter=delimiter)
    
    target = data[target_column]
    data = data.drop([target_column], axis=1)
    data = data.drop(drop, axis=1)
    
    train_length = int(len(target) * train_proportion)
    
    return (data, target, data[:train_length], target[:train_length])


